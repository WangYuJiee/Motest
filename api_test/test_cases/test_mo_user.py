import seldom
from seldom import file_data, data
from seldom.request import ResponseResult
import requests
from config.api_url import GLOBLE_URL
from utility.requests_interface import BaseRequest
from utility.utility import login, logout
from utility.JsbnRSA import JsbnRSA
import json


class test_mo_user(BaseRequest):
    @classmethod
    def start_class(cls):
        print("开始测试")
        # r= login("luxu99","111111")
        # Token  = r.json()['token']
        # print(Token)
        r = login("luxu99", "111111")
        global Token
        Token = r.json()['token']

    @classmethod
    def end_class(cls):
        print("结束测试")
        logout()

    @file_data("email_case_data.yaml", key="data")
    def test_case_send_verification_code_email(
            self, _, email, expectMessage, StatusCode):
        """注册/登录时, 发送验证码到邮箱"""
        url = '/user/send_verification_code_email/' + email
        self.get(url=GLOBLE_URL + url)
        assert_json = expectMessage
        self.assertJSON(assert_json)
        # self.assertPath("response",expectMessage)
        self.assertStatusCode(StatusCode)

    @file_data("phone_case_data.yaml", key="data")
    def test_send_verification_code_phone(
            self, _, phone, expectMessage, StatusCode):
        """给手机发送验证码"""
        url = '/user/send_verification_code/' + str(phone)
        self.get(url=GLOBLE_URL + url)
        assert_json = expectMessage
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    @file_data("username_case_data.yaml", key="data")
    def test_check_username_exist(
            self, _, username, expectMessage, StatusCode):
        """检查用户名是否已存在"""
        url = '/user/check_username_exist'
        self.get(url=GLOBLE_URL + url, params=username)
        assert_json = expectMessage
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    @file_data("email_case_data.yaml", key="data2")
    def test_check_email_exist(self, _, email, expectMessage, StatusCode):
        """注册时检查邮箱是否已存在"""
        url = '/user/check_email_exist'
        self.get(url=GLOBLE_URL + url, params=email)
        assert_json = expectMessage
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    @file_data("phone_case_data.yaml", key='data2')
    def test_check_phone_exist(self, _, phone, expectMessage, StatusCode):
        """注册时检查手机号是否已存在"""
        url = '/user/check_phone_exist'
        self.get(url=GLOBLE_URL + url, params=phone)
        assert_json = expectMessage
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    @file_data("email_case_data.yaml", key='data3')
    def test_check_email_belong_user(
            self, _, email, expectMessage, StatusCode):
        """检查邮箱是否属于用户"""
        url = '/user/check_email_belong_user'
        self.post(
            url=GLOBLE_URL +
            url,
            json=email,
            headers={
                "Authorization": "Bearer " +
                Token})
        assert_json = expectMessage
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    @file_data("username_case_data.yaml", key='data1')
    def test_login(self, _, username, pwd, expect_message, StatusCode):
        """用户账号(用户名 / 邮箱 / 手机号)密码登录"""
        session = requests.session()
        r = session.get(GLOBLE_URL + '/user/session_login')
        cookie = next(
            (cookie for cookie in r.cookies
             if cookie.name == 'public_key'), None
        )
        if not cookie:
            raise ValueError('error cookie')
        public_key = cookie.value
        public_key = json.loads(public_key)
        public_key = public_key.strip('"').replace('\\n', '\n')
        password = JsbnRSA(public_key, is_public=True).encrypt(pwd)

        body = {
            "username": username,
            "password": password
        }
        headers = {
            'X-From': 'oooo.com',
            'X-Language': 'zh-CN'
        }
        # result = session.post(GLOBLE_URL + '/user/login', json=body, headers={
        #     'X-From': 'oooo.com',
        #     'X-Language': 'zh-CN'
        # })
        url = '/user/login'
        self.post(
            GLOBLE_URL + url,
            json=body,
            headers=headers,
            cookies=r.cookies)
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(StatusCode)

    def test_session_login(self):
        """设置session和cookie"""
        url = '/user/session_login'
        self.get(url=GLOBLE_URL + url)
        assert_json = {"response": "session login success"}
        self.assertJSON(assert_json)
        self.assertStatusCode(200)
    #
    # # 用户注册
    # def test_register(self, _,username,password,email):
    #     url = '/user/register'
    #     body = {
    #         "username": username,
    #         "password": password,
    #         "email": email,
    #     }
    #     self.post(url=GLOBLE_URL+url,json=body)
    #     requests.delete(GLOBLE_URL + f'/git/{user_ID}/delete_user_path')
    #
    #
    #
    #


if __name__ == '__main__':
    seldom.main(debug=True)
