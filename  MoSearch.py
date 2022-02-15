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

    # Click button:has-text("查找标签")
    page.click("button:has-text(\"查找标签\")")

    # Click text=卷积神经网络 / CNN
    page.click("text=卷积神经网络 / CNN")
    # assert page.url == "https://momodel.cn/explore?&tag=%E5%8D%B7%E7%A7%AF%E7%A5%9E%E7%BB%8F%E7%BD%91%E7%BB%9C%20/%20CNN&page=1"

    # Click .index_contentImg-2rj4G
    page.click(".index_contentImg-2rj4G")
    # assert page.url == "https://momodel.cn/explore/5bfb634e1afd943c623dd9cf?type=app"

    # Click text=图像风格迁移 - Style Transfer
    page.click("text=图像风格迁移 - Style Transfer")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
