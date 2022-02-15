from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=自然语言处理：自然语言生成
    page.click("text=自然语言处理：自然语言生成")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af39ed&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af39ed&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=免费加入课程 >> i
    page.click("text=免费加入课程 >> i")

    # Click div[role="document"] button:has-text("加入课程")
    page.click("div[role=\"document\"] button:has-text(\"加入课程\")")

    # Go to https://momodel.cn/workspace/61efadabdca63ce48d4b8bb9/app
    page1.goto("https://momodel.cn/workspace/61efadabdca63ce48d4b8bb9/app")

    # Click text=自然语言生成介绍
    page1.once("dialog", lambda dialog: dialog.dismiss())
    page1.click("text=自然语言生成介绍")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
