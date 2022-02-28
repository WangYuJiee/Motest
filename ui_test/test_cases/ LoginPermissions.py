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

    # Click text=体验课官方课程学习路径 >> img
    page.click("text=体验课官方课程学习路径 >> img")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=61c7ddff221233b41caedca6&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Click [aria-label="Close"]
    page.click("[aria-label=\"Close\"]")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=61c7ddff221233b41caedca6&activeKey=info"

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case2():
    print('test2 start')

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click button:has-text("新建项目")
    page.click("button:has-text(\"新建项目\")")

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

    # Click text=数据集
    # with page.expect_navigation(url="https://momodel.cn/dataset?&p=1"):
    with page.expect_navigation():
        page.click("text=数据集")
    # assert page.url == "https://momodel.cn/dataset"

    # Click button:has-text("新建数据集")
    page.click("button:has-text(\"新建数据集\")")

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

    # Click text=讨论
    page.click("text=讨论")
    # assert page.url == "https://momodel.cn/discussion"

    # Click button:has-text("发布话题")
    page.click("button:has-text(\"发布话题\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case5():
    print('test5 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click text=体验课官方课程学习路径 >> :nth-match(img, 2)
    page.click("text=体验课官方课程学习路径 >> :nth-match(img, 2)")

    # Click button:has-text("不会 Python")
    page.click("button:has-text(\"不会 Python\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case6():
    print('test6 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click #Button-chat
    page.click("#Button-chat")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case7():
    print('test7 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click span:has-text("yangsaisai")
    with page.expect_popup() as popup_info:
        page.click("span:has-text(\"yangsaisai\")")
    page1 = popup_info.value

    # Click button:has-text("发送消息")
    page1.click("button:has-text(\"发送消息\")")

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case8():
    print('test8 start')
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

    # Click a:nth-child(2) .index_content-1Xrgi .index_contentImg-1-7tF
    page.click("a:nth-child(2) .index_content-1Xrgi .index_contentImg-1-7tF")
    # assert page.url == "https://momodel.cn/explore/5efc77dbc018c95e69fb2a81?type=dataset"

    # Click button:has-text("添加到项目")
    page.click("button:has-text(\"添加到项目\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case9():
    print('test9 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=项目
    page.click("text=项目")
    # assert page.url == "https://momodel.cn/explore"

    # Click a:nth-child(2) .index_content-3VvHd .index_contentImg-2rj4G
    page.click("a:nth-child(2) .index_content-3VvHd .index_contentImg-2rj4G")
    # assert page.url == "https://momodel.cn/explore/5bfb634e1afd943c623dd9cf?type=app"

    # Click button:has-text("Fork")
    page.click("button:has-text(\"Fork\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case10():
    print('test10 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=课程
    page.click("text=课程")
    # assert page.url == "https://momodel.cn/classroom"

    # Click #py a div:has-text("Mo-Tutor")
    page.click("#py a div:has-text(\"Mo-Tutor\")")
    # assert page.url == "https://momodel.cn/classroom/course/detail?id=60f02c635076ff487bce4c6f&activeKey=info"

    # Click text=加入课程
    page.click("text=加入课程")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

def case11():
    print('test11 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=立即体验
    with page.expect_popup() as popup_info:
        page.click("text=立即体验")
    page1 = popup_info.value

    # Click span:has-text("开始学习")
    with page.expect_popup() as popup_info:
        page1.click("span:has-text(\"开始学习\")")
    page2 = popup_info.value



    # Click text=2 做计算
    page2.click("text=2 做计算")

    # Click text=编程题 1
    page2.click("text=编程题 1")

    # Click button:has-text("是")
    page2.click("button:has-text(\"是\")")
    # assert page2.url == "https://momodel.cn/workspace/61ea757c9fc15dfd2777d8fe/app/classic?sectionIdx=0&chapterIdx=0&unitIdx=0&isTrial=true&unlockCourseId=60f02c635076ff487bce4c6f"

    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


def case12():
    print('test12 start')
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://momodel.cn/
    page.goto("https://momodel.cn/")

    # Click text=讨论
    page.click("text=讨论")
    # assert page.url == "https://momodel.cn/discussion"

    # Click text=姓名：Mo（读音同“莫”） 个人主页（网址）：momodel.cn（暂不适配IE浏览器，敬请谅解。） 性别：女 生日：2018.12.12 星座：射手 邮箱：s
    page.click("text=姓名：Mo（读音同“莫”） 个人主页（网址）：momodel.cn（暂不适配IE浏览器，敬请谅解。） 性别：女 生日：2018.12.12 星座：射手 邮箱：s")
    # assert page.url == "https://momodel.cn/discussion/5c36f4461afd94734e342fbe?type=app"

    # Click button:has-text("评论")
    page.click("button:has-text(\"评论\")")

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    case1()
    case2()
    case3()
    case4()
    case5()
    case6()
    case7()
    case8()
    case9()
    case10()
    case11()
    case12()