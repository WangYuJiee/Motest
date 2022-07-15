# -*- coding: utf-8 -*-#
"""
    @Name: test_mo_cource
    @Author:  49173
    @Date:  2022-04-06
    @Description:
"""
import seldom
from seldom import file_data, skip, skip_if
from api_test.test_cases import BaseRequest
from config.api_url import GLOBLE_URL
from utility.local_storage import local_data
from utility.utility import requires_auth, logout


class MoCourseTest(BaseRequest):
    """Course Test"""

    def __init__(self, *args, **kwargs):
        super(MoCourseTest, self).__init__(*args, **kwargs)
        self.__token = None
        # 存变量

    @requires_auth()
    def start_class(self):
        print("开始测试")
        global Token
        # Token = r.json()['token']
        Token = local_data.__getattr__("token")
    # @requires_auth()
    # def init_auth(self):
    #     self.__token = local_data.__getattr__("token")
    #     print("token: ", self.__token)

    def end_class(self):
        print("结束测试")
        # 登录闭环
        # print("token: ", self.__token)
        logout()

    @file_data("course_case_data.yaml", key="data")
    def test_get_course(self, _, params, expect_message, status_code):
        """个人课程/所有课程"""

        url = GLOBLE_URL + "/course"
        # 获取本地变量
        self.get_data(url=url, params=params, headers={
            "Authorization": "Bearer " + Token})
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)


    @skip_if(local_data.__getattr__("token"), "login error")
    @file_data("course_case_data.yaml", key="data2")
    def test_get_series(self, _, assert_json, status_code):
        """学习路径的系列课程"""
        url = GLOBLE_URL + "/course/series"
        # 获取本地变量
        self.get_data(url=url)
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data3")
    def test_get_individual(self, _, expect_message, status_code):
        """我的课程"""
        url = GLOBLE_URL + "/course/individual"
        self.get(url=url, headers={
            "Authorization": "Bearer " + Token
        })
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data4")
    def test_get_comment(self, _, params, assert_json, status_code):
        """个人课程评分"""
        url = GLOBLE_URL + "/course/comment/"
        self.get(url=url + params, headers={"Authorization": "Bearer " + Token})
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("course_case_data.yaml", key="data5")
    def test_get_rating(self, _, params, status_code):
        """课程评分"""
        url = GLOBLE_URL + "/course/rating/"
        self.get(url=url + params)
        Schema = {
            "response": {
                "course_avg_rate": {"type":int},
                "total_count":  {"type":int}
            }
        }
        self.assertSchema(Schema)
        self.assertStatusCode(status_code)


    # def test_post_rating(self, _, params, status_code):
    #     """对参加的课程评分"""
    #     url = GLOBLE_URL + "/course/rating/"
    #     self.post(url=url + params)
    #     Schema = {
    #         "response": {
    #             "course_avg_rate": {"type":int},
    #             "total_count": {"type":int}
    #         }
    #     }
    #     self.assertSchema(Schema)
    #     self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data6")
    def test_get_status(self, _, params, status_code):
        """课程状态 加入人数,完成人数"""
        url = GLOBLE_URL + '/course/status'
        self.get(url=url ,params=params)
        Schema = {
            "response": {
                str: {
                    "name": {"type":str},
                    "zh_name": {"type":str},
                    "status": None,
                    "learn_num": {"type":int},
                    "finish_num": {"type":int}
                }
            }
        }
        self.assertSchema(Schema)
        self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data8")
    def test_get_tree(self, _, courseid, assert_json, status_code):
        """课程总览信息"""
        url = GLOBLE_URL + '/course/tree/' + courseid
        self.get(url=url,headers={"Authorization": "Bearer " + Token})
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data9")
    def test_get_grade(self, _, courseid, assert_json, status_code):
        """课程成绩信息"""
        url = GLOBLE_URL + '/course/grade/' + courseid
        self.get(url=url,headers={"Authorization": "Bearer " + Token})
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)


    @file_data("course_case_data.yaml", key="data10")
    def test_post_enroll(self, _, courseid, assert_json, status_code):
        """学习课程"""
        url = GLOBLE_URL + "/course/enroll"
        self.post(url,json=courseid,headers={"Authorization": "Bearer " + Token})
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("course_case_data.yaml", key="data11")
    def test_post_course(self, _, params, assert_json, status_code):
        """获取或创建课程项目"""
        url = GLOBLE_URL + "/project/course"
        self.post(url,json=params,headers={"Authorization": "Bearer " + Token})
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)






if __name__ == '__main__':
    seldom.main(debug=True)
