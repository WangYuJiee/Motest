from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context = browser.new_context(storage_state='login_data.json')

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click button:has-text("新建项目")
    page.click("button:has-text(\"新建项目\")")

    # Click div[role="tab"]:has-text("密码登录")
    # page.click("div[role=\"tab\"]:has-text(\"密码登录\")")
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

    # Click button:has-text("新建项目")
    page.click("button:has-text(\"新建项目\")")

    # Click div[role="document"] button:has-text("新建项目")
    # with page.expect_navigation(url="https://momodel.cn/workspace/61ea27f49fc15dfd2777d8b8/app"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("div[role=\"document\"] button:has-text(\"新建项目\")")
        page1 = popup_info.value

    # Click text=文件数据集模块任务部署目录NameLast Modifiedresults2 days ago_OVERVIEW.md2 days ago_README.ipy >> button
    page1.click("text=文件数据集模块任务部署目录NameLast Modifiedresults2 days ago_OVERVIEW.md2 days ago_README.ipy >> button")

    # Click #id-49abaa3e-a26f-4e39-8b33-a3f2a4dbe8a4 .jp-Launcher-body .jp-Launcher-content div:nth-child(2) .jp-Launcher-cardContainer .jp-LauncherCard .jp-LauncherCard-icon
    page1.click("#id-49abaa3e-a26f-4e39-8b33-a3f2a4dbe8a4 .jp-Launcher-body .jp-Launcher-content div:nth-child(2) .jp-Launcher-cardContainer .jp-LauncherCard .jp-LauncherCard-icon")

    # Click text=[ ]: ​ >> pre[role="presentation"]
    page1.click("text=[ ]: ​ >> pre[role=\"presentation\"]")

    # Fill text=[ ]: ​ >> textarea
    page1.fill("text=[ ]: ​ >> textarea", "123")

    # Click .mo-code-bar-item .iconfont
    page1.click(".mo-code-bar-item .iconfont")

    # Click #id-0b2f0a56-18a0-4055-952d-22cc878da70e .p-Widget.jp-Toolbar div:nth-child(7) .bp3-button
    page1.click("#id-0b2f0a56-18a0-4055-952d-22cc878da70e .p-Widget.jp-Toolbar div:nth-child(7) .bp3-button")

    # Click .p-Widget.jp-Toolbar.jp-MonacoPanel-toolbar div:nth-child(3) .bp3-button
    page1.click(".p-Widget.jp-Toolbar.jp-MonacoPanel-toolbar div:nth-child(3) .bp3-button")

    # Fill :nth-match(input[name="radiogroup"], 4)
    page1.fill(":nth-match(input[name=\"radiogroup\"], 4)", "gpu")

    # Click :nth-match(input[name="radiogroup"], 4)
    page1.click(":nth-match(input[name=\"radiogroup\"], 4)")

    # Click button:has-text("确定")
    page1.click("button:has-text(\"确定\")")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
