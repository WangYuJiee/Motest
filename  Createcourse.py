from playwright.sync_api import Playwright, sync_playwright


def case1():
    print('test1 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=Python 基础Python 系列
    page.click("text=Python 基础Python 系列")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=5fd22ac1af9564c826c0c23f&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="tab"]:has-text("密码登录")
    page.click("div[role=\"tab\"]:has-text(\"密码登录\")")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Press Enter
    page.press("[placeholder=\"请输入已注册的账户\"]", "Enter")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=5fd22ac1af9564c826c0c23f&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")


    # Click text=继续学习
    # with page.expect_navigation(url="https://momodel.cn/workspace/61ef96a067a87217644b8bb6/app"):
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            try:
                page.click("text=加入课程")
                page.click("div[role=\"document\"] button:has-text(\"加入课程\")")
            except:
                page.click("text=继续学习")
        page1 = popup_info.value

    # Click li[role="treeitem"] >> text=Python 基础数据类型
    page1.once("dialog", lambda dialog: dialog.dismiss())
    page1.click("li[role=\"treeitem\"] >> text=Python 基础数据类型")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case2():
    print('test2 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='login_data.json')


    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=Python 进阶
    page.click("text=Python 进阶")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc3e&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    # page.click("text=密码登录")
    #
    # # Click [placeholder="请输入已注册的账户"]
    # page.click("[placeholder=\"请输入已注册的账户\"]")
    #
    # # Fill [placeholder="请输入已注册的账户"]
    # page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu")
    #
    # # Press Enter
    # page.press("[placeholder=\"请输入已注册的账户\"]", "Enter")
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
    # # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=5fd22947af9564c76a30dc3e&activeKey=info"):
    # with page.expect_navigation():
    #     page.click("button:has-text(\"登录\")")

    # Click text=免费加入课程
    page.click("text=免费加入课程")

    # Click div[role="document"] button:has-text("加入课程")
    with page.expect_popup() as popup_info:
        page.click("div[role=\"document\"] button:has-text(\"加入课程\")")
    page1 = popup_info.value


    # Go to https://momodel.cn/workspace/61ef98e567a87217644b8bbf/app
    page1.goto("https://momodel.cn/workspace/61ef98e567a87217644b8bbf/app")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case3():
    print('test3 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=Python 图形可视化基础Python 系列
    page.click("text=Python 图形可视化基础Python 系列")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=60eb9ee5bb3e92c927af38ee&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Press Enter
    page.press("[placeholder=\"请输入已注册的账户\"]", "Enter")

    # Click [placeholder="请输入密码"]
    page.click("[placeholder=\"请输入密码\"]")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=60eb9ee5bb3e92c927af38ee&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=加入课程
    page.click("text=加入课程")

    # Click div[role="document"] button:has-text("加入课程")
    with page.expect_popup() as popup_info:
        page.click("div[role=\"document\"] button:has-text(\"加入课程\")")
    page1 = popup_info.value


    # Go to https://momodel.cn/workspace/61ef993667a87217644b8bc2/app
    page1.goto("https://momodel.cn/workspace/61ef993667a87217644b8bc2/app")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case4():
    print('test4 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=Python 图形可视化进阶Python 系列
    page.click("text=Python 图形可视化进阶Python 系列")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af3907&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click text=密码登录
    page.click("text=密码登录")

    # Click [placeholder="请输入已注册的账户"]
    page.click("[placeholder=\"请输入已注册的账户\"]")

    # Fill [placeholder="请输入已注册的账户"]
    page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu99")

    # Press Enter
    page.press("[placeholder=\"请输入已注册的账户\"]", "Enter")

    # Press Tab
    page.press("[placeholder=\"请输入已注册的账户\"]", "Tab")

    # Press CapsLock
    page.press("[placeholder=\"请输入密码\"]", "CapsLock")

    # Fill [placeholder="请输入密码"]
    page.fill("[placeholder=\"请输入密码\"]", "123456")

    # Click button:has-text("登录")
    # with page.expect_navigation(url="https://momodel.cn/classroom/course/detail?id=60eb9ee6bb3e92c927af3907&activeKey=info"):
    with page.expect_navigation():
        page.click("button:has-text(\"登录\")")

    # Click text=加入课程
    page.click("text=加入课程")

    with page.expect_popup() as popup_info:
        page.click("div[role=\"document\"] button:has-text(\"加入课程\")")
    page1 = popup_info.value

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    case1()
    case2()
    case3()
