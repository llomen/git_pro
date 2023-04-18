"""
IPAD自动化测试
肖子淅
日期：2022年07月25日
"""

from page.BasePage import BasePage

class PindaoPage(BasePage):
    # 精选频道
    chain1 = '**/XCUIElementTypeStaticText[`label == "精选"`]'

    # 综艺频道
    chain2 = '**/XCUIElementTypeStaticText[`label == "综艺"`]'

    # 电视剧频道
    chain3 = '**/XCUIElementTypeStaticText[`label == "电视剧"`]'

    # 电影频道
    chain4 = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[4]/XCUIElementTypeOther'

    # 少儿频道
    #chain5 = '**/XCUIElementTypeStaticText[`label == "少儿"`]'
    chain5 = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[5]/XCUIElementTypeOther'


    # 动漫频道
    chain6 = '**/XCUIElementTypeStaticText[`label == "动漫"`]'

    # 大芒频道
    #chain7 = '**/XCUIElementTypeStaticText[`label == "大芒"`]'
    chain7 = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[1]/XCUIElementTypeOther[2]/XCUIElementTypeCollectionView/XCUIElementTypeCell[7]/XCUIElementTypeOther'

    # 新闻频道
    chain8 = '**/XCUIElementTypeStaticText[`label == "新闻"`]'

    # 音乐频道
    chain9 = '**/XCUIElementTypeStaticText[`label == "音乐"`]'

    # 游戏频道
    chain10 = '**/XCUIElementTypeStaticText[`label == "游戏"`]'

    # 娱乐频道
    chain11 = '**/XCUIElementTypeStaticText[`label == "娱乐"`]'

    # 生活频道
    chain12 = '**/XCUIElementTypeStaticText[`label == "生活"`]'

    # 教育频道
    chain13 = '**/XCUIElementTypeStaticText[`label == "教育"`]'

    # 投教频道
    chain14 = '**/XCUIElementTypeStaticText[`label == "投教"`]'

    # 纪录片频道
    chain15 = '**/XCUIElementTypeStaticText[`label == "纪录片"`]'

    # 时尚频道
    chain16 = '**/XCUIElementTypeStaticText[`label == "时尚"`]'

    # 直播频道
    chain17 = '**/XCUIElementTypeStaticText[`label == "直播"`]'

    #精选频道页 女儿们的恋爱4
    chain18 = '**/XCUIElementTypeStaticText[`label == "女儿们的恋爱4"`]'

    #综艺频道 爸爸当家
    chain19 = '**/XCUIElementTypeStaticText[`label == "吴敏霞支持张效诚育儿方式"`]'

    #电视剧频道 好好说话
    chain20 = '**/XCUIElementTypeStaticText[`label == "好好说话 "`]'

    #电影频道 长津湖之水门桥
    chain21 = '**/XCUIElementTypeStaticText[`label == "长津湖之水门桥"`][2]'

    #少儿频道 汪汪队立大功 第八季
    chain22 = '**/XCUIElementTypeStaticText[`label == "汪汪队立大功 第八季"`]'

    #动漫频道 郡主稳住，人设不能崩
    chain23 = '**/XCUIElementTypeStaticText[`label == "郡主稳住，人设不能崩"`]'

    #大芒频道 大芒星歌汇
    chain24 = '**/XCUIElementTypeStaticText[`label == "大芒星歌汇"`]'

    #新闻频道 中国外交部：七国集团不要以“家法帮规”霸凌他国
    chain25 = '**/XCUIElementTypeStaticText[`label == "中国外交部：七国集团不要以“家法帮规”霸凌他国"`]'

    #音乐频道 A-Lin《挚友》MV
    chain26 = '**/XCUIElementTypeStaticText[`label == "A-Lin《挚友》MV"`]'

    #游戏频道 我的世界：魔法大陆和虚无世界
    chain27 = '**/XCUIElementTypeStaticText[`label == "我的世界：魔法大陆和虚无世界"`]'