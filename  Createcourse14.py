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

    # Click text=自然语言处理：词嵌入
    page.click("text=自然语言处理：词嵌入")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af39b7&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "lu")

    # Press CapsLock
    page.press("[placeholder=\"请输入已注册的账户\"]", "CapsLock")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Click .ant-form div:nth-child(2) .ant-col .ant-form-item-control .ant-form-item-children .index_formItemMessage-M-3BU
    page.click(".ant-form div:nth-child(2) .ant-col .ant-form-item-control .ant-form-item-children .index_formItemMessage-M-3BU")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af39b7&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="document"] button:has-text("加入课程")
    # with page.expect_navigation(url="https://momodel.cn/workspace/61efa97467a87217644b8bfe/app"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("div[role=\"document\"] button:has-text(\"加入课程\")")
        page1 = popup_info.value

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
