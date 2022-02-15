from playwright.sync_api import Playwright, sync_playwright
import random
import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://192.168.30.154:8899/
    page.goto("http://192.168.30.154:8899/")

    # Click text=登录 / 注册
    page.click("text=登录 / 注册")
    # assert page.url == "http://192.168.30.154:8899/user/login?from=%2F"

    # Click text=密码登录
    page.click("text=密码登录")

    # Click text=注册账号
    page.click("text=注册账号")
    # assert page.url == "http://192.168.30.154:8899/user/register?from=%2F"

    # Click [placeholder="请输入邮箱"]
    page.click("[placeholder=\"请输入邮箱\"]")

    # Fill [placeholder="请输入邮箱"]
    math = random.uniform(1, 10)
    page.fill("[placeholder=\"请输入邮箱\"]", str(math) + "@qq.com")
    time.sleep(3)

    # Click .index_header-28_eL
    page.click(".index_header-28_eL")

    # Click .index_header-28_eL
    page.click(".index_header-28_eL")

    # Click [placeholder="至少6位数字或字符"]
    page.click("[placeholder=\"至少6位数字或字符\"]")

    # Fill [placeholder="至少6位数字或字符"]
    page.fill("[placeholder=\"至少6位数字或字符\"]", "123456")

    # Click #re_password
    page.click("#re_password")

    # Fill #re_password
    page.fill("#re_password", "123456")

    # Click button:has-text("注册")
    # with page.expect_navigation(url="http://192.168.30.154:8899/launchpage"):
    with page.expect_navigation():
        page.click("button:has-text(\"注册\")")

    # Click button:has-text("暂不绑定")
    page.click("button:has-text(\"暂不绑定\")")

    # Click text=直接选课
    with page.expect_popup() as popup_info:
        page.click("text=直接选课")
    page1 = popup_info.value

    # Click button:has-text("会 Python 不会人工智能")
    page1.click("button:has-text(\"会 Python 不会人工智能\")")

    # Click button:has-text("退出")
    page1.click("button:has-text(\"退出\")")

    time.sleep(5)

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
