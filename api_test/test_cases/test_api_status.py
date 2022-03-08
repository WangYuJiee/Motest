# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-03-08
"""
import seldom
from seldom import file_data, data

from config.api_url import GROPLE_URL
from utility.requests_interface import BaseRequest


class EnableApi(BaseRequest):

    @classmethod
    def start_class(cls):
        # cls.token = request_info.TOKEN
        # cls.headers = request_info.HEADERS
        # cls.headers['Authorization'] = cls.token
        print(1)
        pass

    def start(self):
        print("一条测试开始执行")

    # @data([
    #     ("/course/series", "get", 1, "12")
    # ])
    @file_data(file="excel_api.xlsx", sheet="Sheet1", line=2)
    def test_excel(self, url, method, data, parameter, desc):
        """
        used file_data test
        """

        if parameter:
            url = url+str(parameter)
        print(GROPLE_URL+url, method, data, parameter, desc)
        self.request(url=url, method=method)


if __name__ == '__main__':
    seldom.main()
