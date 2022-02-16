# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-01-06
"""
import json
import os
import threading
import typing
from time import sleep
from concurrent.futures.thread import ThreadPoolExecutor

from loguru import logger
from playwright.sync_api import Playwright, BrowserType, BrowserContext, Page
from playwright.sync_api import sync_playwright
from .my_stl import Stack


class Tls(threading.local):
    def __init__(self):
        self.playwright: Playwright = None
        self.browser: BrowserType = None
        self.context: BrowserContext = None
        self.page: Page = None


class Generator:
    tls = Tls()

    def __init__(self):
        self.url_visit_list: typing.Set[str] = set()  # 标记保存浏览过的url
        self.url_stack: Stack = Stack()  # 当前收集到的url（未浏览）
        self.storage = None

    def run(self, k=1):
        logger.info(f"THREAD: {k} - ENTER")

        # storage_state = json.loads(os.environ["STORAGE"])
        # print(self.storage)
        self.tls.playwright = sync_playwright().start()
        self.tls.browser = self.tls.playwright.chromium.launch(headless=True)
        self.tls.context = self.tls.browser.new_context(
            bypass_csp=True,
            ignore_https_errors=True,
            # color_scheme=random.choice(["dark", "light", "no-preference"]),
            timezone_id=None,
            geolocation={"longitude": 1, "latitude": 2},
            locale="zh-CN",
            java_script_enabled=True,
            storage_state=self.storage,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
        )
        self.tls.page = self.tls.context.new_page()
        base_url = "https://momodel.cn/"
        try:

            # self.tls.context.add_cookies(self.storage['cookies'])
            # print(self.storage['cookies'])
            self.mo_page(base_url, k)
        except Exception as e:
            logger.info(f"THREAD: {k} - Exception {e}")
        finally:
            print(len(self.url_visit_list))
            self.tls.context.close()
            self.tls.browser.close()
            self.tls.playwright.stop()
            ps = self.tls.context.pages
            ps.clear()
            logger.info(f"THREAD: {k} - finally cls")

    def mo_page(self, url, k=1):

        # logger.info(f"THREAD: {k} - ENTER PAGE")
        #
        # logger.info(f"THREAD: - {url}")
        self.url_visit_list.add(url)
        page = self.tls.page
        page.set_default_timeout(30000)
        # page.goto("https://momodel.cn/")
        page.goto(url)

        # 在这里判断元素

        # assert page.url == "https://momodel.cn/"
        # page.screenshot(path=f'{111}.png')

        # 页面
        # get页面的所有url
        urls = set()
        urls.union(self.get_url(page, urls))
        if url == 'https://momodel.cn/classroom':
            page.screenshot(path=f'classroom.png')

            # Click text=体验课官方课程学习路径 >> i  //*[@id="trial_course_box"]/div[2]/div/div/span/span/span/span[1]/i
            page.click("text=体验课官方课程学习路径 >> i")
            # Click text=社群课程
            page.click("text=社群课程")
            # assert page.url == "https://momodel.cn/classroom?&p=1&tab=community"
            # Click text=社群课程官方课程社群课程实战练习其他课程活动 >> :nth-match(span, 4)
            urls.union(self.get_url(page, urls))
            page.click("text=社群课程官方课程社群课程实战练习其他课程活动 >> :nth-match(span, 4)")
            # Click text=实战练习
            page.click("text=实战练习")
            urls.union(self.get_url(page, urls))
            # assert page.url == "https://momodel.cn/classroom?&p=1&tab=practice"
            # Click text=实战练习官方课程社群课程实战练习其他课程活动 >> i
            page.click("text=实战练习官方课程社群课程实战练习其他课程活动 >> i")
            # Click text=其他课程
            page.click("text=其他课程")
            urls.union(self.get_url(page, urls))
            # assert page.url == "https://momodel.cn/classroom?&p=1&tab=others"
            # Click text=其他课程官方课程社群课程实战练习其他课程活动 >> i
            page.click("text=其他课程官方课程社群课程实战练习其他课程活动 >> i")
            # Click text=活动
            page.click("text=活动")
            urls.union(self.get_url(page, urls))
        # print(len(urls))

        # 查询url是否浏览过
        if len(urls) > 0:
            for item in urls:
                _repeat = False
                for i in self.url_visit_list:
                    if i == item:
                        _repeat = True
                if not _repeat and not self.url_stack.find(item):
                    self.url_stack.push(item)
        # 遍历 栈
        if self.url_stack.is_empty():
            # 递归出口
            logger.info(f"THREAD: {k} - EXIT")
            return
        else:
            url = self.url_stack.pop()
            self.mo_page(url)

    def find_value(self, lists, item):
        """

        :param lists:
        :param item:
        :return:
        """
        for t in lists:
            if t in item:
                return True
        return False

    def get_url(self, page, urls: set):
        """
        获取页面url
        :param urls:
        :param page:
        :return:
        """


        all_items = page.query_selector_all('a')
        for item in all_items:
            # 获取每个url的时候，可以存一个url结构（url,相关内容，比如一个map）
            # 判断元素 示例
            # book = {}
            # name_el = item.query_selector('h3')
            # book['name'] = name_el.inner_text()
            # price_el = item.query_selector('.price_color')
            # book['price'] = price_el.inner_text()
            # stock_el = item.query_selector('.availability')
            # book['stock'] = stock_el.inner_text()
            # books.append(book)
            # item.get_attribute()
            cell: str = str(item.get_property('href'))
            # 去除页面的footer，login等页面跳转链接
            pass_url = ['docs', 'login', 'logout', 'aboutus', 'status', 'article', 'about', 'profile']
            if 'momodel.cn' in cell and not self.find_value(pass_url, cell):
                urls.add(cell)
        return urls

    def login_state(self):
        """
        登录
        :return:
        """
        # page = self.tls.page
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch(headless=True)
            context = browser.new_context()
            page = context.new_page()

            # Go to https://momodel.cn/
            page.goto("https://momodel.cn/")
            # Click text=登录 / 注册
            page.click("text=登录 / 注册")
            # assert page.url == "https://momodel.cn/user/login?from=%2F"
            # Click text=密码登录
            page.click("text=密码登录")
            # Click [placeholder="请输入已注册的账户"]
            page.click("[placeholder=\"请输入已注册的账户\"]")
            # Fill [placeholder="请输入已注册的账户"]
            page.fill("[placeholder=\"请输入已注册的账户\"]", "luxu919")
            # Click [placeholder="请输入密码"]
            page.click("[placeholder=\"请输入密码\"]")
            # Fill [placeholder="请输入密码"]
            page.fill("[placeholder=\"请输入密码\"]", "123456")
            # Click button:has-text("登录")
            # with page.expect_navigation(url="https://momodel.cn/"):
            with page.expect_navigation():
                page.click("button:has-text(\"登录\")")
            # ---------------------
            self.storage = context.storage_state()
            # context.storage_state(path='login_data.json')
            # os.environ["STORAGE"] = json.dumps(self.storage)
            # print(self.storage)


if __name__ == "__main__":
    generators = list()
    tpe = ThreadPoolExecutor(2)
    for i in range(1, 2):
        generator = Generator()
        generators.append(generator)
        tpe.submit(generator.run, i)
        sleep(0.1)
    tpe.shutdown(wait=False)

    while sum([int(t.is_alive()) for t in tpe._threads]) > 1:
        sleep(3)

    generator = Generator()
    generator.login_state()

    # print(storage_state)
    generator.run()
    # pass_url = ['docs', 'login', 'logout', 'aboutus', 'status', 'article', 'about', 'profile']
    # tt = 'https://momodel.cn/logout'
    # t = generator.find_value(pass_url, tt)
    # print(t)
    pass
