"""
IPAD自动化测试
肖子淅
日期：2022年07月26日
装包，卸载包操作类
"""
# coding:utf-8
import json
import os
import urllib.parse
import urllib.request
import os
import subprocess
from Utils import *

class AppOpt():

    def __init__(self):
        self.savepath= '/Users/xiaozixi/Desktop/自动化测试/iPhone自动化测试/MGTV-iPhone-appstore.ipa'   #安装包路径
        self.bundleid = 'com.hunantv.imgotv'

    def setBundleid(self):
        self.bundleid = 'com.hunantv.imgotv'



    def deviceExist(self,udid=""):
        str = "ios-deploy -c"
        result = Utils().exeLocalcmd(str)
        print(result)
        if  result.find("Found")==-1:
            print("can't find any devices")
            return False
        if udid.strip() and result.find(udid) ==-1 :
            print("can't find device --" +udid)
            return False
        return True


    def uninstall(self,udid = ""):
        isExist = self.deviceExist(udid)
        if not isExist:
            return
        str = "ios-deploy -9 -1 " + 'com.hunantv.imgotv'
        if udid:
            str = str +" -i " + udid
        Utils().exeLocalcmd(str)

    def install(self ,udid="",delete=0):
        isExist = self.deviceExist(udid)
        if not isExist:
            return False
        str = "ios-deploy "  + "-b " +self.savepath
        if udid:
            str = str + " -i " + udid

        if delete :
            str = str + " -r -1 " + 'com.hunantv.imgotv'
        print("----------install app -----------")
        Utils().exeLocalcmd(str)
        return True


