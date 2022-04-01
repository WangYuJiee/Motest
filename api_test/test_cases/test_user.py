from datetime import datetime

import requests
import seldom
from seldom import file_data, data

from config import request_info
from db_data.redis_cache import redis_cache


class UserTest(seldom.TestCase):
    """ 用户信息 """

    @classmethod
    def start_class(cls):
        cls.token = redis_cache.get_redis_info('user:admin')
        cls.headers = request_info.HEADERS
        cls.headers['Authorization'] = cls.token
        cls.user_login = request_info.USERS

    def start(self):
        # print("\n一个测试用例开始")
        pass

    def end(self):
        # print("\n一个用例结束")
        pass

    # @seldom.skip()
    # @data([
    #     ('admin', 'admin', 200, 'success'),
    # ])
    # # @file_data("user_login.xlsx", sheet="Sheet1", line=2)
    # def test_user_login(self, username, password, status, msg):
    #     self.post(self.user_login + "/login_verify", json={"email": username, "password": password, "code": correct,
    #                                                        "phone_or_mail_verification": verification_encode},
    #               headers=self.headers)
    #     self.assertPath("status", int(status))
    #     self.assertPath("message", msg)

    # get users info
    @data([
        # (1, 10, '杭州市', 200),
        (1, 10, '嘉兴市', 200),
    ])
    # @file_data("users.xlsx", sheet="Sheet1", line=2)
    def test_user_get_lists(self, page_no, page_size, area, status):
        self.get(self.user_login + "/users", params={"page_no": page_no, "page_size": page_size, "area": area},
                 headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("message", "success")

    @data([
        (1, 10, '李思儒', 200),
        (1, 10, 'snow', 200),
    ])
    @file_data("users.xlsx", sheet="Sheet1", line=2)
    def test_user_search_by_name(self, page_no, page_size, uname, status):
        self.get(self.user_login, params={"page_no": page_no, "page_size": page_size, "display_name": uname},
                 headers=self.headers)
        self.assertStatusCode(200)
        self.assertPath("message", "success")


if __name__ == "__main__":
    seldom.main(base_url="http://192.168.30.58:8080", debug=True)
