# -*- coding: utf-8 -*-#
"""
    @Name: test_mo_cource
    @Author:  49173
    @Date:  2022-04-06
    @Description:
"""
from seldom import file_data
from seldom.request import ResponseResult


from config.api_url import GLOBLE_URL
from utility.local_storage import local_data
from utility.requests_interface import BaseRequest
from utility.utility import login_decorator, Token


class CourseTest(BaseRequest):
    """Course Test"""

    def test_get_course(self):
        """个人课程/所有课程"""

        pass

    @file_data("../test_data/course_case_data.yaml", key="course")
    @login_decorator()
    def test_get_series(self, _, params, status_code):
        """学习路径的系列课程"""
        url = "/course/series"
        # 获取本地变量
        token = local_data.__getattr__("token")
        self.get(url=GLOBLE_URL + url, params=params, headers={
            "Authorization": "Bearer " + token})
        ret = ResponseResult.response
        print("ret: ", str(ret))
        self.assertStatusCode(status_code)

    def test_get_individual(self):
        """我的课程"""
        pass

    def test_get_comment(self):
        """个人课程评分"""
        pass

    def test_get_rating(self):
        """课程评分"""
        pass

    def test_post_rating(self):
        """对参加的课程评分"""
        pass

    def test_get_status(self):
        """课程状态 加入人数,完成人数"""
        pass

    def test_post_status(self):
        """开始课程"""
        pass

    def test_get_tree(self):
        """课程总览信息"""
        pass

    def test_get_grade(self):
        """课程成绩信息"""

    def test_post_enroll(self):
        """学习课程"""
        pass
