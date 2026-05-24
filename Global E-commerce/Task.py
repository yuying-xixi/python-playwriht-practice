import time
from asyncio import sleep

from Student import Student

from playwright.sync_api import sync_playwright, Page, ViewportSize
from playwright.sync_api import TimeoutError

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

    # 屏幕点击调试
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

    # 保存按钮
    @staticmethod
    def save_click(page: Page,  content='保 存', iframe_id='#iframe_window') -> None:
        try:
            # 1. 定位到第一层 iframe
            iframe = page.frame_locator(iframe_id)

            # 2. 动态定位按钮 (添加 exact=False 忽略空格和大小写差异)
            # 比如 content="保存"，即便 HTML 里是 "保 存" 或 "  保存  " 也能匹配到
            save_button = iframe.get_by_role("button", name=content, exact=False)

            print(f"正在尝试点击按钮: '{content}'")

            # 3. 等待并点击
            save_button.wait_for(state="visible", timeout=5000)
            save_button.click()
            print(f"成功点击按钮: '{content}'")

        except TimeoutError:
            print(f"超时：未能在5秒内找到或点击按钮 '{content}'，已自动跳过")
        except Exception as e:
            print(f"点击按钮 '{content}' 时发生其他错误: {e}，已自动跳过")

    # 提交并确认
    @staticmethod
    def confirm_commit_click(page: Page, iframe_id='#iframe_window') -> None:
        try:
            # 1. 定位到第一层 iframe
            iframe = page.frame_locator(iframe_id)

            # ================= 步骤 1：点击【提交】 =================
            try:
                # 在该 iframe 内通过角色(button)和名字(提交)定位按钮
                commit_button = iframe.get_by_role("button", name="提 交")

                # 等待按钮可见并点击
                commit_button.wait_for(state="visible", timeout=5000)
                commit_button.click()
                print("成功点击【提交】按钮")
            except TimeoutError:
                print("未在限定时间内检测到【提交】按钮，已跳过")
            except Exception as e:
                print(f"点击【提交】时发生其他错误: {e}，已跳过")

            # ================= 步骤 2：点击【确定】 =================
            try:
                # 在该 iframe 内通过角色(button)和名字(确认)定位按钮
                confirm_button = iframe.get_by_role("button", name="确 定")

                # 点击
                confirm_button.wait_for(state="visible", timeout=5000)
                confirm_button.click()
                print("成功点击【确定】按钮")
            except TimeoutError:
                print("未在限定时间内检测到【确定】按钮，已跳过")
            except Exception as e:
                print(f"点击【确定】时发生其他错误: {e}，已跳过")

        except Exception as main_e:
            print(f"Iframe 定位或整体流程发生重大异常: {main_e}")


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

    # 拖动
    @staticmethod
    def drag_by_coords(page, start, end, steps=20, scroll_to_top=True):
        """
        按坐标拖动

        :param page: Playwright page
        :param start: (x, y) 起始坐标
        :param end: (x, y) 终止坐标
        :param steps: 拖动轨迹平滑度
        :param scroll_to_top: 是否滚动到顶部避免坐标偏移
        """

        if scroll_to_top:
            page.evaluate("window.scrollTo(0, 0)")

        start_x, start_y = start
        end_x, end_y = end

        page.mouse.move(start_x, start_y)
        page.mouse.down()

        for i in range(steps):
            x = start_x + (end_x - start_x) * i / steps
            y = start_y + (end_y - start_y) * i / steps
            page.mouse.move(x, y)

        page.mouse.up()

    # 获取cookie
    def get_headers_cookie(self, page, x=0, y=0, url_keyword="suitanglian.com", timeout=20000):
        """
        通过拦截网络请求获取请求头中的 cookie
        :param page: Playwright 的 page 对象
        :param x: int 触发捕获的点击x坐标
        :param y: int 触发捕获的点击y坐标
        :param url_keyword: 过滤请求的关键词，默认为域名
        :param timeout: 等待请求的超时时间（毫秒）
        :return: 找到的 cookie 字符串，如果没找到则返回 None
        """
        try:
            # 定义筛选规则：URL包含关键词 且 Header里有 cookie
            check_func = lambda req: url_keyword in req.url and "cookie" in req.headers

            # 使用 with 启动监听
            if x or y:
                with page.expect_request(check_func, timeout=timeout) as request_info:
                    self.debug_click(page, x, y)
            else:
                with page.expect_request(check_func, timeout=timeout) as request_info:
                    self.save_click(page)

            # 提取并返回 cookie
            return request_info.value.headers

        except Exception as e:
            print(f"获取 headers 失败或超时: {e}")
            return None

    # 点击确认并提交
    def submit_and_confirm(self, page, *points):
        page.wait_for_load_state("domcontentloaded")
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
        page.wait_for_load_state("domcontentloaded")

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

        try:
            with self.context.expect_page(timeout=3000) as new_page_info:
                print("进行点击")
                self.screen_click(self.home, 720, 210)

            print("进入实验选择页面成功")
            return new_page_info.value

        except TimeoutError:
            print("进入实验页面超时，跳过")
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

        page.wait_for_load_state("domcontentloaded")

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

        try:
            with self.context.expect_page(timeout=3000) as new_page_info:
                self.screen_click(page, x, y)

            new_page = new_page_info.value
            print(f"捕获到新页面: {new_page.url}")
            return new_page

        except TimeoutError:
            print("没有新标签页，继续当前页面")

            page.wait_for_timeout(2000)

            print(f"当前页面: {page.url}")
            return page

