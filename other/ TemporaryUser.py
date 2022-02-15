from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click .moHomepage_slideLines-1X9Ez div:nth-child(3)
    page.click(".moHomepage_slideLines-1X9Ez div:nth-child(3)")

    # Click text=立即体验
    with page.expect_popup() as popup_info:
        page.click("text=立即体验")
    page1 = popup_info.value

    # Click text=开始学习
    with page.expect_popup() as popup_info:
        page1.click("text=开始学习")
    page2 = popup_info.value

    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
