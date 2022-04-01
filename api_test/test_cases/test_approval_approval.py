from datetime import timedelta
import seldom
from seldom import file_data, data, Seldom
from seldom.request import ResponseResult
from config import request_info
from config.api_url import APPROVAL
from config.log import LOG
from utility.requests_interface import BaseRequest
from utility.utility import get_this_time


class ApprovalTest(BaseRequest):
    """
    审批管理
    """

    @classmethod
    def start_class(cls):
        # cls.token = request_info.TOKEN
        # cls.headers = request_info.HEADERS
        # cls.headers['Authorization'] = cls.token
        cls.paaroval_url = APPROVAL

    @seldom.skip
    @data([
        (37, "my_request", 1, 10, 200),
        (4, "approval_record", 1, 10, 200),
    ])
    def test_get_approval(self, operator_id, approval_type, page_no, page_size, status):
        """

        """
        start_time = get_this_time(UTC_TIME=False) - timedelta(days=10)
        print(start_time)
        self.get_data(self.paaroval_url,
                      params={"operator_id": operator_id, "start_time": start_time,
                              "approval_type": approval_type, "page_no": page_no, "page_size": page_size})
        self.assertStatusCode(status)

    @seldom.skip
    @file_data("approval.json", key="approval")
    def test_get_approval(self, data):
        params = data
        self.get_data(self.paaroval_url, params=params)
        self.assertStatusCode(data['operator_id'])

    @file_data("approval.json", key="approval")
    def test_get_approval(self, data):
        """
            审批管理
        """
        params = data
        # from requests import request
        self.get_data(self.paaroval_url, params=params)
        # 断言
        print(ResponseResult.status_code)
        self.assertStatusCode(200)
        try:
            print("count: ", self.response['count'])
        except Exception as e:
            LOG.info('请求错误:%s' % e)


if __name__ == '__main__':
    seldom.main(base_url="http://192.168.30.58:8080", debug=True)
