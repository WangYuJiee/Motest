import seldom
from seldom import file_data, data
from seldom.request import ResponseResult
import requests
from config.api_url import GLOBLE_URL
from utility.local_storage import local_data
from utility.requests_interface import BaseRequest
from utility.utility import login, logout, requires_auth
from utility.JsbnRSA import JsbnRSA
import json


class MoUserTest(BaseRequest):

    def __init__(self, *args, **kwargs):
        super(MoUserTest, self).__init__(*args, **kwargs)
        self._token = None

    @requires_auth()
    def start_class(self):
        print("开始测试")
        # global Token
        # Token = r.json()['token']
        self._token = local_data.__getattr__("token")

    @classmethod
    def end_class(cls):
        print("结束测试")
        logout()

    @file_data("email_case_data.yaml", key="data")
    def test_case_send_verification_code_email(
            self, _, email, expect_message, status_code):
        """注册/登录时, 发送验证码到邮箱"""
        url = '/user/send_verification_code_email/' + email
        self.get(url=GLOBLE_URL + url)
        assert_json = expect_message
        self.assertJSON(assert_json)
        # self.assertPath("response",expect_message)
        self.assertStatusCode(status_code)

    @file_data("phone_case_data.yaml", key="data")
    def test_send_verification_code_phone(
            self, _, phone, expect_message, status_code):
        """给手机发送验证码"""
        url = '/user/send_verification_code/' + str(phone)
        self.get(url=GLOBLE_URL + url)
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("username_case_data.yaml", key="data")
    def test_check_username_exist(
            self, _, username, expect_message, status_code):
        """检查用户名是否已存在"""
        url = '/user/check_username_exist'
        self.get(url=GLOBLE_URL + url, params=username)
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("email_case_data.yaml", key="data2")
    def test_check_email_exist(self, _, email, expect_message, status_code):
        """注册时检查邮箱是否已存在"""
        url = '/user/check_email_exist'
        self.get(url=GLOBLE_URL + url, params=email)
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("phone_case_data.yaml", key='data2')
    def test_check_phone_exist(self, _, phone, expect_message, status_code):
        """注册时检查手机号是否已存在"""
        url = '/user/check_phone_exist'
        self.get(url=GLOBLE_URL + url, params=phone)
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("email_case_data.yaml", key='data3')
    def test_check_email_belong_user(
            self, _, email, expect_message, status_code):
        """检查邮箱是否属于用户"""
        url = '/user/check_email_belong_user'
        self.post(
            url=GLOBLE_URL +
            url,
            json=email,
            headers={
                "Authorization": "Bearer " +
                                 self._token})
        assert_json = expect_message
        self.assertJSON(assert_json)
        self.assertStatusCode(status_code)

    @file_data("username_case_data.yaml", key='data1')
    def test_login(self, _, username, pwd, expect_message, status_code):
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
        self.assertStatusCode(status_code)

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
    def test_temp_user(self, ):
        """临时用户账号登录"""
        url = "/user/temp_user"
        self.put(url)

    def test_login_or_register_phone(self):
        """手机号登录或注册"""
        url = "/user/login_or_register_phone"
        self.post()

    def test_login_with_phone(self):
        """手机号登录"""
        url = "/user/login_with_phone"
        self.post()

    def test_register_with_phone(self):
        """手机号注册"""
        url = "/user/register_with_phone"
        self.post()

    def test_login_or_register_email(self):
        """邮箱登录或注册"""

        url = "/user/login_or_register_email"
        self.post()

    def test_login_with_email(self):
        """邮箱登录"""
        url = "/user/login_with_email"
        self.post()

    def test_register_with_email(self):
        """邮箱注册"""
        url = "/user/register_with_email"
        self.post()

    def test_verify_code_phone(self):
        """验证手机验证码"""
        url = "/user/verify_code_phone"
        self.post()

    def test_reset_password_phone(self):
        """手机重置密码"""

        url = "/user/reset_password_phone"
        self.post()

    def test_verify_code_email(self):
        """验证邮箱验证码"""
        url = "/user/verify_code_email"
        self.post()

    def test_reset_password_email(self):
        """邮箱重置密码"""
        # new_password、new_check_password、email
        url = "/user/reset_password_email"
        self.post()


if __name__ == '__main__':
    seldom.main(debug=True)
