"""
IPAD自动化测试
肖子淅
日期：2022年05月11日
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


class pianku_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        cls.LoginPage = LoginPage(cls.driver)
        cls.PiankuPage = PiankuPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    def test_001(self):
        #进入片库
        self.PiankuPage.to_pianku()
        str = self.PiankuPage.find_ele(PiankuPage.chain2).get_attribute('label')

    def test_002(self):
        #进入综艺频道
        self.PiankuPage.click_ele(PiankuPage.chain3)

    def test_003(self):
        #片库综艺频道
        str = self.PiankuPage.find_ele(PiankuPage.chain3).get_attribute('label')
        assert str == '综艺'

    def test_004(self):
        #综艺频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain17).get_attribute('label')
        assert str == '大侦探 第七季'

    def test_005(self):
        #进入综艺频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain17)
        str = self.PiankuPage.find_ele(PiankuPage.chain31).get_attribute('label')
        assert str == '大侦探 第七季'

    def test_006(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_007(self):
        #进入电视剧频道
        self.PiankuPage.click_ele(PiankuPage.chain4_2)

    def test_008(self):
        #片库电视剧频道
        str = self.PiankuPage.find_ele(PiankuPage.chain4).get_attribute('label')
        assert str == '电视剧'

    def test_009(self):
        #电视剧频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain18).get_attribute('label')
        assert str == '尚食'

    def test_010(self):
        #进入电视剧频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain18)
        str = self.PiankuPage.find_ele(PiankuPage.chain32).get_attribute('label')
        assert str == '尚食'

    def test_011(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_012(self):
        #进入电影频道
        self.PiankuPage.click_ele(PiankuPage.chain5_2)

    def test_013(self):
        #片库电视剧频道
        str = self.PiankuPage.find_ele(PiankuPage.chain5).get_attribute('label')
        assert str == '电影'

    def test_014(self):
        #电影频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain19).get_attribute('label')
        assert str == '这个杀手不太冷静'

    def test_015(self):
        #进入电影频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain19)
        str = self.PiankuPage.find_ele(PiankuPage.chain33).get_attribute('label')
        assert str == '这个杀手不太冷静'

    def test_016(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_017(self):
        #进入动漫频道
        self.PiankuPage.click_ele(PiankuPage.chain6_2)

    def test_018(self):
        #片库动漫频道
        str = self.PiankuPage.find_ele(PiankuPage.chain6).get_attribute('label')
        assert str == '动漫'

    def test_019(self):
        #动漫频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain20).get_attribute('label')
        assert str == '宝贝赳赳 第三季'

    def test_020(self):
        #进入动漫频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain20)
        str = self.PiankuPage.find_ele(PiankuPage.chain34).get_attribute('label')
        assert str == '宝贝赳赳 第三季'

    def test_021(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_022(self):
        #进入少儿频道
        self.PiankuPage.click_ele(PiankuPage.chain7_2)

    def test_023(self):
        #片库少儿频道
        str = self.PiankuPage.find_ele(PiankuPage.chain7).get_attribute('label')
        assert str == '少儿'

    def test_024(self):
        #少儿频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain20).get_attribute('label')
        assert str == '宝贝赳赳 第三季'

    def test_025(self):
        #进入少儿频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain20)
        str = self.PiankuPage.find_ele(PiankuPage.chain34).get_attribute('label')
        assert str == '宝贝赳赳 第三季'

    def test_026(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_027(self):
        #进入纪录片频道
        self.PiankuPage.click_ele(PiankuPage.chain8_2)

    def test_028(self):
        #片库纪录片频道
        str = self.PiankuPage.find_ele(PiankuPage.chain8).get_attribute('label')
        assert str == '纪录片'

    def test_029(self):
        #纪录片频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain21).get_attribute('label')
        assert str == '中国 第二季'

    def test_030(self):
        #进入纪录片频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain21)
        str = self.PiankuPage.find_ele(PiankuPage.chain35).get_attribute('label')
        assert str == '中国 第二季'

    def test_031(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_032(self):
        #进入新闻频道
        self.PiankuPage.click_ele(PiankuPage.chain9_2)

    def test_033(self):
        #片库新闻频道
        str = self.PiankuPage.find_ele(PiankuPage.chain9).get_attribute('label')
        assert str == '新闻'

    def test_034(self):
        #新闻频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain22).get_attribute('label')
        assert str == '焦点时刻 2022'

    def test_035(self):
        #进入新闻频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain22)
        str = self.PiankuPage.find_ele(PiankuPage.chain36).get_attribute('label')
        assert str == '焦点时刻 2022'

    def test_036(self):
        #退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_037(self):
        # 进入音乐频道
        self.PiankuPage.click_ele(PiankuPage.chain10_2)

    def test_038(self):
        # 片库音乐频道
        str = self.PiankuPage.find_ele(PiankuPage.chain10).get_attribute('label')
        assert str == '音乐'

    def test_039(self):
        # 音乐频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain23).get_attribute('label')
        assert str == '【王俊凯】四面楚歌'

    def test_040(self):
        # 进入音乐频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain23)
        str = self.PiankuPage.find_ele(PiankuPage.chain37).get_attribute('label')
        assert str == '【王俊凯】四面楚歌'

    def test_041(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_042(self):
        # 进入乐活频道
        self.PiankuPage.click_ele(PiankuPage.chain11_2)

    def test_043(self):
        # 片库乐活频道
        str = self.PiankuPage.find_ele(PiankuPage.chain11).get_attribute('label')
        assert str == '乐活'

    def test_044(self):
        # 乐活频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain24).get_attribute('label')
        assert str == '燃烧吧，卡路里 2022'

    def test_045(self):
        # 进入乐活频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain24)
        str = self.PiankuPage.find_ele(PiankuPage.chain38).get_attribute('label')
        assert str == '燃烧吧，卡路里 2022'

    def test_046(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_047(self):
        # 进入游戏频道
        self.PiankuPage.click_ele(PiankuPage.chain12_2)

    def test_048(self):
        # 片库游戏频道
        str = self.PiankuPage.find_ele(PiankuPage.chain12).get_attribute('label')
        assert str == '游戏'

    def test_049(self):
        # 游戏频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain25).get_attribute('label')
        assert str == '糖果植物大战僵尸 植物组合冒险模式'

    def test_050(self):
        # 进入游戏频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain25)
        str = self.PiankuPage.find_ele(PiankuPage.chain39).get_attribute('label')
        assert str == '糖果植物大战僵尸 植物组合冒险模式'

    def test_051(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_052(self):
        # 进入体育频道
        self.PiankuPage.click_ele(PiankuPage.chain13_2)

    def test_053(self):
        # 片库体育频道
        str = self.PiankuPage.find_ele(PiankuPage.chain13).get_attribute('label')
        assert str == '体育'

    def test_054(self):
        # 体育频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain26).get_attribute('label')
        assert str == '王者之战 2016'

    def test_055(self):
        # 进入体育频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain26)
        str = self.PiankuPage.find_ele(PiankuPage.chain40).get_attribute('label')
        assert str == '王者之战 2016'

    def test_056(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_057(self):
        # 进入体育频道
        self.PiankuPage.click_ele(PiankuPage.chain13_2)

    def test_058(self):
        # 片库体育频道
        str = self.PiankuPage.find_ele(PiankuPage.chain13).get_attribute('label')
        assert str == '体育'

    def test_059(self):
        # 体育频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain26).get_attribute('label')
        assert str == '王者之战 2016'

    def test_060(self):
        # 进入体育频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain26)
        str = self.PiankuPage.find_ele(PiankuPage.chain40).get_attribute('label')
        assert str == '王者之战 2016'

    def test_061(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_062(self):
        # 进入教育频道
        self.PiankuPage.click_ele(PiankuPage.chain14_2)

    def test_063(self):
        # 片库教育频道
        str = self.PiankuPage.find_ele(PiankuPage.chain14).get_attribute('label')
        assert str == '教育'

    def test_064(self):
        # 教育频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain27).get_attribute('label')
        assert str == '“防溺水”湖南省中小学专题课'

    def test_065(self):
        # 进入教育频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain27)
        str = self.PiankuPage.find_ele(PiankuPage.chain41).get_attribute('label')
        assert str == '“防溺水”湖南省中小学专题课'

    def test_066(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_067(self):
        # 进入原创频道
        self.PiankuPage.click_ele(PiankuPage.chain15_2)

    def test_068(self):
        # 片库原创频道
        str = self.PiankuPage.find_ele(PiankuPage.chain15).get_attribute('label')
        assert str == '原创'

    def test_069(self):
        # 原创频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain28).get_attribute('label')
        assert str == '嘴巴都笑裂了 2019'

    def test_070(self):
        # 进入原创频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain28)
        str = self.PiankuPage.find_ele(PiankuPage.chain42).get_attribute('label')
        assert str == '嘴巴都笑裂了 2019'

    def test_071(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_072(self):
        # 进入娱乐频道
        self.PiankuPage.click_ele(PiankuPage.chain16_2)

    def test_073(self):
        # 片库娱乐频道
        str = self.PiankuPage.find_ele(PiankuPage.chain16).get_attribute('label')
        assert str == '娱乐'

    def test_074(self):
        # 娱乐频道第一个媒资
        str = self.PiankuPage.find_ele(PiankuPage.chain29).get_attribute('label')
        assert str == '爱豆传送门 2020'

    def test_075(self):
        # 进入娱乐频道第一个媒资
        self.PiankuPage.click_ele(PiankuPage.chain29)
        str = self.PiankuPage.find_ele(PiankuPage.chain43).get_attribute('label')
        assert str == '爱豆传送门 2020'

    def test_076(self):
        # 退出媒资播放页回到片库
        self.PiankuPage.click_ele(PiankuPage.chain30)

    def test_77(self):
        #回到精选首页
        self.PiankuPage.click_ele(PiankuPage.back)

if __name__ == '__main__':
    suite = unittest.TestSuite()