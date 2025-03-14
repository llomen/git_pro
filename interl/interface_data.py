"""
肖子淅
日期：2024年07月24日
获取接口数据，并保存
"""
import json
import jsonpath
import requests
from Public.log import LOG, logger


class Myrq:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:51.0) Gecko/20100101 Firefox/51.0"}

    def get(self, url): #get消息
        try:
            r = requests.get(url,headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return json_response
        except Exception as e:
            LOG.info('get请求出错，出错原因:%s' % e)
            print('get请求出错,出错原因:%s' % e)
            return {}

    def post(self, url, params):  # post消息
        data = json.dumps(params)
        try:
            r = requests.post(url, params=params)
            json_response = json.loads(r.text)
            return json_response
        except Exception as e:
            LOG.info('post请求出错，出错原因:%s' % e)
            print('post请求出错,原因:%s' % e)

    def delfile(self, url, params):  # 删除的请求
        try:
            del_word = requests.delete(url, params=params)
            json_response = json.loads(del_word.text)
            return json_response
        except Exception as e:
            LOG.info('del请求出错，出错原因:%s' % e)
            print('del请求出错,原因:%s' % e)
            return {}

    def putfile(self, url, params):  # put请求
        try:
            data = json.dumps(params)
            me = requests.put(url, data)
            json_response = json.loads(me.text)
            return json_response
        except Exception as e:
            LOG.info('put请求出错，出错原因:%s' % e)
            print('put请求出错,原因:%s' % e)








