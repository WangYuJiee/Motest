from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=数据集
    # with page.expect_navigation(url="https://momodel.cn/dataset?&p=1"):
    with page.expect_navigation():
        page.click("text=数据集")
    # assert page.url == "https://momodel.cn/dataset"

    # Click [placeholder="搜索数据集"]
    page.click("[placeholder=\"搜索数据集\"]")

    # Fill [placeholder="搜索数据集"]
    # with page.expect_navigation(url="https://momodel.cn/dataset?&p=1&classification=all"):
    with page.expect_navigation():
        page.fill("[placeholder=\"搜索数据集\"]", "")

    # Press CapsLock
    page.press("[placeholder=\"搜索数据集\"]", "CapsLock")

    # Fill [placeholder="搜索数据集"]
    page.fill("[placeholder=\"搜索数据集\"]", "垃圾")

    # Click li[role="option"]:has-text("垃圾分类")
    page.click("li[role=\"option\"]:has-text(\"垃圾分类\")")
    # assert page.url == "https://momodel.cn/explore/6069143b1afd9438c4026345?type=dataset"

    # Click text=垃圾分类
    page.click("text=垃圾分类")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
