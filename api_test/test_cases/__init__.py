# -*- coding: utf-8 -*-
"""
    @Author: 49173
    date: 2022-03-02
"""
import requests
import seldom
from config.log import LOG


class BaseRequest(seldom.TestCase):

    def __init__(self, *args, **kwargs):
        super(BaseRequest, self).__init__(*args, **kwargs)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/91.0.4472.124 Safari/537.36"}

    def get_data(self, url, params=None, headers=None, **kwargs):  # get消息
        try:
            if headers is None:
                h = self.headers
            else:
                h = headers
            return self.get(url=url, params=params, headers=h, **kwargs)
        except Exception as e:
            LOG.error('get请求出错，出错原因:%s' % e)
            print('get请求出错,出错原因:%s' % e)
            return {}
        finally:
            # self.assertStatusCode()
            pass

    def post_data(self, url, params, headers=None, **kwargs):  # post消息
        # data = json.dumps(params)
        data = params
        try:
            if headers is None:
                h = self.headers
            else:
                h = headers
            self.post(url=url, json=data, headers=h, **kwargs)
            # json_response = json.loads(self.response)
            json_response = self.response
            return json_response
        except Exception as e:
            LOG.error('post请求出错，出错原因:%s' % e)
            print('post请求出错,原因:%s' % e)
        finally:
            pass

    def del_data(self, url, params, headers=None, **kwargs):  # 删除的请求
        try:
            if headers is None:
                h = self.headers
            else:
                h = headers
            self.delete(url=url, params=params, headers=h, **kwargs)
            # json_response = json.loads(self.response)
            json_response = self.response
            return json_response
        except Exception as e:
            LOG.error('del请求出错，出错原因:%s' % e)
            print('del请求出错,原因:%s' % e)
            return {}
        finally:
            pass

    def put_data(self, url, params=None, json=None, headers=None, **kwargs):  # put请求
        try:
            if headers is None:
                h = self.headers
            else:
                h = headers
            # data = json.dumps(params)
            # data = params
            self.put(url=url, params=params, json=json, headers=h, **kwargs)
            # json_response = json.loads(self.response)
            json_response = self.response
            return json_response
        except Exception as e:
            LOG.error('put请求出错，出错原因:%s' % e)
            print('put请求出错,原因:%s' % e)
            return {}
        finally:
            pass

    @classmethod
    def request_data(cls, method, url, params=None, json=None, **kwargs):
        try:
            data = params
            res = requests.request(method, url, params=data, json=json, **kwargs)
            json_response = res
            return json_response
        except Exception as e:
            LOG.error('put请求出错，出错原因:%s' % e)
            print('put请求出错,原因:%s' % e)
            return {}
        finally:
            pass
