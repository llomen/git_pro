"""
IPAD自动化测试
肖子淅
日期：2022年07月19日
"""
import cv2
import numpy as np
from appium import webdriver
import time
import unittest
import page
from page import base
from page import login_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.jingxuan_page import JingxuanPage
from appium.webdriver.common.touch_action import TouchAction






class login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)
        cls.driver.implicitly_wait(5)


    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_001(self):
        "手机登录风控滑块"
        driver = self.driver
        self.driver.find_element_by_xpath(JingxuanPage.chain18).click()
        time.sleep(3)
        self.LoginPage.mobile_login(17764592306)
        self.LoginPage.cut(LoginPage.background_ele, 'background')
        self.LoginPage.cut(LoginPage.slider_ele, 'slider')
        print(self.LoginPage.get_element_slide_distance(LoginPage.slider_ele, LoginPage.background_ele))
        distance = int(self.LoginPage.get_element_slide_distance(LoginPage.slider_ele, LoginPage.background_ele))
        driver.swipe(420, 520, 420+distance, 520, 10000)

if __name__ == '__main__':
    suite = unittest.TestSuite()

