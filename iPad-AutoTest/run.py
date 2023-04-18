# coding:utf-8
import sys
import getopt
import os
import warnings
import datetime
import urllib
import requests
from urllib.request import urlopen
from urllib.parse import urlencode
#import urllib2
import subprocess,threading
from pprint import pprint
import multiprocessing
import datetime, time
# from robot.api import TestData
import json,pprint
# from robot.api import TestData
from robot.api import ExecutionResult
from robot.utils import elapsed_time_to_string
from getTsApp import AppManager

class Testsuite:
    def __init__(self, dir):
        self.suitedir = dir
        self.suitename= ''
        self.suitedetails = []

    def setdir(self,dir):
        self.suitedir = dir
    def setname(self,name):
        self.suitename = name

    def addChild(self, testcase):
        self.suitedetails.append(testcase)

class readSuite:
    def __init__(self,source):
        self.source= source
        self.suites=[]
        self.testdata = TestData(source=source)
        self.dic=[]
        self.version = self.testdata._get_basename()

    def addSuite(self):
        self.dic.append(self.testdata)
        while  self.dic:
            file = self.dic.pop(0)
            if not file.has_tests():
                break
            if file.children:
                for child in file.children:
                    self.dic.append(child)
            else:
                self.suites.append(self.readcase(file))

    def readcase(self,suite):
        testsuite = Testsuite(suite.source)
        #print(testsuite.dir)
        #print(testsuite.dir.replace(self.source,''))
        #print(suite.name)
        #print(suite.directory)
        #print(suite.directory.replace(self.source,''))
        testsuite.setname(suite.name)
        testsuite.setdir(suite.directory.replace(self.source,''))
        i = suite.testcase_table.__iter__()
        for case in i:
            # print (case.name)
            steps = []
            name = case.name
            for step in case.steps:
                # print(step.as_list(indent=True))
                steps.append('    '.join(step.as_list(indent=True)))
            content = '\n'.join(steps)
            # print(content)
            testcase = {}
            testcase['casename']= name
            testcase['casecontent']=content
            testsuite.addChild(testcase)
            # print(json.dumps(testsuite))
        return testsuite.__dict__

class readReport():
    def __init__(self,source):
        self.source = source
        self.result = ExecutionResult(source)
        self.suites=[]
        self.tests=[]

    def addReport(self,report_url):
        suite = self.result.suite
        if not suite :
            return None
        else :
            self.suites.append(suite)
        report={'version':suite.name,'platform':'iPad','starttime':suite.starttime,'endtime':suite.endtime,'reporturl':report_url}
        report['elapsedtime'] = elapsed_time_to_string(suite.elapsedtime)
        result = suite.statistics.all.get_attributes()
        report.update(result)
        #report['suites']=[]
        while  self.suites:
            suites = self.suites.pop(0)
            if suites.suites:
                for child in suites.suites:
                    self.suites.append(child)
            if suites.tests:
                children = []

                case = {'suitename': suites.name, 'starttime': suites.starttime,'endtime':suites.endtime}
                case['elapsedtime'] = elapsed_time_to_string(suites.elapsedtime)
                case['dir']=suites.source.replace(suite.source, '')
                result = suites.statistics.all.get_attributes()
                case.update(result)

                for child in suites.tests:
                    c={}
                    c['name'] = child.name
                    c['status']=child.status
                    c['message']=child.message
                    children.append(c)
                case['cases']= children
                self.tests.append(case)
        report['suites'] = self.tests
        #print(report)
        return report

def insert_case():
    #   channel改成了调试
    DIR = '/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTestipad-auto/调试'
    suite = readSuite(DIR)
    suite.addSuite()

    test_data = {}
    test_data['version'] = suite.version
    test_data['platform'] = 'iPad'
    test_data['data'] = suite.suites
    datas = json.dumps(test_data)
    # pprint.pprint(datas)

    print('insert case data...')
    # requrl = "http://172.31.33.22:8880/cases/UpdataTestCase"
    requrl = "http://10.200.12.153/cases/UpdataTestCase"
    req = requests.post(requrl, data=datas)
    print(req)
    print('insert finished!')

def insert_report(report_url):
    DIR = '/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/output.xml'     #本地调试读取xml报告路径
    # DIR = '/Users/atx/.jenkins/workspace/iPad_auto/output_back.xml'   #jenkins远程执行读取路径
    report = readReport(DIR)
    result = report.addReport(report_url)
    result_data=json.dumps(result)
    # pprint.pprint(result_data)

    print('insert report...')
    # requrl = "http://172.31.33.22:8880/cases/UpdataResults"
    requrl = "http://10.200.12.153/cases/UpdataResults"
    req = requests.post(requrl, data=result_data)
    print(req)
    print('insert report finished!')

def prerun_handle():
    threads = []
    ipa_name='iPad.ipa'

    #并行处理安装包和下载安装包
    p1 = threading.Thread(target=insert_case, args=())
    threads.append(p1)
    TM = AppManager()

    p2 = threading.Thread(target=TM.DownloadApp, args=(TM.getappurl(),TM.filepath+ipa_name))
    threads.append(p2)

    for p in threads:
        p.start()
    for p in threads:
        p.join()

    print('install app...')
    TM.installApp(TM.filepath + ipa_name)
    print('install app finished')



def delete_old_report():
    try:
        os.remove('/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTestipad-auto/output_back.xml')
    except FileNotFoundError :
        print('output_back.xml not found')
    try:
        os.remove('/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTestipad-auto/report.html')
    except FileNotFoundError :
        print('report.html not found')


if __name__ == '__main__':

    # insert_case()

    # prerun_handle()
    # delete_old_report()

    # suites=sys.argv[1]
    # report_url=sys.argv[2]+'robot/report/report.html'
    # print(report_url)

    # suite_list='-s 1搜索入口 -s 2搜索纠错  -s 3搜索结果筛选 -s  4搜索结果展示    '
    # suite_list='-s 01点播评论  -s 03我的看单  -s 02HB  -s  04我-未登录  -s 05我-非会员  -s 06我-会员  -s 5我的  -s 6片库 '
    # suite_list=' -s 07缓存  -s  08点播页跳转 -s 09播单 -s 10直播分享 -s 11直播切换机位  '
    # suite_list=' -s 前贴广告   -s 广告流失率  -s 小窗页面跳转   '
    # suite_list=' -s 01猜你在追   -s 02预约  -s 03猜你喜欢    '
    suite_list=' '

    # for suite in suites.strip(',').split(','):
    #     cmd=' -s '+suite
    #     suite_list=suite_list+cmd
    # print(suite_list)
    #   channel改成了调试
    cmd='robot '+suite_list+' /Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/channel/灰度测试'
    print(cmd)
    subprocess.call(cmd,shell=True)


    report_url=''
    insert_report(report_url)


