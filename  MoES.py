from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click text=标题, 作者, 描述 登录 / 注册公有云版En >> i
    page.click("text=标题, 作者, 描述 登录 / 注册公有云版En >> i")

    # Click input
    page.click("input")

    # Fill input
    page.fill("input", "python")

    # Click text=课程 (10) 最多展示3项
    page.click("text=课程 (10) 最多展示3项")
    # assert page.url == "https://momodel.cn/search?query=python&activeKey=courses"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
