import time
from Student import Student
from playwright.async_api import Error

from playwright.sync_api import sync_playwright, Page

class Task(Student):
    # 登录地址
    url = r'https://www.suitanglian.com/#/login'

    # 实验主页
    home = ''
    def __init__(self, student_name: int, student_password: int):
        super().__init__(student_name, student_password)
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.firefox.launch(headless=False)
        self.context = self.browser.new_context()

        login_page = self.login()
        if not login_page:
            print("用户登录失败!!!检查账号或密码")
            exit()
        # 存储实验主页
        self.home = self.enter_practice(login_page)

    # 退出
    def close(self):
        self.context.close()
        self.browser.close()
        self.playwright.stop()

    # 屏幕点击实现及调试
    @staticmethod
    def _debug_click(page: Page, x: int, y: int) -> None:
        """
        在指定的 x, y 坐标模拟点击，并立即在该位置显示一个红点调试动画。
        :param page :playwright单页面对象 : 用于控制和操作浏览器中单个页面的对象
        :param x: int : 执行点击操作的x坐标
        :param y: int : 执行点击操作的y坐标
        :return page对象: 点击后新刷新或新的页面
        """
        #  在浏览器前端注入 JavaScript 产生红点动画
        page.evaluate(f"""
            ((x, y) => {{
                const dot = document.createElement('div');
                dot.style.position = 'fixed'; // 使用 fixed 确保相对于视口
                dot.style.width = '20px';
                dot.style.height = '20px';
                dot.style.background = 'red';
                dot.style.borderRadius = '50%';
                dot.style.left = (x - 10) + 'px';
                dot.style.top = (y - 10) + 'px';
                dot.style.zIndex = '1000000';
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

        #  调用 Playwright 底层接口模拟真实鼠标移动和点击
        page.mouse.move(x, y)
        page.mouse.click(x, y)
        print(f"已点击 ({x}, {y})")

    # x-token抓取
    @staticmethod
    def get_x_token(page, url_keyword="suitanglian.com", timeout=5000):
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
            return request_info.value.headers.get('x-token')

        except Exception as e:
            print(f"获取 Token 失败或超时: {e}")
            return None

    # 登录学生账号的实现
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

    # 进入实验主页面脚本实现
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

    # 实验主页面选择项目和任务脚本
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
            self._debug_click(self.home, 720, 210)
        if new_page_info:
            print("进入实验选择页面成功")
            return new_page_info.value
        return None

    # 练习主页面选择练习模块脚本
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

        # 注意
        # 若进入实验动画渲染时间太长可适当增加sleep时间
        # 注意
        page.reload(wait_until="networkidle")
        time.sleep(10)

        # 根据坐标点击，捕获新页面
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

    # 捕获点击后的新页面，无新页面返回None
        with self.context.expect_page() as new_page_info:
            self._debug_click(page, x, y)

        # 没有捕获到新页面，返回None
        if new_page_info:
            new_page = new_page_info.value
        else:
            new_page = None

        return new_page
