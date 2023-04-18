"""
iPhone 启动下拉崩溃复现测试
肖子淅
日期：2023年02月10日
"""
from appium import webdriver
import time
import unittest
from page.BasePage import BasePage
import page
from page import base
from page import login_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.pianku_page import PiankuPage
from page.search_page import SearchuPage
from Utils import *



dev = {
    "platformName": "iOS",
    "deviceName": "可妮兔",
    "platformVersion": "14.3",
    "udid": "00008020-001A54623A04002E",
    "bundleId": "com.hunantv.imgotv",
    "noReset": "true",
    "AutomationName": "XCUITest",
    "xcodeOrgId": "WKQZHDVG49",
    "xcodeSigningId": "iphone Developer"
}



for i in range(1,1000):
    try:
        print(i)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dev)
        time.sleep(15)
        driver.swipe(200, 200, 200, 400, 500)
        time.sleep(10)
    except:
        print('这里就出错了')
        break


