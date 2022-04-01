# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-03-08
"""
import json
import unittest

import requests
import seldom
from seldom import file_data, data
from seldom.request import ResponseResult

from config.api_url import GLOBLE_URL
from utility.requests_interface import BaseRequest
# from utility.Request import MyRequest
# from utility.utility import res_check ,updateExcel
import xlrd,openpyxl,json

class EnableApi(BaseRequest):

    # @classmethod
    # def start_class(cls):
    #     # cls.token = request_info.TOKEN
    #     # cls.headers = request_info.HEADERS
    #     # cls.headers['Authorization'] = cls.token
    #     print(1)
    #     pass
    #
    # def start(self):
    #     print("一条测试开始执行")
    #
    # # @data([
    # #     ("/course/series", "get", 1, "12")
    # # ])
    @file_data(file="excel_api.xlsx", sheet="Sheet1", line=2)
    def test_status(self, url, method, _data, parameter, desc, expect, ispass,rel):
        """
        used file_data test
        """
        responses_list = []
        result_list = []

        if parameter:
            url = url+str(parameter)
        # print(GLOBLE_URL+url, method, _data, parameter, desc, expect, ispass)
        self.request(url=GLOBLE_URL+url, method=method, data=_data)
        # print(response.json())
        self.assertStatusCode(200)
        # responses_list.append(response.json())
        # res = res_check(response, expect)
        # for r in res_check:
        # if expect in response.json():
        #     pass
        # else:
        #     return 'fail'
        # return 'pass'

        # # print(rel.json())

        # if '通过' in res:
        #     result_list.append('通过')
        # else:
        #     result_list.append('失败')

        # updateExcel('api_test/test_data/excel_api.xlsx', result_list, responses_list)

        # self.assertEqual(self,expect,rel['response'])


if __name__ == '__main__':
    seldom.main()
