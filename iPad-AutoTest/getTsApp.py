# coding:utf-8
import json
import os
import urllib.parse
import urllib.request
import requests,pprint


class AppManager():
    def __init__(self):
        self.shortLink = 'hdadhoc'
        # self.shortLink = 'adhoc2'
        self.password = '320bnm'
        self.pageNo =1 #下包地址页码
        self.pageSize = 1 #下载包列表个数
        self.host = 'http://platform-oss.api.mgtv.com'
        self.path = '/api/outer/app/preview'
        self.data = {}
        self.downloadHost = 'http://ugc.hitv.com/'
        self.filepath= '/Users/atx/Desktop/iPad-AutoTest/ipa/'

    def getTsRequestdata(self):
        '''请求参数'''
        self.data = {'shortLink':self.shortLink,
                'password':self.password,
                'pageNo':self.pageNo,
                'pageSize':self.pageSize
                }
        return self.data
        # return urllib.parse.urlencode(self.data)

    def getTsUrl(self):
        '''完整下载请求接口'''
        return self.host + self.path +'?' + urllib.parse.urlencode(self.getTsRequestdata())


    def getTsResponese(self):
        '''获取接口响应内容'''
        res=requests.get(self.getTsUrl())
        # pprint.pprint(res.json())
        return res.json()

        # params=urllib.parse.urlencode(self.getTsRequestdata())
        # data = bytes(params, encoding='utf8')
        # responese =  urllib.request.urlopen(self.host+self.path,data = data)
        # return (responese.read().decode())

    def getappurl(self):
        '''获取ipa下载地址'''
        # responese = json.loads(self.getTsResponese())
        data=self.getTsResponese()
        data = data["data"]["packageList"][0]
        fileUrl = data['fileUrl']
        return self.downloadHost + fileUrl

    def exeLocalcmd(self,str):
        '''执行本地cmd命令'''
        print(str)
        with os.popen(str) as stdout:
            result = stdout.read()
        return result

    def DownloadApp(self,url,savepath):
        '''执行下载'''
        str = "curl " + url + " -o " + savepath
        self.exeLocalcmd(str)

    def deviceExist(self,udid=""):
        '''检测本地设备是否连接'''
        str = "ios-deploy -c"
        result = self.exeLocalcmd(str)
        print(result)

        if  result.find("Found")==-1: #判断是否有设备连接
            print("can't find any devices")
            return False
        if udid.strip() and result.find(udid) ==-1 :  #判断指定的设备是否连接
            print("can't find device --" +udid)
            return False
        return True

    def uninstallapp(self,bundleid,udid = ""):
        isExist = self.deviceExist(udid)
        if not isExist:
            return
        str = "ios-deploy -9 -1 " + bundleid
        if udid:
            str = str +" -i " + udid
        self.exeLocalcmd(str)

    def installApp(self,path,udid="eea1bc48d18637186fb815485c5210092e6b9566",bundleid="",uninstall=0):
        isExist = self.deviceExist(udid)
        if not isExist:
            return
        str = "ios-deploy "  + "-b " +path
        if udid:
            str = str + " -i " + udid

        if uninstall and bundleid.strip():
            str = str + " -r -1 " + bundleid

        self.exeLocalcmd(str)

if __name__ == '__main__':
    TM = AppManager()
    # print(TM.getTsUrl())
    # print(TM.getTsRequestdata())
    # TM.getTsResponese()
    # url=TM.getappurl()
    # print(url)
    name = 'mgtv.ipa'
    TM.DownloadApp(TM.getappurl(),TM.filepath+name)
    # TM.deviceExist()
    #TM.exeLocalcmd("ios-deploy -c")
    # TM.installApp(TM.filepath+name)
    #print(TM.getappurl())