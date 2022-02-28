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

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
