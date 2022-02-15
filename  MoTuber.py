from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='login_data.json')

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click #py >> :nth-match(div:has-text("Mo-Tutor"), 3)
    page.click("#py >> :nth-match(div:has-text(\"Mo-Tutor\"), 3)")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=6173911eab37f12b14daf4a8&activeKey=info"

    # # Click text=加入课程
    # page.click("text=加入课程")
    #
    # # Click text=密码登录
    # page.click("text=密码登录")
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
    # # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=6173911eab37f12b14daf4a8&activeKey=info"):
    # with page.expect_navigation():
    #     page.click("button:has-text(\"登录\")")

    # Click text=加入课程
    page.click("text=加入课程")

    # Click button:has-text("加入课程")
    # with page.expect_navigation(url="https://momodel.cn/overview/6173911eab37f12b14daf4a8"):
    with page.expect_navigation():
        page.click("button:has-text(\"加入课程\")")

    # Click button:has-text("立即学习")

    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("button:has-text(\"立即学习\")")
        page1 = popup_info.value


    # Click button:has-text("退出")
    page1.click("button:has-text(\"退出\")")

    # Click [aria-label="Close"]
    page1.click("[aria-label=\"Close\"]")

    # Click text=2 AI 之梦
    page1.click("text=2 AI 之梦")

    # Click text=选择题
    page1.click("text=选择题")
    # assert page1.url == "https://momodel.cn/workspace/61ea6c729fc15dfd2777d8f2/app/classic?chapterIdx=3&sectionIdx=1&unitIdx=0"

    # Click text=A、是 >> p
    page1.click("text=A、是 >> p")

    # Click button:has-text("下一题")
    page1.click("button:has-text(\"下一题\")")
    # assert page1.url == "https://momodel.cn/workspace/61ea6c729fc15dfd2777d8f2/app/classic?chapterIdx=3&sectionIdx=1&unitIdx=1"

    # Click text=机器学习包含了神经网络
    page1.click("text=机器学习包含了神经网络")

    # Click button:has-text("提交")
    page1.click("button:has-text(\"提交\")")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
