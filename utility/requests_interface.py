# -*- coding: utf-8 -*-import unittestimport seldomfrom config.log import LOGclass RoomRequest(seldom.TestCase, unittest.TestCase):    # def __init__(self):    #     super().__init__()    #     # self.headers = {    #     #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "    #     #                   "Chrome/91.0.4472.124 Safari/537.36"}    headers = {        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "                      "Chrome/91.0.4472.124 Safari/537.36"}    def get_data(self, url, params):  # get消息        try:            return self.get(url, params, headers=self.headers)        except Exception as e:            LOG.info('get请求出错，出错原因:%s' % e)            print('get请求出错,出错原因:%s' % e)            return {}        finally:            # self.assertStatusCode()            pass    def post_data(self, url, params):  # post消息        # data = json.dumps(params)        data = params        try:            self.post(url, params=data, headers=self.headers)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('post请求出错，出错原因:%s' % e)            print('post请求出错,原因:%s' % e)        finally:            pass    def del_data(self, url, params):  # 删除的请求        try:            self.delete(url, params=params, headers=self.headers)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('del请求出错，出错原因:%s' % e)            print('del请求出错,原因:%s' % e)            return {}        finally:            pass    def put_data(self, url, params):  # put请求        try:            # data = json.dumps(params)            data = params            self.put(url, data)            # json_response = json.loads(self.response)            json_response = self.response            return json_response        except Exception as e:            LOG.info('put请求出错，出错原因:%s' % e)            print('put请求出错,原因:%s' % e)            return {}        finally:            pass