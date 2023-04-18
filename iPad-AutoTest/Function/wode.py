"""
IPAD自动化测试
肖子淅
日期：2022年04月26日
"""
from appium import webdriver
import time
import unittest

import page.login_page
from page import base
from page import jingxuan_page
from page.login_page import LoginPage
from page.BasePage import BasePage
from page.wode_page import MyPage
from page.jingxuan_page import JingxuanPage


class wo_test(unittest.TestCase):

    @classmethod
    def setUpClass(cls) :
        cls.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", base.dev2)
        time.sleep(10)
        # 使用子类之前一定要初始化
        cls.LoginPage = LoginPage(cls.driver)
        cls.MyPage = MyPage(cls.driver)
        cls.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close_app()

    ''''未登录前个人中心'''

    def test_001(self):
        driver = self.driver
        driver.find_element_by_xpath(JingxuanPage.chain18).click()
        time.sleep(2)
        str = self.LoginPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'

    def test_002(self):
        str = self.LoginPage.find_ele(MyPage.chain2).get_attribute('label')
        assert str == '登录/注册'

    def test_003(self):
        str = self.LoginPage.find_ele(MyPage.chain3).get_attribute('label')
        assert str == '领15天会员'

    def test_004(self):
        str = self.LoginPage.find_ele(MyPage.chain4).get_attribute('label')
        assert str == '签到领会员'

    def test_005(self):
        str = self.LoginPage.find_ele(MyPage.chain5).get_attribute('label')
        assert str == '开通VIP会员'

    def test_006(self):
        str = self.LoginPage.find_ele(MyPage.chain6).get_attribute('label')
        assert str == '我的积分'

    def test_007(self):
        str = self.LoginPage.find_ele(MyPage.chain7_1).get_attribute('label')
        assert str == '播放记录'

    def test_008(self):
        str = self.LoginPage.find_ele(MyPage.chain8).get_attribute('label')
        assert str == '离线中心'

    def test_009(self):
        str = self.LoginPage.find_ele(MyPage.chain9).get_attribute('label')
        assert str == '我的看单'

    def test_010(self):
        str = self.LoginPage.find_ele(MyPage.chain10).get_attribute('label')
        assert str == '消息中心'

    def test_011(self):
        str = self.LoginPage.find_ele(MyPage.chain11).get_attribute('label')
        assert str == '帮助反馈'

    def test_012(self):
        str = self.LoginPage.find_ele(MyPage.chain12).get_attribute('label')
        assert str == '设置'

    '''''登录后个人中心'''

    def test_013(self):
        self.LoginPage.click_ele(LoginPage.chain1)
        self.LoginPage.quick_login()
        str = self.LoginPage.find_ele(MyPage.chain13).get_attribute('label')
        self.assertIn('V', str)

    def test_014(self):
        str = self.LoginPage.find_ele(MyPage.chain14).get_attribute('label')
        self.assertIn('有效期', str)

    def test_015(self):
        str = self.LoginPage.find_ele(MyPage.chain7_1).get_attribute('label')
        assert str == '播放记录'

    def test_016(self):
        str = self.LoginPage.find_ele(MyPage.chain8).get_attribute('label')
        assert str == '离线中心'

    def test_017(self):
        str = self.LoginPage.find_ele(MyPage.chain9).get_attribute('label')
        assert str == '我的看单'

    def test_018(self):
        str = self.LoginPage.find_ele(MyPage.chain10).get_attribute('label')
        assert str == '消息中心'

    def test_019(self):
        driver = self.driver
        driver.tap([(91,228)],1000)
        time.sleep(3)
        str = self.LoginPage.find_ele(MyPage.chain15).get_attribute('label')
        assert str == '会员中心'

    def test_020(self):
        str = self.LoginPage.find_ele(MyPage.chain16).get_attribute('label')
        assert str == '立即续费'

    def test_021(self):
        str = self.LoginPage.find_ele(MyPage.chain17).get_attribute('label')
        self.assertIn('观影券', str)

    def test_022(self):
        str = self.LoginPage.find_ele(MyPage.chain18).get_attribute('label')
        self.assertIn('交易记录', str)

    def test_023(self):
        str = self.LoginPage.find_ele(MyPage.chain20).get_attribute('label')
        assert str == '详情'

    def test_024(self):
        driver = self.driver
        #self.LoginPage.click_ele(MyPage.chain20)
        driver.tap([(1060, 143)], 10)
        time.sleep(3)
        str = self.LoginPage.find_ele(MyPage.chain21).get_attribute('label')
        assert str == '会员有效期详情'
        self.LoginPage.click_ele(MyPage.chain22)
        time.sleep(3)

    def test_025(self):
        self.LoginPage.click_ele(MyPage.chain17)
        time.sleep(3)
        str = self.LoginPage.find_ele(MyPage.chain23).get_attribute('label')
        assert str == '观影券'
        self.LoginPage.click_ele(MyPage.back)
        time.sleep(3)

    def test_026(self):
        self.LoginPage.click_ele(MyPage.chain18)
        time.sleep(3)
        str = self.LoginPage.find_ele(MyPage.chain25).get_attribute('label')
        assert str == '交易记录'
        self.LoginPage.click_ele(MyPage.back)
        time.sleep(3)

    def test_027(self):
        self.LoginPage.click_ele(MyPage.chain26)
        str = self.LoginPage.find_ele(MyPage.chain27).get_attribute('label')
        assert str == '帮助反馈'
        self.LoginPage.click_ele(MyPage.back)

    def test_028(self):
        #关闭会员中心页面
        self.LoginPage.click_ele(MyPage.close)

    def test_029(self):
        self.LoginPage.click_ele(MyPage.chain6)
        str = self.LoginPage.find_ele(MyPage.chain29).get_attribute('label')
        assert str == '积分中心'

    def test_030(self):
        str = self.LoginPage.find_ele(MyPage.chain30).get_attribute('label')
        self.assertIn('积分明细', str)

    def test_031(self):
        #关闭积分中心页面
        self.LoginPage.click_ele(MyPage.close)
        time.sleep(10)

    def test_032(self):
        # 展开播放记录页面
        driver = self.driver
        driver.find_element_by_xpath(JingxuanPage.chain18).click()
        time.sleep(10)
        self.LoginPage.click_ele(MyPage.chain7_2)
        str = self.LoginPage.find_ele(MyPage.chain32).get_attribute('label')
        assert str == '播放记录'

    def test_033(self):
        # 编辑按钮
        str = self.LoginPage.find_ele(MyPage.chain33).get_attribute('label')
        assert str == '编辑'

    def test_034(self):
        # 过滤短视频
        str = self.LoginPage.find_ele(MyPage.chain34).get_attribute('label')
        assert str == '过滤短视频'

    def test_035(self):
        # 开启过滤短视频，再关闭过滤短视频
        self.LoginPage.click_ele(MyPage.chain35)
        self.LoginPage.click_ele(MyPage.chain40)
        str = self.LoginPage.find_ele(MyPage.chain35).get_attribute('value')
        assert str == '0'

    def test_036(self):
        # 点击编辑按钮，展示删除
        self.LoginPage.click_ele(MyPage.chain33)
        str = self.LoginPage.find_ele(MyPage.chain36).get_attribute('label')
        assert str == '删除'

    def test_037(self):
        # 点击编辑按钮，展示全选
        str = self.LoginPage.find_ele(MyPage.chain37).get_attribute('label')
        assert str == '全选'

    def test_038(self):
        # 点击编辑按钮，展示取消
        str = self.LoginPage.find_ele(MyPage.chain38).get_attribute('label')
        assert str == '取消'

    def test_039(self):
        # 点击全选，取消全选
        self.LoginPage.click_ele(MyPage.chain37)
        assert self.LoginPage.find_ele(MyPage.chain39).get_attribute('label') == '取消全选'
        self.LoginPage.click_ele(MyPage.chain39)
        assert self.LoginPage.find_ele(MyPage.chain37).get_attribute('label') == '全选'

    def test_040(self):
        # 勾选播放记录，成功删除
        self.MyPage.click_ele_xpath(MyPage.xpath41)
        self.MyPage.click_ele(MyPage.chain36)


    def test_041(self):
        # 勾选播放记录，取消删除
        self.MyPage.click_ele_xpath(MyPage.xpath41)
        self.MyPage.click_ele_xpath(MyPage.xpath41)

    def test_042(self):
        # 取消编辑
        self.MyPage.click_ele(MyPage.chain38)
        str = self.MyPage.find_ele(MyPage.chain33).get_attribute('label')
        assert str == '编辑'

    def test_043(self):
        # 退出播放记录页面
        self.MyPage.click_ele(MyPage.close)
        str = self.MyPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'

    def test_044(self):
        # 进入离线中心
        self.MyPage.click_ele_point(MyPage.chain8)
        str = self.MyPage.find_ele(MyPage.chain43).get_attribute('label')
        print(str)
        assert str == '离线缓存'
        time.sleep(3)

    def test_045(self):
        # 离线中心,当前可用内存
        str = self.MyPage.find_ele_xpath(MyPage.xpath46).get_attribute('label')
        self.assertIn('当前可用', str)
        time.sleep(3)

    def test_046(self):
        # 离线中心全部开始
        str = self.MyPage.find_ele(MyPage.chain44).get_attribute('label')
        assert str == '全部开始'
        time.sleep(3)

    def test_047(self):
        # 离线中心删除
        str = self.MyPage.find_ele(MyPage.chain45).get_attribute('label')
        assert str == '删除'
        time.sleep(3)

    def test_048(self):
        # 退出离线中心页面
        self.MyPage.click_ele(MyPage.vod_close)
        str = self.MyPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'
        time.sleep(3)

    def test_049(self):
        # 进入我的看单
        self.driver.swipe(100, 300, 100, 100,1000)
        self.MyPage.click_ele(MyPage.chain9)
        str = self.MyPage.find_ele(MyPage.chain47).get_attribute('label')
        assert str == '我的看单'
        time.sleep(3)

    def test_050(self):
        # 我的看单 编辑
        str = self.MyPage.find_ele(MyPage.chain48).get_attribute('label')
        assert str == '编辑'
        time.sleep(3)

    def test_051(self):
        # 我的看单 节目
        str = self.MyPage.find_ele(MyPage.chain49).get_attribute('label')
        assert str == '节目'

    def test_052(self):
        # 我的看单 视频
        str = self.MyPage.find_ele(MyPage.chain50).get_attribute('label')
        assert str == '视频'
        time.sleep(3)

    def test_053(self):
        # 退出我的看单
        self.MyPage.click_ele(MyPage.close)
        str = self.MyPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'
        time.sleep(3)

    def test_054(self):
        # 进入消息中心
        self.MyPage.click_ele(MyPage.chain10)
        str = self.MyPage.find_ele(MyPage.chain51).get_attribute('label')
        assert str == '消息中心'

    def test_055(self):
        # 退出消息中心
        self.MyPage.click_ele(MyPage.close)
        str = self.MyPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'
        time.sleep(3)

    def test_056(self):
        self.driver.swipe(100, 300, 100, 100, 1000)
        time.sleep(3)
        str = self.LoginPage.find_ele(MyPage.chain11).get_attribute('label')
        assert str == '帮助反馈'
        time.sleep(3)

    def test_057(self):
        driver = self.driver
        str = self.LoginPage.find_ele(MyPage.chain12).get_attribute('label')
        assert str == '设置'
        time.sleep(3)

    def test_058(self):
        # 进入帮助反馈页
        self.MyPage.click_ele(MyPage.chain11)
        str = self.MyPage.find_ele(MyPage.chain52).get_attribute('label')
        assert str == '帮助反馈'

    def  test_059(self):
        #  退出帮助反馈页
        self.MyPage.click_ele(MyPage.close)
        str = self.MyPage.find_ele(MyPage.chain1).get_attribute('label')
        assert str == '个人中心'

    def test_060(self):
        # 进入设置页
        self.MyPage.click_ele(MyPage.chain12)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_061(self):
        # 修改密码
        str = self.MyPage.find_ele(MyPage.chain54).get_attribute('label')
        assert str == '修改密码'

    def test_062(self):
        # 进入设置 修改密码页面
        self.MyPage.click_ele(MyPage.chain54)
        str = self.MyPage.find_ele(MyPage.chain76).get_attribute('label')
        assert str == '修改密码'

    def test_063(self):
        # 修改密码页面密码限制
        self.MyPage.click_ele(MyPage.chain54)
        str = self.MyPage.find_ele(MyPage.chain77).get_attribute('label')
        assert str == '密码为8-20位，且必须包含大小写字母，数字及符号'

    def test_064(self):
        # 退出修改密码页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_065(self):
        # 绑定号码
        str = self.MyPage.find_ele(MyPage.chain55).get_attribute('label')
        assert str == '绑定号码'

    def test_066(self):
        # 进入设置 绑定号码页面
        self.MyPage.click_ele(MyPage.chain55)
        str = self.MyPage.find_ele(MyPage.chain78).get_attribute('label')
        assert str == '验证手机'

    def test_067(self):
        # 退出号码绑定页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_068(self):
        # 青少年模式
        str = self.MyPage.find_ele(MyPage.chain56).get_attribute('label')
        assert str == '青少年模式'

    def test_069(self):
        # 进入青少年模式开启页面
        self.MyPage.click_ele(MyPage.chain56)
        str = self.MyPage.find_ele(MyPage.chain81).get_attribute('label')
        assert str == '青少年模式'

    def test_070(self):
        # 青少年模式状态
        str = self.MyPage.find_ele(MyPage.chain79).get_attribute('label')
        assert str == '青少年模式未开启'

    def test_071(self):
        # 青少年模式开启按钮
        str = self.MyPage.find_ele(MyPage.chain80).get_attribute('label')
        assert str == '开启青少年模式'

    def test_072(self):
        # 退出青少年页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'
        time.sleep(3)

    def test_073(self):
        # 账号注销
        str = self.MyPage.find_ele(MyPage.chain57).get_attribute('label')
        assert str == '账号注销'

    def test_074(self):
        # 进入设置 账号注销页面
        self.MyPage.click_ele(MyPage.chain57)
        str = self.MyPage.find_ele(MyPage.chain82).get_attribute('label')
        assert str == '账号注销协议'
        time.sleep(3)

    def test_075(self):
        # 确认注销协议
        str = self.MyPage.find_ele(MyPage.chain84).get_attribute('label')
        assert str == '我已阅读注销协议'

    def test_076(self):
        # 确认注销按钮
        str = self.MyPage.find_ele(MyPage.chain83).get_attribute('label')
        assert str == '确认注销'

    def test_077(self):
        # 退出账号注销页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_078(self):
        # 非wifi网络下播放提醒
        str = self.MyPage.find_ele(MyPage.chain58).get_attribute('label')
        assert str == '非wifi网络下播放提醒'

    def test_079(self):
        # 非wifi网络下播放提醒默认开启
        str = self.MyPage.find_ele(MyPage.chain59).get_attribute('value')
        assert str == '1'

    def test_080(self):
        # 非wifi网络下播放提醒关闭
        self.MyPage.click_ele(MyPage.chain59)
        str = self.MyPage.find_ele(MyPage.chain59).get_attribute('value')
        assert str == '0'

    def test_081(self):
        # 非wifi网络下播放提醒关闭后开启
        self.MyPage.click_ele(MyPage.chain59)
        str = self.MyPage.find_ele(MyPage.chain59).get_attribute('value')
        assert str == '1'


    def test_082(self):
        # 非wifi网络下离线缓存
        str = self.MyPage.find_ele(MyPage.chain60).get_attribute('label')
        assert str == '非wifi网络下离线缓存'
        time.sleep(3)

    def test_083(self):
        # 非wifi网络下离线缓存默认关闭
        str = self.MyPage.find_ele(MyPage.chain61).get_attribute('value')
        assert str == '0'


    def test_084(self):
        # 非wifi网络下播放提醒开启
        self.MyPage.click_ele(MyPage.chain61)
        str = self.MyPage.find_ele(MyPage.chain61).get_attribute('value')
        assert str == '1'


    def test_085(self):
        # 非wifi网络下播放提醒开启后关闭
        self.MyPage.click_ele(MyPage.chain61)
        str = self.MyPage.find_ele(MyPage.chain61).get_attribute('value')
        assert str == '0'


    def test_086(self):
        # 自动跳过片头片尾
        str = self.MyPage.find_ele(MyPage.chain62).get_attribute('label')
        assert str == '自动跳过片头片尾'


    def test_087(self):
        # 自动跳过片头片尾默认关闭
        str = self.MyPage.find_ele(MyPage.chain63).get_attribute('value')
        assert str == '0'

    def test_088(self):
        # 自动跳过片头片尾开启
        self.MyPage.click_ele(MyPage.chain63)
        str = self.MyPage.find_ele(MyPage.chain63).get_attribute('value')
        assert str == '1'

    def test_089(self):
        # 自动跳过片头片尾开启后关闭
        self.MyPage.click_ele(MyPage.chain63)
        str = self.MyPage.find_ele(MyPage.chain63).get_attribute('value')
        assert str == '0'

    def test_090(self):
        # 同步芒果TV电视端播放记录
        str = self.MyPage.find_ele(MyPage.chain64).get_attribute('label')
        assert str == '同步芒果TV电视端播放记录'

    def test_091(self):
        # 同步芒果TV电视端播放记录默认关闭
        str = self.MyPage.find_ele(MyPage.chain65).get_attribute('value')
        assert str == '1'

    def test_092(self):
        # 同步芒果TV电视端播放记录开启
        self.MyPage.click_ele(MyPage.chain65)
        str = self.MyPage.find_ele(MyPage.chain65).get_attribute('value')
        assert str == '0'

    def test_093(self):
        # 同步芒果TV电视端播放记录开启后关闭
        self.MyPage.click_ele(MyPage.chain65)
        str = self.MyPage.find_ele(MyPage.chain65).get_attribute('value')
        assert str == '1'

    def test_094(self):
        # 个人信息保护政策
        str = self.MyPage.find_ele(MyPage.chain66).get_attribute('label')
        assert str == '个人信息保护政策'

    def test_095(self):
        # 进入个人信息保护政策页面
        self.MyPage.click_ele(MyPage.chain66)
        str = self.MyPage.find_ele(MyPage.chain85).get_attribute('label')
        assert str == '个人信息保护政策'

    def test_096(self):
        # 退出个人信息保护政策页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_097(self):
        # 其他法律文件
        time.sleep(5)
        str = self.MyPage.find_ele(MyPage.chain67).get_attribute('label')
        assert str == '其他法律文件'

    def test_098(self):
        # 进入其他法律文件页面
        self.MyPage.click_ele(MyPage.chain67)
        str = self.MyPage.find_ele(MyPage.chain86).get_attribute('label')
        assert str == '其他法律文件'

    def test_099(self):
        # 其他法律页面的文件
        str = self.MyPage.find_ele(MyPage.chain87).get_attribute('label')
        assert str == '服务协议'
        time.sleep(2)
        str = self.MyPage.find_ele(MyPage.chain88).get_attribute('label')
        assert str == '历史文件'
        time.sleep(2)
        str = self.MyPage.find_ele(MyPage.chain89).get_attribute('label')
        assert str == '儿童个人信息保护政策'
        time.sleep(2)

    def test_100(self):
        # 进入服务协议
        self.MyPage.click_ele(MyPage.chain87)
        str = self.MyPage.find_ele(MyPage.chain90).get_attribute('label')
        assert str == '服务协议'

    def test_101(self):
        # 退出服务协议
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain86).get_attribute('label')
        assert str == '其他法律文件'

    def test_102(self):
        # 进入历史文件
        self.MyPage.click_ele(MyPage.chain88)
        str = self.MyPage.find_ele(MyPage.chain91).get_attribute('label')
        assert str == '历史文件'

    def test_103(self):
        # 退出历史文件
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain86).get_attribute('label')
        assert str == '其他法律文件'

    def test_104(self):
        # 进入儿童个人信息保护政策
        self.MyPage.click_ele(MyPage.chain89)
        str = self.MyPage.find_ele(MyPage.chain92).get_attribute('label')
        assert str == '儿童个人信息保护政策'

    def test_105(self):
        # 退出儿童个人信息保护政策
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain86).get_attribute('label')
        assert str == '其他法律文件'

    def test_106(self):
        # 退出其他法律文件页
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_107(self):
        # 进入隐私保护
        self.MyPage.click_ele(MyPage.chain68)
        str = self.MyPage.find_ele(MyPage.chain93).get_attribute('label')
        assert str == '隐私保护'
        time.sleep(3)

    def test_108(self):
        # 进入隐私设置
        str = self.MyPage.find_ele(MyPage.chain94).get_attribute('label')
        assert str == '隐私设置'
        self.MyPage.click_ele(MyPage.chain94)
        str = self.MyPage.find_ele(MyPage.chain96).get_attribute('label')
        assert str == '隐私设置'

    def test_109(self):
        #允许芒果TV访问位置信息
        str = self.MyPage.find_ele(MyPage.chain97).get_attribute('label')
        assert str == '允许芒果TV访问位置信息'
        str = self.LoginPage.find_ele(MyPage.chain98).get_attribute('label')
        assert str == '已开启'

    def test_110(self):
        #允许芒果TV使用相机功能
        str = self.MyPage.find_ele(MyPage.chain99).get_attribute('label')
        assert str == '允许芒果TV访问位置信息'
        str = self.LoginPage.find_ele(MyPage.chain100).get_attribute('label')
        assert str == '已开启'

    def test_111(self):
        #允许芒果TV使用相册存储和访问功能
        str = self.MyPage.find_ele(MyPage.chain101).get_attribute('label')
        assert str == '允许芒果TV使用相册存储和访问功能'
        str = self.LoginPage.find_ele(MyPage.chain102).get_attribute('label')
        assert str == '去设置'

    def test_112(self):
        #允许芒果TV使用麦克风功能
        str = self.MyPage.find_ele(MyPage.chain103).get_attribute('label')
        assert str == '允许芒果TV使用麦克风功能'
        str = self.LoginPage.find_ele(MyPage.chain104).get_attribute('label')
        assert str == '去设置'

    def test_113(self):
        #允许芒果TV使用日历功能
        str = self.MyPage.find_ele(MyPage.chain105).get_attribute('label')
        assert str == '允许芒果TV使用日历功能'
        str = self.LoginPage.find_ele(MyPage.chain106).get_attribute('label')
        assert str == '去设置'

    def test_114(self):
        #允许芒果TV向您展现个性化推荐广告
        str = self.MyPage.find_ele(MyPage.chain107).get_attribute('label')
        assert str == '允许芒果TV向您展现个性化推荐广告'
        str = self.LoginPage.find_ele(MyPage.chain108).get_attribute('value')
        assert str == '1'

    def test_115(self):
        #允许芒果TV向您展现个性化推荐视频
        str = self.MyPage.find_ele(MyPage.chain109).get_attribute('label')
        assert str == '允许芒果TV向您展现个性化推荐视频'
        str = self.LoginPage.find_ele(MyPage.chain110).get_attribute('value')
        assert str == '1'

    def test_116(self):
        #退出隐私设置页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain93).get_attribute('label')
        assert str == '隐私保护'

    def test_117(self):
        #进入隐私保护指南页面
        self.MyPage.click_ele(MyPage.chain95)
        str = self.MyPage.find_ele(MyPage.chain111).get_attribute('label')
        assert str == '隐私保护指南'

    def test_118(self):
        #退出隐私保护指南页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain93).get_attribute('label')
        assert str == '隐私保护'

    def test_119(self):
        #退出隐私保护页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_120(self):
        # 进入常见问题页面
        self.MyPage.click_ele(MyPage.chain69)
        str = self.MyPage.find_ele(MyPage.chain52).get_attribute('label')
        assert str == '帮助反馈'

    def test_121(self):
        #退出常见问题页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    # def test_122(self):
    #     #清理缓存
    #     self.MyPage.click_ele(MyPage.chain70)
    #     str = self.MyPage.find_ele(MyPage.chain112).get_attribute('label')
    #     assert str == '清理成功'
    #
    # def test_123(self):
    #     #关闭清除成功toast
    #     self.MyPage.click_ele(MyPage.chain113)
    #     str = self.MyPage.find_ele(MyPage.chain71).get_attribute('value')
    #     assert str == '0.00M'

    def test_124(self):
        #当前版本
        str = self.MyPage.find_ele(MyPage.chain72).get_attribute('label')
        assert str == '当前版本'

    def test_125(self):
        #给我好评
        str = self.MyPage.find_ele(MyPage.chain73).get_attribute('label')
        assert str == '给我好评'

    def test_126(self):
        #关于我们
        str = self.MyPage.find_ele(MyPage.chain74).get_attribute('label')
        assert str == '关于我们'

    def test_127(self):
        #进入于我们页面
        self.MyPage.click_ele(MyPage.chain74)
        str = self.MyPage.find_ele(MyPage.chain114).get_attribute('label')
        assert str == '关于我们'
        time.sleep(3)

    def test_128(self):
        #退出关于我们页面
        self.MyPage.click_ele(MyPage.back)
        str = self.MyPage.find_ele(MyPage.chain53).get_attribute('label')
        assert str == '设置'

    def test_129(self):
        #退出设置页面,回到个人中心
        self.MyPage.click_ele(MyPage.close)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(wo_test())


