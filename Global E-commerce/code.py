from playwright.sync_api import sync_playwright, Page
from time import sleep

url = r"https://3d.suitanglian.com/kjds/BusinessDataTask/index.html?url=https://www.suitanglian.com:3018/api/market_select/initJson&token=009a04e154b9a9e36f21cc9a8881ec13dbf0a54e83b1b0550588b003e19485168f484b1f488125d66f6ca1e3e910d1c5965460b8bbbc9c5a15f7805562bdc747bf4ef91ecb03de6df88f7a546568d6afe1d6d19cbd902cadeb0ac16ed9ef38658698a3c0cffb0a95ead33f750912a49d1a1bf022a56e0781ccd9971487aa640394764e253e4cfa9d76ef1d7e895e888b11cc0b00b1ef0c5c5cdb7e92d2f039bd&record_id=19086"


def click_confirm_button(page, main_btn_name="提 交", confirm_btn_name="确 定", timeout=5000):
    """
    二次确认按钮点击封装
    :param page: Playwright 的 page 对象
    :param main_btn_name: 第一个点击的按钮文字（如：提交）
    :param confirm_btn_name: 弹窗中需要确认的按钮文字（如：确定）
    :param timeout: 等待按钮出现的最大时间（毫秒）
    :return: None
    """
    try:
        # 1. 点击初始按钮
        # exact=False 自动处理文字中的空格或换行
        main_button = page.get_by_role("button", name=main_btn_name, exact=False)
        main_button.click(timeout=timeout)
        print(f"已点击初次按钮: {main_btn_name}")

        # 2. 定位确认按钮
        confirm_button = page.get_by_role("button", name=confirm_btn_name, exact=False)

        # 3. 显式等待按钮可见（处理弹窗动画）
        confirm_button.wait_for(state="visible", timeout=timeout)

        # 4. 执行第二次点击
        confirm_button.click()
        print(f"已点击确认按钮: {confirm_btn_name}")

    except Exception as e:
        print(f"点击流程失败: {e}")
        # 根据需要决定是抛出异常还是静默处理
        raise e

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

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()

    page.goto(url)
    sleep(20)

    x, y = 700, 680
    _debug_click(page, x, y)
    sleep(10)
    click_confirm_button(page)
