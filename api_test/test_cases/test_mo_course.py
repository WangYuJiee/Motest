# -*- coding: utf-8 -*-#
"""
    @Name: test_mo_cource
    @Author:  49173
    @Date:  2022-04-06
    @Description:
"""
import seldom
from seldom import file_data, skip, skip_if
from seldom.request import ResponseResult
from config.api_url import GLOBLE_URL
from utility.local_storage import local_data
from utility.requests_interface import BaseRequest
from utility.utility import requires_auth


class MoCourseTest(BaseRequest):
    """Course Test"""

    def __init__(self, *args, **kwargs):
        super(MoCourseTest, self).__init__(*args, **kwargs)
        self._token = None

    @requires_auth()
    def start_class(self):
        print("开始测试")
        self._token = local_data.__getattr__("token")

    @file_data("../test_data/course_case_data.yaml", key="course")
    def test_get_course(self, _, params, status_code):
        """个人课程/所有课程"""

        url = "/course"
        # 获取本地变量
        token = self._token
        self.get(url=GLOBLE_URL + url, params=params, headers={
            "Authorization": "Bearer " + token})
        ret = ResponseResult.response
        # print("ret: ", str(ret))
        self.assertStatusCode(status_code)

    # @skip_if(local_data.__getattr__("token"), "login error")
    @file_data("../test_data/course_case_data.yaml", key="series")
    def test_get_series(self, _, params, status_code):
        """学习路径的系列课程"""
        url = "/course/series"
        # 获取本地变量
        token = self._token
        self.get(url=GLOBLE_URL + url, params=params, headers={
            "Authorization": "Bearer " + token})
        ret = ResponseResult.response
        # print("ret: ", str(ret))
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

    course_ret = [
        {
            "course_id": "121212",
            "232": "334"
        },
        {
            "course_id": "343434"
        },
    ]

    # @skip()
    # @file_data("../test_data/course_case_data.yaml", key="status")
    # def test_post_status(self, _, params, status_code):
    #     """开始课程"""
    #     url = "/course/status"
    #     # 获取用户token
    #     token = self._token
    #
    #     # # 获取具体课程的course_id
    #     # self.get(url='', params='', headers={
    #     #     "Authorization": "Bearer " + token})
    #     # course_ret = ResponseResult.response
    #     # course_id = [course.get('course_id') for course in course_ret]
    #     # params.update({"course_id": course_id})
    #
    #     self.get(url=url, params=params, headers={
    #         "Authorization": "Bearer " + token})
    #     ret = ResponseResult.response
    #     print(ret)
    #     self.assertStatusCode(status_code)
    #
    #     pass

    def test_get_tree(self):
        """课程总览信息"""
        pass

    def test_get_grade(self):
        """课程成绩信息"""

    def test_post_enroll(self):
        """学习课程"""
        pass


if __name__ == '__main__':
    seldom.main(debug=True)
