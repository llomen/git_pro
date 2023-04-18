"""
IPAD自动化测试
肖子淅
日期：2022年05月11日
搜索功能测试
"""
from appium import webdriver
import time
import unittest
import page
from page import base
from page import login_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.pianku_page import PiankuPage
from page.search_page import SearchuPage

class search_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)
        cls.PiankuPage = PiankuPage(cls.driver)
        cls.SearchPage = SearchuPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_001(self):
        #搜索入口，进入搜索页
        self.SearchPage.click_ele_xpath(SearchuPage.xpath1)
        time.sleep(10)

    def test_002(self):
        #热搜榜单
        str = self.SearchPage.find_ele(SearchuPage.chain3).get_attribute('label')
        assert str == '热搜榜单'

    def test_003(self):
        #热搜榜单分类
        str = self.SearchPage.find_ele(SearchuPage.chain4).get_attribute('label')
        assert str == '综合'
        str = self.SearchPage.find_ele(SearchuPage.chain5).get_attribute('label')
        assert str == '综艺'
        str = self.SearchPage.find_ele(SearchuPage.chain6).get_attribute('label')
        assert str == '电视剧'
        str = self.SearchPage.find_ele(SearchuPage.chain7).get_attribute('label')
        assert str == '电影'
        str = self.SearchPage.find_ele(SearchuPage.chain8).get_attribute('label')
        assert str == '动漫'

    def test_004(self):
        #搜索历史
        str = self.SearchPage.find_ele(SearchuPage.chain9).get_attribute('label')
        assert str == '搜索历史'

    def test_005(self):
        #搜索推荐
        str = self.SearchPage.find_ele(SearchuPage.chain10).get_attribute('label')
        assert str == '搜索推荐'

    def test_006(self):
        #搜索后搜索记录出现在搜索历史中
        self.SearchPage.send_keys(SearchuPage.chain11, 'hhhh')
        self.SearchPage.search_enter()
        self.SearchPage.click_ele(SearchuPage.chain13)
        str = self.SearchPage.find_ele(SearchuPage.chain14).get_attribute('value')
        assert str == 'hhhh'

    def test_007(self):
        #搜索输入联想推荐词条
        self.SearchPage.send_keys(SearchuPage.chain11, 'hhhh')
        str = self.SearchPage.find_ele(SearchuPage.chain15).get_attribute('value')
        assert str == '哈哈哈哈哈'
        str = self.SearchPage.find_ele(SearchuPage.chain16).get_attribute('value')
        assert str == '哈哈哈哈哈第2季'
        str = self.SearchPage.find_ele(SearchuPage.chain17).get_attribute('value')
        assert str == '花红花火'

    def test_008(self):
        #搜索结果页自动纠错
        self.SearchPage.search_enter()
        str = self.SearchPage.find_ele(SearchuPage.chain18).get_attribute('value')
        assert str == '花红花火'

    def test_009(self):
        #搜索结果页的相关搜索，热门搜索
        # str = self.SearchPage.find_ele(SearchuPage.chain20).get_attribute('value')
        # assert str == '相关搜索'
        str = self.SearchPage.find_ele(SearchuPage.chain21).get_attribute('value')
        assert str == '热门搜索'

    def test_010(self):
        #搜索结果页的高级筛选
        str = self.SearchPage.find_ele(SearchuPage.chain19).get_attribute('value')
        assert str == '高级筛选 '
        self.SearchPage.click_ele(SearchuPage.chain19)
        str = self.SearchPage.find_ele(SearchuPage.chain22).get_attribute('value')
        assert str == '时长'
        str = self.SearchPage.find_ele(SearchuPage.chain23).get_attribute('value')
        assert str == '发布时间'
        str = self.SearchPage.find_ele(SearchuPage.chain24).get_attribute('value')
        assert str == '排序'

    def test_011(self):
        #退出搜索页
        self.SearchPage.click_ele(SearchuPage.chain2)

    def test_012(self):
        #通过搜索进入点播，起播
        self.SearchPage.click_ele_xpath(SearchuPage.xpath1)
        self.SearchPage.send_keys(SearchuPage.chain11, '向往的生活')
        self.SearchPage.search_enter()
        self.SearchPage.tap_point()
        time.sleep(5)
        str = self.SearchPage.find_ele(SearchuPage.chain26).get_attribute('label')
        assert str == '向往的生活 第六季'

    def test_013(self):
        #退出点播
        self.SearchPage.click_ele(SearchuPage.back)

    def test_014(self):
        #搜索结果页进入相关搜索的点播
        self.SearchPage.click_ele(SearchuPage.chain27)
        time.sleep(5)
        str = self.SearchPage.find_ele(SearchuPage.chain28).get_attribute('label')
        assert str == '明星大侦探 第六季'
        self.SearchPage.click_ele(SearchuPage.chain26)

    def test_015(self):
        #搜索结果页进入热门搜索的点播
        self.SearchPage.click_ele(SearchuPage.chain29)
        self.SearchPage.tap_point()
        time.sleep(5)
        str = self.SearchPage.find_ele(SearchuPage.chain26).get_attribute('label')
        assert str == '向往的生活 第六季'
        self.SearchPage.click_ele(SearchuPage.chain26)


if __name__ == '__main__':
    suite = unittest.TestSuite()













