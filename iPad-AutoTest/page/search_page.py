"""
IPAD自动化测试
肖子淅
日期：2022年05月11日
搜索页
"""
from page.BasePage import BasePage
import time


#片库
class SearchuPage(BasePage):
    #搜索入口
    chain1 = '**/XCUIElementTypeOther[$label == "search_textField"$]'
    xpath1 = '//XCUIElementTypeTextField[@name="search_textField"]/parent::XCUIElementTypeOther'
    #搜索页面取消按钮
    chain2 = '**/XCUIElementTypeButton[`label == "取消"`]'
    #热搜榜单title
    chain3 = '**/XCUIElementTypeStaticText[`label == "热搜榜单"`]'
    #热搜榜单 综合
    chain4 = '**/XCUIElementTypeStaticText[`label == "综合"`]'
    #热搜榜单 综艺
    chain5 = '**/XCUIElementTypeStaticText[`label == "综艺"`]'
    #热搜榜单 电视剧
    chain6 = '**/XCUIElementTypeStaticText[`label == "电视剧"`]'
    #热搜榜单 综合
    chain7 = '**/XCUIElementTypeStaticText[`label == "电影"`]'
    #热搜榜单 动漫
    chain8 = '**/XCUIElementTypeStaticText[`label == "动漫"`]'
    #搜索历史
    chain9 = '**/XCUIElementTypeStaticText[`label == "搜索历史"`]'
    #搜索推荐
    chain10 = '**/XCUIElementTypeStaticText[`label == "搜索推荐"`]'
    #搜索输入框
    chain11 = '**/XCUIElementTypeTextField[`label == "searchTextField"`]'
    #搜索结果页取消按钮
    chain12 = '**/XCUIElementTypeStaticText[`label == "取消"`]'
    #搜索结果页关闭搜索结果按钮
    chain13 = '**/XCUIElementTypeButton[`label == "close"`]'
    #搜索历史第一条
    chain14 = '**/XCUIElementTypeStaticText[`label == "hhhh"`]'
    #搜索联想页第一条
    chain15 = '**/XCUIElementTypeStaticText[`label == "哈哈哈哈哈"`]'
    #搜索联想页第二条
    chain16 = '**/XCUIElementTypeStaticText[`label == "哈哈哈哈哈第2季"`]'
    #搜索联想页第三条
    chain17 = '**/XCUIElementTypeStaticText[`label == "花红花火"`]'
    #搜索结果页纠正后的搜索结果
    chain18 = '**/XCUIElementTypeStaticText[`label == "花红花火"`]'
    #搜索结果页高级筛选
    chain19 = '**/XCUIElementTypeStaticText[`label == "高级筛选 "`]'
    #搜索结果页相关搜索
    chain20 = '**/XCUIElementTypeStaticText[`label == "相关搜索"`]'
    #搜索结果页热门搜索
    chain21 = '**/XCUIElementTypeStaticText[`label == "热门搜索"`]'
    #搜索结果页高级筛选中时长
    chain22 = '**/XCUIElementTypeStaticText[`label == "时长"`]'
    #搜索结果页高级筛选中发布时间
    chain23 = '**/XCUIElementTypeStaticText[`label == "发布时间"`]'
    #搜索结果页高级筛选中排序
    chain24 = '**/XCUIElementTypeStaticText[`label == "排序"`]'
    #搜索结果页播放按钮
    chain25 = '**/XCUIElementTypeButton[`label == "播放"`][1]'
    xpath25 = '//XCUIElementTypeButton[@name=" 播放"][1]'
    #点播媒资名称
    chain26 = '**/XCUIElementTypeStaticText[`label == "向往的生活 第六季"`]'
    #点播页退出
    back = '**/XCUIElementTypeButton[`label == "player back icon"`]'
    #结果搜索页相关搜索明星大侦探
    chain27 = '**/XCUIElementTypeStaticText[`label == "明星大侦探 第六季"`]'
    #点播页媒资名称
    chain28 = '**/XCUIElementTypeStaticText[`label == "明星大侦探 第六季"`]'
    #搜索结果页热门搜索第一部媒资
    chain29 = '**/XCUIElementTypeStaticText[`label == "向往的生活 第六季"`][3]'



    def tap_point(self):
        #搜索结果页播放按钮
        self.driver.tap([(198, 346)], 10)
        time.sleep(10)