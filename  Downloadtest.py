from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=数据集
    # with page.expect_navigation(url="https://momodel.cn/dataset?&p=1"):
    with page.expect_navigation():
        page.click("text=数据集")
    # assert page.url == "https://momodel.cn/dataset"

    # Click .index_contentImg-1-7tF
    page.click(".index_contentImg-1-7tF")
    # assert page.url == "https://momodel.cn/explore/5d411ace1afd9427c236eab5?type=dataset"

    # Click text=Momodel2021/03/03 1751 22添加到项目 >> :nth-match(i, 4)
    page.click("text=Momodel2021/03/03 1751 22添加到项目 >> :nth-match(i, 4)")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/explore/5d411ace1afd9427c236eab5?type=dataset"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=Momodel2021/03/03 1751 22添加到项目 >> :nth-match(i, 4)
    with page.expect_download() as download_info:
        page.click("text=Momodel2021/03/03 1751 22添加到项目 >> :nth-match(i, 4)")
    download = download_info.value

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
