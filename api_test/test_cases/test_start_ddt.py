import seldom


class TestCase(seldom.TestCase):
    bb = 55

    @classmethod
    def start_class(cls):
        cls.a = 12
        print("测试类开始执行", cls.a, cls.bb)

    # @classmethod
    # def setUp(cls):
    #     cls.bb = 88
    #     print("setup一条测试开始执行", cls.a, cls.bb)

    @classmethod
    def end_class(cls):
        print("测试类结束执行", cls.a, cls.bb)

    def start(self):
        self.a = 33
        self.bb = 66
        print("一条测试开始执行", self.a, self.bb)

    def end(self):
        print("一条测试结果")

    def test_search_seldom(self):
        # self.open("https://www.baidu.com")
        # self.type_enter(id_="kw", text="seldom")
        print("test001")

    def test_search_poium(self):
        # self.open("https://www.baidu.com")
        # self.type_enter(id_="kw", text="poium")
        print("test002")


if __name__ == "__main__":
    seldom.main(base_url="http://192.168.30.58:8080", debug=True)
