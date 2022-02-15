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

    # Click text=卷积神经网络深度学习基础系列
    page.click("text=卷积神经网络深度学习基础系列")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc52&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Press Enter
    page.press("[placeholder=\"请输入已注册的账户\"]", "Enter")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc52&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click #content-wrap div div div div
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?&id=5fd22947af9564c76a30dc52&activeKey=info"):
    with page.expect_navigation():
        page.click("#content-wrap div div div div")

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="document"] button:has-text("加入课程")
    page.click("div[role=\"document\"] button:has-text(\"加入课程\")")

    # Go to https://momodel.cn/workspace/61efa18d67a87217644b8bcb/app
    page1.goto("https://momodel.cn/workspace/61efa18d67a87217644b8bcb/app")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
