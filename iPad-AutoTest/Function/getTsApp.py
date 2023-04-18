"""
IPAD自动化测试
肖子淅
日期：2022年07月26日
"""
# coding:utf-8
import json
import os
import urllib.parse
import urllib.request
import Utils
from Utils import Utils

class AppManager():
    def __init__(self):
        self.shortLink = 'adhoc3'
        self.password = '320bnm'
        self.pageNo =1
        self.pageSize = 1
        self.host = 'http://platform-oss.api.mgtv.com'
        self.path = '/api/outer/app/preview'
        self.data = {}
        #self.downloadHost = 'http://ugc.hitv.com/'
        self.downloadHost = 'https://ossimg.hitv.com/'
        self.savepath= '/Users/xiaozixi/Desktop/自动化测试/'

    def setshortLink(self,link):
        self.shortLink = link

    def getTsRequestdata(self):
        self.data = {'shortLink':self.shortLink,
                'password':self.password,
                'pageNo':self.pageNo,
                'pageSize':self.pageSize
                }
        return self.data

    def getTsUrl(self):
        return self.host + self.path +'?' + urllib.parse.urlencode(self.getTsRequestdata())

    def getTsResponese(self):
        params=urllib.parse.urlencode(self.getTsRequestdata())
        data = bytes(params, encoding='utf8')
        responese =  urllib.request.urlopen(self.host+self.path,data = data)
        return (responese.read().decode())

    def getappurl(self):
        print(self.getTsUrl() + '.....')
        responese = json.loads(self.getTsResponese())
        print(responese)
        data = responese["data"]["packageList"][0]
        fileUrl = data['fileUrl']
        return self.downloadHost + fileUrl


    def DownloadApp(self,url):
        str = "curl " + url + " -o " + self.savepath
        print("------Start Download-------")
        Utils().exeLocalcmd(str)
        print("------End   Download-------")


if __name__ == '__main__':
    TM = AppManager()
    #print(TM.getTsUrl())
    #print(TM.getTsResponese())
    url = TM.getappurl()
    print(url)
    name = 'iphone.ipa'
    TM.DownloadApp(url)
    #TM.exeLocalcmd("ios-deploy -c")
    #TM.installApp(TM.savepath)
    #print(TM.getappurl())