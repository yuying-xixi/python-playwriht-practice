import time
from Student import Student

from playwright.sync_api import sync_playwright, Page, ViewportSize

class Task(Student):
    # 登录地址
    url = r'https://www.suitanglian.com/#/login'

    # 实验主页
    home = ''
    def __init__(self, student_name: int, student_password: int):
        super().__init__(student_name, student_password)
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=False)
        self.context = self.browser.new_context(viewport=ViewportSize(width=1280, height=720))

        login_page = self.login()
        if not login_page:
            print("用户登录失败!!!检查账号或密码")
            exit()
        # 存储实验主页
        self.home = self.enter_practice(login_page)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        self.close()

    # 浏览器退出
    def close(self):
        try:
            if hasattr(self, "context"):
                self.context.close()
        except:
            pass

        try:
            if hasattr(self, "browser"):
                self.browser.close()
        except:
            pass

        try:
            if hasattr(self, "playwright"):
                self.playwright.stop()
        except:
            pass

    # 打印浏览器窗口信息,并设置浏览器窗口大小
    @staticmethod
    def browser_info(page):
        view_size = page.viewport_size
        print("当前浏览器视口宽：", view_size["width"])
        print("当前浏览器视口高：", view_size["height"])

    # 浏览器窗口切换
    def close_current_and_return(self):
        pages = self.context.pages
        if len(pages) > 1:
            current_page = pages[-1]
            previous_page = pages[-2]

            current_page.close()
            # 将上一个页面升至最前（可见状态）
            previous_page.bring_to_front()
            return previous_page
        else:
            print("没有可以返回的上级页面")
            return self.context.pages[0]

    # 屏幕点击调试
    @staticmethod
    def screen_click(page: Page, x: int, y: int) -> None:

        page.evaluate(f"""
            ((x, y) => {{
                const dot = document.createElement('div');

                dot.style.position = 'fixed';
                dot.style.width = '20px';
                dot.style.height = '20px';
                dot.style.background = 'red';
                dot.style.borderRadius = '50%';
                dot.style.left = (x - 10) + 'px';
                dot.style.top = (y - 10) + 'px';

                dot.style.zIndex = '1000000';

                // 关键
                dot.style.pointerEvents = 'none';

                dot.style.transition = 'opacity 0.6s, transform 0.6s';
                dot.style.opacity = '0.8';

                document.body.appendChild(dot);

                setTimeout(() => {{
                    dot.style.opacity = '0';
                    dot.style.transform = 'scale(2.5)';
                }}, 10);

                setTimeout(() => {{
                    dot.remove();
                }}, 10000);

            }})({x}, {y})
        """)

        page.mouse.move(x, y)
        page.mouse.click(x, y)

        print(f"已点击 ({x}, {y})")

    @staticmethod
    def debug_click(page: Page, x: int, y: int) -> None:
        page.evaluate(f"""
            ((x, y) => {{

                const wrapper = document.createElement('div');

                wrapper.style.position = 'fixed';
                wrapper.style.left = x + 'px';
                wrapper.style.top = y + 'px';
                wrapper.style.zIndex = '999999';
                wrapper.style.pointerEvents = 'none';

                // 红点
                const dot = document.createElement('div');
                dot.style.width = '16px';
                dot.style.height = '16px';
                dot.style.background = 'red';
                dot.style.borderRadius = '50%';
                dot.style.border = '2px solid white';
                dot.style.boxShadow = '0 0 10px red';

                // 坐标文字
                const label = document.createElement('div');
                label.innerText = `(${x}, ${y})`;

                label.style.color = 'red';
                label.style.fontSize = '14px';
                label.style.fontWeight = 'bold';
                label.style.background = 'white';
                label.style.padding = '2px 6px';
                label.style.borderRadius = '4px';
                label.style.marginTop = '4px';

                wrapper.appendChild(dot);
                wrapper.appendChild(label);

                document.body.appendChild(wrapper);

            }})({x}, {y})
        """)

        # 坐标监听器
        page.evaluate("""
                      (() => {

                          const box = document.createElement('div');

                          box.id = '__mouse_debug_box__';

                          box.style.position = 'fixed';
                          box.style.top = '10px';
                          box.style.right = '10px';
                          box.style.zIndex = '999999';
                          box.style.background = 'black';
                          box.style.color = 'lime';
                          box.style.padding = '8px';
                          box.style.fontSize = '16px';
                          box.style.fontWeight = 'bold';

                          document.body.appendChild(box);

                          document.addEventListener('mousemove', (e) => {
                              box.innerText = `X: ${e.clientX}, Y: ${e.clientY}`;
                          });

                      })();
                      """)

        page.mouse.move(x, y)
        page.mouse.click(x, y)

        print(f"已点击 ({x}, {y})")

    # headers获取
    @staticmethod
    def get_headers_token(page, url_keyword="suitanglian.com", timeout=20000):
        """
        通过拦截网络请求获取请求头中的 x-token
        :param page: Playwright 的 page 对象
        :param url_keyword: 过滤请求的关键词，默认为域名
        :param timeout: 等待请求的超时时间（毫秒）
        :return: 找到的 token 字符串，如果没找到则返回 None
        """
        try:
            # 定义筛选规则：URL包含关键词 且 Header里有 x-token
            check_func = lambda req: url_keyword in req.url and "x-token" in req.headers

            # 使用 with 启动监听
            with page.expect_request(check_func, timeout=timeout) as request_info:
                # 触发页面刷新
                page.reload()

            # 提取并返回 token
            return request_info.value.headers

        except Exception as e:
            print(f"获取 headers 失败或超时: {e}")
            return None


    def get_headers_cookie(self, page, url_keyword="suitanglian.com", timeout=20000):
        """
        通过拦截网络请求获取请求头中的 cookie
        :param page: Playwright 的 page 对象
        :param url_keyword: 过滤请求的关键词，默认为域名
        :param timeout: 等待请求的超时时间（毫秒）
        :return: 找到的 cookie 字符串，如果没找到则返回 None
        """
        try:
            # 定义筛选规则：URL包含关键词 且 Header里有 cookie
            check_func = lambda req: url_keyword in req.url and "cookie" in req.headers

            # 使用 with 启动监听
            with page.expect_request(check_func, timeout=timeout) as request_info:
                # 触发页面刷新
                self.debug_click(page, 1120, 80)

            # 提取并返回 cookie
            return request_info.value.headers

        except Exception as e:
            print(f"获取 headers 失败或超时: {e}")
            return None

    # 点击确认并提交
    def submit_and_confirm(self, page, *points):
        page.wait_for_load_state("networkidle")
        time.sleep(5)

        for i, (x, y) in enumerate(points):
            self.screen_click(page, x, y)

            # 最后一次点击不等待
            if i < len(points) - 1:
                time.sleep(1)

    # 登录学生账号
    def login(self) -> Page|None:
        """
        通过学生的用户名和密码完成登录操作,并返回登录后的页面对象
        :param 登录页面的页面对象
        :return: 登录成功后新的页面的对象,登录失败返回None
        """

        page = self.context.new_page()

        page.goto(self.url)

        page.get_by_label("学生").click()

        page.fill('input[placeholder="请输入学号"]', str(self.username))
        page.fill('input[placeholder="密码"]', str(self.password))

        time.sleep(1)
        page.get_by_role("button", name="登 录").click()
        print(f"成功登录学号: {self.username}")
        if page is not None:
            return page
        else:
            return None

    # 进入实验主页面
    def enter_practice(self, page: Page) -> Page|None:
        """
        进入实验主页
        :param page: 页面对象
        :return: 实验主页的页面对象或None
        """

        # 寻找并点击新工商实验
        page.locator('//div[@class="sch_con_left"]/button[1]').click()
        page.locator('text=新商科').click()

        # 定位第一个实验练习卡片 (使用 nth(0) 对应之前的 [1])
        card = page.locator('xpath=(//div[@class="sch_list_item"])[1]')
        card.wait_for(state="visible", timeout=10000)

        btn = card.locator("button")

        # 点击进入实验主页,并且记录下新页面
        with self.context.expect_page() as new_page_info:
            btn.evaluate("node => node.click()")

        # 获取新打开的页面对象
        new_page = new_page_info.value

        #  等待页面内容变化,等待网络空闲或特定元素消失/出现
        page.wait_for_load_state("networkidle")

        print(f"成功进入实验主页，新窗口标题: {new_page.title()}")
        return new_page

    # 实验主页面选择项目和任务,并进入练习模块
    def choose_project_task(self,  project_number: int, task_number: int) -> Page|None:
        """
        选择进入对应的实验以及实验项目
        :param project_number: int: 实验编号
        :param task_number: int: 项目编号
        :return: 进入习题页面的页面对象
        """
        # 定位大的项目块 (项目一、项目二等)
        project = self.home.locator(".rationalism-left-item").nth(project_number - 1)

        # 定位任务块(任务一,任务二)
        task_main = project.locator(".rationalism-left-task-main").nth(task_number - 1)

        # 定位具体的任务文字所在的 div
        task = task_main.locator(".rationalism-left-task")

        # 有些任务可能是隐藏的，滚动并等待
        task.scroll_into_view_if_needed()

        # 强制等待元素可以被点击
        task.wait_for(state="visible", timeout=10000)

        # 选择任务块
        task.click()

        # 等待进入实验按钮加载
        time.sleep(2)

        # 捕获点击"进入实验"后的新页面
        with self.context.expect_page() as new_page_info:
            print("进行点击")
            self.screen_click(self.home, 720, 210)
        if new_page_info:
            print("进入实验选择页面成功")
            return new_page_info.value
        return None

    # 选择练习模块,并进入练习
    def start_practice(self, page, choose_practice_index, practice_number=2):
        """
        选择训练目标
        :param page: 习题页面的页面对象
        :param choose_practice_index: int: 选择第几个训练模块(1, 2, 3)
        :param practice_number: int: 页面有几个训练模块(2, 3)
        :return: page对象: 进入练习模块页面的新对象
        """
        if practice_number not in {2, 3}:
            print(f"页面训练模块数量错误,不存在{practice_number}块")
            exit()
        if choose_practice_index > practice_number:
            print(f"不存在第{choose_practice_index}个训练模块")
            exit()

        page.wait_for_load_state("networkidle")

        time.sleep(10)

        if practice_number == 2:
            if choose_practice_index == 1:
                x, y = 580, 680
            else:
                x, y = 700, 680
        else:
            if choose_practice_index == 1:
                x, y = 500, 680
            elif choose_practice_index == 2:
                x, y = 650, 680
            else:
                x, y = 780, 680

        # 记录点击前已有的页面
        pages_before = self.context.pages

        self.screen_click(page, x, y)
        time.sleep(3)  # 等待页面响应

        # 检查是否有新页面出现
        pages_after = self.context.pages
        new_pages = [p for p in pages_after if p not in pages_before]

        if new_pages:
            # 情况1: 打开了新标签页
            new_page = new_pages[-1]
            new_page.wait_for_load_state("networkidle")
            print(f"捕获到新页面: {new_page.url}")
            return new_page
        else:
            # 情况2: 在当前页面内跳转
            page.wait_for_load_state("networkidle")
            print(f"当前页面跳转: {page.url}")
            return page
