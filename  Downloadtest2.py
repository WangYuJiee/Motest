from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(accept_downloads=True)

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click text=yangsaisai10个月前
    page.click("text=yangsaisai10个月前")
    # assert page.url == "https://momodel.cn/explore/5bfd118f1afd942b66b36b30?type=app"

    # Click text=项目 25 2021/04/02yangsaisaiFork >> :nth-match(i, 3)
    page.click("text=项目 25 2021/04/02yangsaisaiFork >> :nth-match(i, 3)")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "lu xu 99")

    # Press CapsLock
    page.press("[placeholder=\"请输入已注册的账户\"]", "CapsLock")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/explore/5bfd118f1afd942b66b36b30?type=app"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=项目 25 2021/04/02yangsaisaiFork >> :nth-match(i, 3)
    with page.expect_download() as download_info:
        page.click("text=项目 25 2021/04/02yangsaisaiFork >> :nth-match(i, 3)")
    download = download_info.value

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
