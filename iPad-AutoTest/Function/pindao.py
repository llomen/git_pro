"""
IPAD自动化测试
肖子淅
日期：2022年07月25日
频道切换
"""

from appium import webdriver
import time
import unittest
from page import base
from page.jingxuan_page import JingxuanPage
from page.BasePage import BasePage
from page.pindao_page import PindaoPage
from page.dianbo_page import DianboPage
from page.login_page import LoginPage


class pindao_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)
        cls.JingxuanPage = JingxuanPage(cls.driver)
        cls.Basepage = BasePage(cls.driver)
        cls.PindaoPage = PindaoPage(cls.driver)
        cls.DianboPage = DianboPage(cls.driver)



    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_001(self):
        "精选页进点播"
        driver = self.driver
        driver.swipe(200,400,200,200, 5000)
        self.Basepage.click_ele_point(PindaoPage.chain18)

    def test_002(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain2).get_attribute('value')
        assert str == '女儿们的恋爱 第四季'

    def test_003(self):
        "点播页返回精选页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_004(self):
        "进入综艺频道"
        self.Basepage.click_ele_point(PindaoPage.chain2)


    def test_005(self):
        "综艺频道进入点播"
        self.Basepage.click_ele_point(PindaoPage.chain19)

    def test_006(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain3).get_attribute('value')
        assert str == '爸爸当家'

    def test_007(self):
        "点播页返回综艺频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_008(self):
        "进入电视剧频道"
        self.Basepage.click_ele_point(PindaoPage.chain3)


    def test_009(self):
        "电视剧频道进入点播"
        self.Basepage.click_ele_point(PindaoPage.chain20)

    def test_010(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain4).get_attribute('value')
        assert str == '好好说话'

    def test_011(self):
        "点播页返回电视剧频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_012(self):
        "进入电影频道"
        self.Basepage.click_ele_point(PindaoPage.chain4)

    def test_013(self):
        "电影频道进入点播"
        driver = self.driver
        driver.swipe(100,200,100,100,5000)
        self.Basepage.click_ele_point(PindaoPage.chain21)

    def test_014(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain5).get_attribute('value')
        assert str == '长津湖之水门桥'

    def test_015(self):
        "点播页返回电影频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_016(self):
        "进入少儿频道"
        self.Basepage.click_ele_point(PindaoPage.chain5)

    def test_017(self):
        "少儿频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain22)

    def test_018(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain6).get_attribute('value')
        assert str == '汪汪队立大功 第八季'

    def test_019(self):
        "点播页返回少儿频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_020(self):
        "进入动漫频道"
        self.Basepage.click_ele_point(PindaoPage.chain6)

    def test_021(self):
        "动漫频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain23)

    def test_022(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain7).get_attribute('value')
        assert str == '郡主稳住，人设不能崩'

    def test_023(self):
        "点播页返回动漫频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)


    def test_024(self):
        "进入大芒频道"
        self.Basepage.click_ele_point(PindaoPage.chain7)

    def test_025(self):
        "大芒频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain24)

    def test_026(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain8).get_attribute('value')
        assert str == '大芒星歌汇'

    def test_027(self):
        "点播页返回大芒频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_028(self):
        "进入新闻频道"
        self.Basepage.click_ele_point(PindaoPage.chain8)

    def test_029(self):
        "新闻频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain25)

    def test_030(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain9).get_attribute('value')
        assert str == '中国外交部：七国集团不要以“家法帮规”霸凌他国'

    def test_031(self):
        "点播页返回新闻频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_032(self):
        "进入音乐频道"
        self.Basepage.click_ele_point(PindaoPage.chain9)

    def test_033(self):
        "音乐频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain26)

    def test_034(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain10).get_attribute('value')
        assert str == 'A-Lin《挚友》MV'

    def test_035(self):
        "点播页返回音乐频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)

    def test_036(self):
        "进入游戏频道"
        self.Basepage.click_ele_point(PindaoPage.chain10)

    def test_037(self):
        "游戏频道进入点播"
        driver = self.driver
        self.Basepage.click_ele_point(PindaoPage.chain27)

    def test_038(self):
        "点播媒资名称"
        str = self.Basepage.find_ele(DianboPage.chain11).get_attribute('value')
        assert str == '我的世界：魔法大陆和虚无世界'

    def test_039(self):
        "点播页返回游戏频道页"
        self.Basepage.click_ele_point(DianboPage.chain1)



if __name__ == '__main__':
    suite = unittest.TestSuite()




