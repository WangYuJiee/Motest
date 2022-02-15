
from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
    # context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())

    # Go to http://192.168.30.154:8899/
    page.goto("http://192.168.30.154:8899/")

    # Click text=登录 / 注册
    page.click("text=登录 / 注册")
    # assert page.url == "http://192.168.30.154:8899/user/login?from=%2F"

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
    # with page.expect_navigation(url="http://192.168.30.154:8899/"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    context.storage_state(path='login_data.json')
    # Click button:has-text("立即绑定")
    with page.expect_popup() as popup_info:
        page.click("button:has-text(\"立即绑定\")")
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
