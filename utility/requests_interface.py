# -*- coding: utf-8 -*-import unittestimport requestsimport seldomfrom seldom.request import requestfrom config.log import LOGclass BaseRequest(seldom.TestCase):    # def __init__(self):    #     super().__init__()    #     # self.headers = {    #     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "    #     #                   "Chrome/91.0.4472.124 Safari/537.36"}    headers = {        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "                      "Chrome/91.0.4472.124 Safari/537.36"}    def get_data(self, url, params=None, **kwargs):  # get消息        try:            return self.get(url, params=params, headers=self.headers, **kwargs)        except Exception as e:            LOG.info('get请求出错，出错原因:%s' % e)            print('get请求出错,出错原因:%s' % e)            return {}        finally:            # self.assertStatusCode()            pass    def post_data(self, url, params, **kwargs):  # post消息        # data = json.dumps(params)        data = params        try:            self.post(url, json=data, headers=self.headers, **kwargs)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('post请求出错，出错原因:%s' % e)            print('post请求出错,原因:%s' % e)        finally:            pass    def del_data(self, url, params, **kwargs):  # 删除的请求        try:            self.delete(url, params=params, headers=self.headers, **kwargs)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('del请求出错，出错原因:%s' % e)            print('del请求出错,原因:%s' % e)            return {}        finally:            pass    def put_data(self, url, params=None, json=None, **kwargs):  # put请求        try:            # data = json.dumps(params)            # data = params            self.put(url, params=params, json=json, **kwargs)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('put请求出错，出错原因:%s' % e)            print('put请求出错,原因:%s' % e)            return {}        finally:            pass    @classmethod    def request_data(cls, method, url, params=None, json=None, **kwargs):        try:            data = params            res = requests.request(method, url, params=data, json=json, **kwargs)            json_response = res            return json_response        except Exception as e:            LOG.info('put请求出错，出错原因:%s' % e)            print('put请求出错,原因:%s' % e)            return {}        finally:            pass