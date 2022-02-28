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

    # Click text=Python 进阶Python 系列
    page.click("text=Python 进阶Python 系列")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc3e&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="tab"]:has-text("密码登录")
    page.click("div[role=\"tab\"]:has-text(\"密码登录\")")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "lū xu 99")

    # Press Tab
    page.press("[placeholder=\"请输入已注册的账户\"]", "Tab")

    # Double click [placeholder="请输入已注册的账户"]
    page.dblclick("[placeholder=\"请输入已注册的账户\"]")

    # Press CapsLock
    page.press("[placeholder=\"请输入已注册的账户\"]", "CapsLock")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "lū xu 99luxu99")

    # 4× click
    page.click("[placeholder=\"请输入已注册的账户\"]", click_count=4)

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc3e&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click #content-wrap div div div div
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?&id=5fd22947af9564c76a30dc3e&activeKey=info"):
    with page.expect_navigation():
        page.click("#content-wrap div div div div")

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="document"] button:has-text("加入课程")
    page.click("div[role=\"document\"] button:has-text(\"加入课程\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
