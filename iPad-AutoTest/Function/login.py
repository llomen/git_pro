"""
IPAD自动化测试
肖子淅
日期：2022年04月26日
"""
from appium import webdriver
import time
import unittest
import page
from page import base
from page import login_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.jingxuan_page import JingxuanPage





class login_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()



    def test_001(self):
        "有快捷登录时邮箱登录"
        self.driver.find_element_by_xpath(JingxuanPage.chain18).click()
        time.sleep(3)
        self.LoginPage.into_mail_login()
        self.LoginPage.mail_login(base.mail, base.mail_secret)

    def test_002(self):
        #邮箱登录登出
        self.LoginPage.logout()

    def test_003(self):
        # 快捷登录
        self.driver.find_element_by_xpath(JingxuanPage.chain18).click()
        time.sleep(3)
        self.LoginPage.click_ele(LoginPage.chain1)
        self.LoginPage.quick_login()

    def test_004(self):
        #快捷登录登出
        self.LoginPage.logout()

if __name__ == '__main__':
    suite = unittest.TestSuite()










