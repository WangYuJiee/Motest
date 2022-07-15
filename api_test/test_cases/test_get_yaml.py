import os
import sys
import unittest

from ddt import ddt, file_data
from seldom import file_data

from api_test.test_cases import BaseRequest

try:
    import yaml
except ImportError:  # pragma: no cover
    have_yaml_support = False
else:
    have_yaml_support = True

# A good-looking decorator
needs_yaml = unittest.skipUnless(
    have_yaml_support, "Need YAML to run this test"
)

# print '***获取上上级目录***'
parent_path = os.path.abspath(os.path.join(os.getcwd(), ".."))

# @ddt
# class TestYaml(BaseRequest):
    #
    # @file_data("info.yaml", key='login2')
    # def test_login(self, username, password):
    #     """a simple test case """
    #     print("\nu-->", username)
    #     print("p-->", password)
    #     # print(username, password, email, params)
    #     # print(username, password, email)
    # #
    # # #
    # @file_data("info.yaml", key='login3')
    # def test_file_data_yaml_dict_dict(self, start, end, value, ed):
    #     print(start, end, value, ed['username'], ed['login'])
    # #
    # 使用ddt的包
    # @needs_yaml
    # # @file_data(parent_path+'/test_data/test_data_dict_dict.yaml')
    # def test_file_data_yaml_dict_dict(self, start, end, value):
    #     print(start, end, value)
        # self.assertLess(start, end)
        # self.assertLess(value, end)
        # self.assertGreater(value, start)

    # @needs_yaml
    # @file_data('test_data/test_data_list.yaml')
    # def test_file_data_yaml_list(self, value):
    #     print(value)
