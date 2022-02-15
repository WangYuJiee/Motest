from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='login_data.json')

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # # Click text=项目
    # page.click("text=项目")
    # # assert page.url == "https://momodel.cn/explore"
    #
    # # Click button:has-text("新建项目")
    # page.click("button:has-text(\"新建项目\")")

    # # Click text=密码登录
    # page.click("text=密码登录")他 不过红包v
    #
    # # Click [placeholder="请输入已注册的账户"]
    # page.click("[placeholder=\"请输入已注册的账户\"]")
    #
    # # Fill [placeholder="请输入已注册的账户"]
    # page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")
    #
    # # Click [placeholder="请输入密码"]
    # page.click("[placeholder=\"请输入密码\"]")
    #
    # # Fill [placeholder="请输入密码"]
    # page.fill("[placeholder=\"请输入密码\"]", "123456")
    #
    # # Click button:has-text("登录")
    # # with page.expect_navigation(url="https://momodel.cn/explore"):
    # with page.expect_navigation():
    #     page.click("button:has-text(\"登录\")")

    # Click a:nth-child(2) .index_content-3VvHd .index_contentImg-2rj4G
    page.click("a:nth-child(2) .index_content-3VvHd .index_contentImg-2rj4G")
    # assert page.url == "https://momodel.cn/explore/5bfb634e1afd943c623dd9cf?type=app"

    # Click button:has-text("Fork")
    page.click("button:has-text(\"Fork\")")

    # Click [placeholder="请输入不超过50个字符"]
    page.click("[placeholder=\"请输入不超过50个字符\"]")

    # Fill [placeholder="请输入不超过50个字符"]
    page.fill("[placeholder=\"请输入不超过50个字符\"]", "图像风格迁移 - Style321 Transfer")

    # Click button:has-text("确定")
    page.click("button:has-text(\"确定\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
