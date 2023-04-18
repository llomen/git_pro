# coding:utf-8
from appium import webdriver
import time
import unittest
from page import jingxuan_page, base
from page import base
from page import jingxuan_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.wode_page import MyPage
from page.jingxuan_page import JingxuanPage
from page.pindao_page import PindaoPage
from HTMLTestRunner import HTMLTestRunner
import logging

now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())

class jingxuan_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)
        cls.JingxuanPage = JingxuanPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_001(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain).get_attribute('label')
        print(str)
        assert str == '芒果TV'

    def test_002(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain11).get_attribute('label')
        assert str == '猜你在追'

    def test_003(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain12).get_attribute('label')
        assert str == '更多'

    def test_004(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain10).get_attribute('label')
        assert str == '片库'

    def test_005(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain2).get_attribute('label')
        assert str == '综艺'

    def test_006(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain3).get_attribute('label')
        assert str == '电视剧'

    def test_007(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain4).get_attribute('label')
        assert str == '电影'

    def test_008(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain5).get_attribute('label')
        assert str == '少儿'

    def test_009(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain6).get_attribute('label')
        assert str == '动漫'

    def test_010(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain7).get_attribute('label')
        assert str == '大芒'

    def test_011(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain8).get_attribute('label')
        assert str == '新闻'

    def test_012(self):
        self.driver.swipe(300, 33, 100, 33, 1000)
        str = self.JingxuanPage.find_ele(JingxuanPage.chain9).get_attribute('label')
        assert str == '音乐'

    def test_013(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain13).get_attribute('label')
        assert str == '当季热播'

    def test_014(self):
        str = self.JingxuanPage.find_ele_xpath(JingxuanPage.chain14).get_attribute('label')
        assert str == '首页'

    def test_015(self):
        str = self.JingxuanPage.find_ele_xpath(JingxuanPage.chain15).get_attribute('label')
        assert str == '大芒'

    def test_016(self):
        str = self.JingxuanPage.find_ele_xpath(JingxuanPage.chain16).get_attribute('label')
        assert str == '会员'

    def test_017(self):
        str = self.JingxuanPage.find_ele_xpath(JingxuanPage.chain17).get_attribute('label')
        assert str == '一起看'

    def test_018(self):
        str = self.JingxuanPage.find_ele_xpath(JingxuanPage.chain18).get_attribute('label')
        assert str == '我的'

    def test_019(self):
        driver = self.driver
        driver.swipe(20, 700, 20, 400, 1000)
        driver.swipe(20, 700, 20, 400, 1000)
        driver.get_screenshot_as_file('大芒短视频.png')
        time.sleep(5)
        str = self.JingxuanPage.find_ele(JingxuanPage.chain19).get_attribute('label')
        assert str == '大芒短视频'

    def test_020(self):
        driver = self.driver
        driver.swipe(20, 700, 20, 400, 1000)
        time.sleep(5)
        str = self.JingxuanPage.find_ele(JingxuanPage.chain20).get_attribute('label')
        assert str == '即将上线'

    def test_021(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain21).get_attribute('label')
        assert str == '预约'

    def test_022(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain22).get_attribute('label')
        assert str == '我的预约'

    def test_023(self):
        str = self.JingxuanPage.find_ele(JingxuanPage.chain23).get_attribute('label')
        assert str == '即将上线'

    def test_024(self):
        driver = self.driver
        driver.swipe(20, 700, 20, 400, 1000)
        time.sleep(5)
        str = self.JingxuanPage.find_ele(JingxuanPage.chain24).get_attribute('label')
        assert str == '猜你喜欢'

if __name__ == '__main__':
    testsuite = unittest.TestSuite()
