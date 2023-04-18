"""
IPAD自动化测试
肖子淅
日期：2022年04月26日
"""
from page.BasePage import BasePage


#个人中心
class JingxuanPage(BasePage):

    #芒果TV角标
    chain = '**/XCUIElementTypeButton[`label == "ChannelLogoIcon"`]'

    #精选频道
    chain1 = '**/XCUIElementTypeStaticText[`label == "精选"`]'

    #综艺频道
    chain2 = '**/XCUIElementTypeStaticText[`label == "综艺"`]'

    #电视剧频道
    chain3 = '**/XCUIElementTypeStaticText[`label == "电视剧"`]'

    #电影频道
    chain4 = '**/XCUIElementTypeStaticText[`label == "电影"`]'

    #少儿频道
    chain5 = '**/XCUIElementTypeStaticText[`label == "少儿"`]'

    #动漫频道
    chain6 = '**/XCUIElementTypeStaticText[`label == "动漫"`]'

    #大芒频道
    chain7 = '**/XCUIElementTypeStaticText[`label == "大芒"`]'

    #新闻频道
    chain8 = '**/XCUIElementTypeStaticText[`label == "新闻"`]'

    #音乐频道
    chain9 = '**/XCUIElementTypeStaticText[`label == "音乐"`]'

    #片库
    chain10 = '**/XCUIElementTypeStaticText[`label == "片库"`]'

    #猜你在追
    chain11 = '**/XCUIElementTypeStaticText[`label == "猜你在追"`]'

    #猜你在追更多
    chain12 = '**/XCUIElementTypeStaticText[`label == "更多"`]'

    #当季热播
    chain13 = '**/XCUIElementTypeStaticText[`label == "当季热播"`]'

    #首页tab
    chain14 = '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[1]'

    #大芒tab
    chain15 = '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[2]'

    #会员tab
    chain16 = '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[3]'

    #一起看tab
    chain17 = '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[4]'

    #我的tab
    chain18 = '//XCUIElementTypeTabBar[@name="标签栏"]/XCUIElementTypeButton[5]'

    #大芒短视频
    chain19 = '**/XCUIElementTypeStaticText[`label == "大芒短视频"`]'

    #即将上线
    chain20 = '**/XCUIElementTypeStaticText[`label == "即将上线"`]'

    #预约
    chain21 = '**/XCUIElementTypeButton[`label == "预约"`][1]'

    #我的预约
    chain22 = '**/XCUIElementTypeStaticText[`label == "我的预约"`]'

    #即将上线
    chain23 = '**/XCUIElementTypeStaticText[`label == "即将上线"`][1]'

    #猜你喜欢
    chain24 = '**/XCUIElementTypeStaticText[`label == "猜你喜欢"`]'

