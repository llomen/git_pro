"""
IPAD自动化测试
肖子淅
日期：2022年07月25日
"""
from page.BasePage import BasePage

class DianboPage(BasePage):
    # 点播返回按钮
    chain1 = '**/XCUIElementTypeButton[`label == "player back icon"`]'
    # 点播媒资名称1
    chain2 = '**/XCUIElementTypeStaticText[`label == "女儿们的恋爱 第四季"`][1]'
    # 点播媒资名称2
    chain3 = '**/XCUIElementTypeStaticText[`label == "爸爸当家"`][1]'
    # 点播媒资名称3
    chain4 = '**/XCUIElementTypeStaticText[`label == "好好说话"`][1]'
    # 点播媒资名称4
    chain5 = '**/XCUIElementTypeStaticText[`label == "长津湖之水门桥"`][1]'
    # 点播媒资名称5
    chain6 = '**/XCUIElementTypeStaticText[`label == "汪汪队立大功 第八季"`][1]'
    # 点播媒资名称6
    chain7 = '**/XCUIElementTypeStaticText[`label == "郡主稳住，人设不能崩"`][1]'
    # 点播媒资名称7
    chain8 = '**/XCUIElementTypeStaticText[`label == "大芒星歌汇"`][1]'
    # 点播媒资名称7
    chain9 = '**/XCUIElementTypeStaticText[`label == "中国外交部：七国集团不要以“家法帮规”霸凌他国"`][1]'
    # 点播媒资名称9
    chain10 = '**/XCUIElementTypeStaticText[`label == "A-Lin《挚友》MV"`][1]'
    # 点播媒资名称10
    chain11 = '**/XCUIElementTypeStaticText[`label == "我的世界：魔法大陆和虚无世界"`][1]'


