"""
IPAD自动化测试
肖子淅
日期：2022年07月26日
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

dev = {
    "platformName": "iOS",
    "deviceName": "可妮兔",
    "platformVersion": "14.3",
    "udid": "00008030-0016586E3623802E",
    "bundleId": "com.hunantv.imgotv",
    "noReset": "true",
    "AutomationName": "XCUITest",
    "xcodeOrgId": "WKQZHDVG49",
    "xcodeSigningId": "iphone Developer"
}



# class download_test(unittest.TestCase):
#
#     def setUp(self) :
#         # self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dev)
#         self.driver = webdriver
#         time.sleep(10)
#         self.AppOpt = AppOpt(self.driver)
#         self.BasePage = BasePage(self.driver)
#
#
#     def tearDown(self):
#         self.driver.close_app()
#         pass
#
#
#     def test_001(self):
#         for i in range(1, 1000):
#             try:
#                 print(i)
#                 #self.AppOpt.install()
#                 self.driver.Remote("http://127.0.0.1:4723/wd/hub", dev)
#                 time.sleep(5)
#                 self.BasePage.click_ele_xpath('**//XCUIElementTypeButton[@name="同意并继续"]')
#                 print('a')
#                 self.BasePage.click_ele('**/XCUIElementTypeButton[`label == "我知道了"`]')
#                 print('b')
#                 self.BasePage.click_ele('**/XCUIElementTypeButton[`label == "Fullwindows close"`]')
#                 print('c')
#                 self.BasePage.click_ele('**/XCUIElementTypeStaticText[`label == "电视剧"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeStaticText[`label == "摧毁"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeButton[`label == "MG Media Download normal class"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeStaticText[`label == "1"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeButton[`label == "vodplayer back Shadow"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeButton[`label == "vodplayer back Shadow"`]')
#                 self.BasePage.click_ele('**/XCUIElementTypeTabBar[`label == "标签栏"`]/XCUIElementTypeButton[5]')
#                 self.BasePage.click_ele('**/XCUIElementTypeStaticText[`label == "我的下载"`]')
#                 str = self.BasePage.find_ele('**/XCUIElementTypeStaticText[`label == "摧毁"`]').get_attribute('value')
#                 assert str == '摧毁'
#                 self.AppOpt.uninstall()
#             except Exception as e:
#                 print('这里就出错了')
#                 break

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


    def uninstall(self ,udid = ""):
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

    def click(self, loc):
        try:
            driver.find_element_by_xpath(loc).click()
            time.sleep(5)
        except:
            time.sleep(5)

    def click_text(self, text):
        try:
            driver.find_elements_by_link_text(text).click()
            time.sleep(5)
        except:
            time.sleep(5)


for i in range(1, 1000):
    try:
        print(i)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", dev)
        time.sleep(15)
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="同意并继续"]').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="允许"]').click()
        # time.sleep(10)
        # AppOpt().click('//XCUIElementTypeButton[@name="我知道了"]')
        # time.sleep(10)
        # AppOpt().click('//XCUIElementTypeButton[@name="Fullwindows close"]')
        # time.sleep(5)
        # driver.tap([(275, 80)], 500)  #点击电视剧 跳转到电视剧频道
        # time.sleep(5)
        # AppOpt().click_text('使用App时允许')
        # driver.swipe(200, 400, 200, 200, 500)
        # driver.swipe(200, 400, 200, 200, 500)
        # driver.swipe(200, 400, 200, 200, 500)
        # driver.swipe(200, 400, 200, 200, 500)
        # time.sleep(5)
        # # #driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="摧毁"]').click()
        # driver.tap([(200, 150)], 500)
        # time.sleep(5)
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="meetion tips Know"]').click() #一起看浮层 知道了按钮
        # time.sleep(5)
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="MG Media Download normal class"]').click()
        # time.sleep(5)
        # driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="1"]').click()
        # time.sleep(5)
        # driver.tap([(100, 100)], 500)
        # time.sleep(5)
        # driver.find_element_by_xpath('//XCUIElementTypeButton[@name="vodplayer back Shadow"]').click()
        # time.sleep(5)
        driver.find_element_by_xpath('//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[5]').click()
        time.sleep(5)
        AppOpt().click('//XCUIElementTypeButton[@name="Fullwindows close"]') #关闭广告大弹窗
        time.sleep(5)
        driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="我的下载"]').click()
        time.sleep(5)
        str = driver.find_element_by_xpath('//XCUIElementTypeStaticText[@name="摧毁"]').get_attribute('value')
        time.sleep(1)
        print(str)
        assert str == '摧毁'
        time.sleep(20)
    except Exception as e:
        print('这里就出错了')
        break