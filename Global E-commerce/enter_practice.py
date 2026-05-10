from playwright.sync_api import sync_playwright
import time

# 屏幕点击实现及调试
def debug_click(page, context, x, y):
    """
    在指定的 x, y 坐标模拟点击，并立即在该位置显示一个红点调试动画。
    :param page :playwright单页面对象 : 用于控制和操作浏览器中单个页面的对象
    :param context: 浏览器上下文
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
    print(f"Debug Click: Clicked at ({x}, {y})")

    # 尝试捕获新打开的页面
    with context.expect_page() as new_page_info:
        pass  # 这里不需要额外的操作，因为点击已经在上面完成了

    # 检查是否捕获到了新的页面
    if new_page_info.value:
        new_page = new_page_info.value
        print("New page opened.")
        print(new_page)
        return new_page
    else:
        print("No new page opened. Returning the current page.")
        print(page)
        return page

# 登录功能
def login(page, username, password):
    """
    给定学生的用户名和密码完成登录操作,并返回登录后的页面对象
    :param page: 页面对象
    :param username: int : 学生用户名
    :param password: int : 学生登录密码
    :return:  页面对象: 返回登录后新页面的对象
    """
    page.get_by_label("学生").click()

    page.fill('input[placeholder="请输入学号"]', str(username))
    page.fill('input[placeholder="密码"]', str(password))

    time.sleep(1)
    page.get_by_role("button", name="登 录").click()
    print(f"成功登录学号: {username}")

# 进入实验主页面
def enter_practice(page, context):
    """
     进入实验主页
    :param page: 页面对象
    :param context: 浏览器上下文
    :return: 进入实验主页后的新页面
    :param page:
    :param context:
    :return:
    """

    # 寻找并点击新工商实验
    page.locator('//div[@class="sch_con_left"]/button[1]').click()
    page.locator('text=新商科').click()

    # 定位第一个实验练习卡片 (使用 nth(0) 对应之前的 [1])
    card = page.locator('xpath=(//div[@class="sch_list_item"])[1]')
    card.wait_for(state="visible", timeout=10000)

    btn = card.locator("button")

    # 点击进入实验主页,并且记录下新页面
    with context.expect_page() as new_page_info:
        btn.evaluate("node => node.click()")

    # 获取新打开的页面对象
    new_page = new_page_info.value

    #  等待页面内容变化,等待网络空闲或特定元素消失/出现
    page.wait_for_load_state("networkidle")

    print(f"成功进入实验主页，新窗口标题: {new_page.title()}")

    return new_page

# 选择实验并进入
def choose_project_task(page, context, project_number, task_number):
    """
    选择进入对应的实验以及实验项目
    :param page:
    :param context:
    :param project_number: int: 实验编号
    :param task_number: int: 项目编号
    :return: 进入习题页面的网址
    """
    # 1. 定位大的项目块 (项目一、项目二等)
    project = page.locator(".rationalism-left-item").nth(project_number - 1)

    # 2. 定位任务块
    # 在 project 内部寻找第 N 个任务主容器
    task_main = project.locator(".rationalism-left-task-main").nth(task_number - 1)

    # 3. 定位具体的任务文字所在的 div
    task = task_main.locator(".rationalism-left-task")

    # --- 增加等待和可见性检查 ---
    # 有些任务可能是隐藏的，需要滚动并等待
    task.scroll_into_view_if_needed()

    # 强制等待元素可以被点击（防止动画干扰）
    task.wait_for(state="visible", timeout=10000)

    # 点击任务
    task.click()

    time.sleep(3)

    with context.expect_page() as new_page_info:
        print("进行点击")
        debug_click(page, context, 720, 210)

    # 获取新打开的页面对象
    new_page = new_page_info.value

    # 注意
    # 若进入实验动画渲染时间太长可适当增加sleep时间
    # 注意
    time.sleep(20)

    # 两个选项
    debug_click(new_page, context, 580, 680)
    # debug_click(new_page, context, 700, 680)

    return new_page

def run():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)

        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.suitanglian.com/#/login")

        login(page, 241438010104, 123456)

        # 返回实验主页
        home_page = enter_practice(page, context)

        lab_page = choose_project_task(home_page, context, 2, 2)

        print(lab_page)

        time.sleep(100)
        browser.close()


if __name__ == "__main__":
    run()