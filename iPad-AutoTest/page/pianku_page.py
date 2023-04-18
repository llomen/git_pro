"""
IPAD自动化测试
肖子淅
日期：2022年05月11日
片库页对应元素地址
"""
import time

from page.BasePage import BasePage


#片库
class PiankuPage(BasePage):
    #精选页上片库入口按钮
    chain1 = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[3]/XCUIElementTypeCollectionView/XCUIElementTypeCell[2]/XCUIElementTypeOther'
    #片库title
    chain2 = '**/XCUIElementTypeStaticText[`label == "片库"`]'
    #综艺
    chain3 = '**/XCUIElementTypeStaticText[`label == "综艺"`]'
    #电视剧
    chain4 = '**/XCUIElementTypeStaticText[`label == "电视剧"`]'
    chain4_2 = '**/XCUIElementTypeCell[$label == "电视剧"$]/XCUIElementTypeOther[1]'
    #电影
    chain5 = '**/XCUIElementTypeStaticText[`label == "电影"`]'
    chain5_2 = '**/XCUIElementTypeCell[$label == "电影"$]/XCUIElementTypeOther[1]'
    #动漫
    chain6 = '**/XCUIElementTypeStaticText[`label == "动漫"`]'
    chain6_2 = '**/XCUIElementTypeCell[$label == "动漫"$]/XCUIElementTypeOther[1]'
    #少儿
    chain7 = '**/XCUIElementTypeStaticText[`label == "少儿"`]'
    chain7_2 = '**/XCUIElementTypeCell[$label == "少儿"$]/XCUIElementTypeOther[1]'
    #纪录片
    chain8 = '**/XCUIElementTypeStaticText[`label == "纪录片"`]'
    chain8_2 = '**/XCUIElementTypeCell[$label == "纪录片"$]/XCUIElementTypeOther[1]'
    #新闻
    chain9 = '**/XCUIElementTypeStaticText[`label == "新闻"`]'
    chain9_2 = '**/XCUIElementTypeCell[$label == "新闻"$]/XCUIElementTypeOther[1]'
    #音乐
    chain10 = '**/XCUIElementTypeStaticText[`label == "音乐"`]'
    chain10_2 = '**/XCUIElementTypeCell[$label == "音乐"$]/XCUIElementTypeOther[1]'
    #乐活
    chain11 = '**/XCUIElementTypeStaticText[`label == "乐活"`]'
    chain11_2 = '**/XCUIElementTypeCell[$label == "乐活"$]/XCUIElementTypeOther[1]'
    #游戏
    chain12 = '**/XCUIElementTypeStaticText[`label == "游戏"`]'
    chain12_2 = '**/XCUIElementTypeCell[$label == "游戏"$]/XCUIElementTypeOther[1]'
    #体育
    chain13 = '**/XCUIElementTypeStaticText[`label == "体育"`]'
    chain13_2 = '**/XCUIElementTypeCell[$label == "体育"$]/XCUIElementTypeOther[1]'
    #教育
    chain14 = '**/XCUIElementTypeStaticText[`label == "教育"`]'
    chain14_2 = '**/XCUIElementTypeCell[$label == "教育"$]/XCUIElementTypeOther[1]'
    #原创
    chain15 = '**/XCUIElementTypeStaticText[`label == "原创"`]'
    chain15_2 = '**/XCUIElementTypeCell[$label == "原创"$]/XCUIElementTypeOther[1]'
    #娱乐
    chain16 = '**/XCUIElementTypeStaticText[`label == "娱乐"`]'
    chain16_2 = '**/XCUIElementTypeCell[$label == "娱乐"$]/XCUIElementTypeOther[1]'
    #综艺第一部媒资
    chain17 = '**/XCUIElementTypeStaticText[`label == "大侦探 第七季"`]'
    #电视剧第一部媒资
    chain18 = '**/XCUIElementTypeStaticText[`label == "尚食"`]'
    #电影第一部媒资
    chain19 = '**/XCUIElementTypeStaticText[`label == "这个杀手不太冷静"`]'
    #动漫/少儿第一部媒资
    chain20 = '**/XCUIElementTypeStaticText[`label == "宝贝赳赳 第三季"`]'
    #纪录片第一部媒资
    chain21 = '**/XCUIElementTypeStaticText[`label == "中国 第二季"`]'
    #新闻第一部媒资
    chain22 = '**/XCUIElementTypeStaticText[`label == "焦点时刻 2022"`]'
    #音乐第一部媒资
    chain23 = '**/XCUIElementTypeStaticText[`label == "【王俊凯】四面楚歌"`]'
    #乐活第一部媒资
    chain24 = '**/XCUIElementTypeStaticText[`label == "燃烧吧，卡路里 2022"`]'
    #游戏第一部媒资
    chain25 = '**/XCUIElementTypeStaticText[`label == "糖果植物大战僵尸 植物组合冒险模式"`]'
    #体育第一部媒资
    chain26 = '**/XCUIElementTypeStaticText[`label == "王者之战 2016"`]'
    #教育第一部媒资
    chain27 = '**/XCUIElementTypeStaticText[`label == "“防溺水”湖南省中小学专题课"`]'
    #原创第一部媒资
    chain28 = '**/XCUIElementTypeStaticText[`label == "嘴巴都笑裂了 2019"`]'
    #娱乐第一部媒资
    chain29 = '**/XCUIElementTypeStaticText[`label == "爱豆传送门 2020"`]'
    #退出点播页按钮
    chain30 = '**/XCUIElementTypeButton[`label == "player back icon"`]'
    #点播页媒资名称
    chain31 = '**/XCUIElementTypeStaticText[`label == "大侦探 第七季"`][1]'
    #点播页媒资名称
    chain32 = '**/XCUIElementTypeStaticText[`label == "尚食"`][1]'
    #点播页媒资名称
    chain33 = '**/XCUIElementTypeStaticText[`label == "这个杀手不太冷静"`][1]'
    #点播页媒资名称
    chain34 = '**/XCUIElementTypeStaticText[`label == "宝贝赳赳 第三季"`][1]'
    #点播页媒资名称
    chain35 = '**/XCUIElementTypeStaticText[`label == "中国 第二季"`][1]'
    #点播页媒资名称
    chain36 = '**/XCUIElementTypeStaticText[`label == "焦点时刻 2022"`][1]'
    #点播页媒资名称
    chain37 = '**/XCUIElementTypeStaticText[`label == "【王俊凯】四面楚歌"`][1]'
    #点播页媒资名称
    chain38 = '**/XCUIElementTypeStaticText[`label == "燃烧吧，卡路里 2022"`][1]'
    #点播页媒资名称
    chain39 = '**/XCUIElementTypeStaticText[`label == "糖果植物大战僵尸 植物组合冒险模式"`][1]'
    #点播页媒资名称
    chain40 = '**/XCUIElementTypeStaticText[`label == "王者之战 2016"`][1]'
    #点播页媒资名称
    chain41 = '**/XCUIElementTypeStaticText[`label == "“防溺水”湖南省中小学专题课"`]'
    #点播页媒资名称
    chain42 = '**/XCUIElementTypeStaticText[`label == "嘴巴都笑裂了 2019"`][1]'
    #点播页媒资名称
    chain43 = '**/XCUIElementTypeStaticText[`label == "爱豆传送门 2020"`]'
    #片库返回按钮
    back = '**/XCUIElementTypeButton[`label == "返回"`]'



    def to_pianku(self):
        time.sleep(5)
        self.click_ele(self.chain1)

