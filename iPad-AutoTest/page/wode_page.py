"""
IPAD自动化测试
肖子淅
日期：2022年04月26日
"""
from page.BasePage import BasePage


#个人中心
class MyPage(BasePage):
    chain1 = '**/XCUIElementTypeStaticText[`label == "个人中心"`]'

    #登录/注册
    chain2 = '**/XCUIElementTypeButton[`label == "登录/注册"`]'

    #领15天会员气泡
    chain3 = '**/XCUIElementTypeButton[`label == "领15天会员"`]'

    #签到领会员
    chain4 = '**/XCUIElementTypeButton[`label == "签到领会员"`]'

    #开通VIP会员
    chain5 = '**/XCUIElementTypeStaticText[`label == "开通VIP会员"`]'

    #我的积分
    chain6 = '**/XCUIElementTypeStaticText[`label == "我的积分"`]'

    #播放记录
    chain7_1 = '**/XCUIElementTypeStaticText[`label == "播放记录"`]'   #播放记录文本
    chain7_2 = '**/XCUIElementTypeCell[$label == "播放记录"$]/XCUIElementTypeButton[1]'   #播放记录按钮，点击  找父节点，然后往下找兄弟节点
    xpath7 = '//XCUIElementTypeStaticText[@name="播放记录"]/following-sibling::XCUIElementTypeButton[1]'

    #离线中心
    chain8 = '**/XCUIElementTypeStaticText[`label == "离线中心"`]'

    #我的看单
    chain9 = '**/XCUIElementTypeStaticText[`label == "我的看单"`]'

    #消息中心
    chain10 = '**/XCUIElementTypeStaticText[`label == "消息中心"`]'

    #帮助反馈
    chain11 = '**/XCUIElementTypeStaticText[`label == "帮助反馈"`]'

    #设置
    chain12 = '**/XCUIElementTypeStaticText[`label == "设置"`]'

    #VIP会员
    chain19 = '**/**[`label == "VIP会员"`]'

    #会员等级标签
    chain13 = '**/XCUIElementTypeStaticText[`label == "V9"`]'

    #会员有效期
    chain14 = '**/XCUIElementTypeStaticText[`label == "有效期:2037-09-20"`]'

    #会员中心
    chain15 = '**/XCUIElementTypeStaticText[`label == "会员中心"`]'

    #立即续费按钮
    chain16 = '**/XCUIElementTypeStaticText[`label == "立即续费"`]'

    #观影券
    chain17 = '**/XCUIElementTypeLink[`label == " 观影券"`]'

    #交易记录
    chain18 = '**/XCUIElementTypeLink[`label == " 交易记录"`]'

    #会员详情
    chain20 = '**/XCUIElementTypeStaticText[`label == "详情"`]'

    #会员有效期详情
    chain21 = '**/XCUIElementTypeStaticText[`label == "会员有效期详情"`]'

    #会员有效期详情页关闭按钮
    chain22 = '**/XCUIElementTypeOther[`label == "会员中心"`]/XCUIElementTypeOther[13]/XCUIElementTypeOther'

    #观影券页面-观影券title
    chain23 = '**/XCUIElementTypeOther[`label == "观影券"`]'

    #观影券页面关闭按钮
    back = '**/XCUIElementTypeButton[`label == "back icon"`]'

    #交易记录详情页title
    chain25 = '**/XCUIElementTypeStaticText[`label == "交易记录"`]'

    #会员中心帮助反馈
    chain26 = '**/XCUIElementTypeStaticText[`label == "帮助反馈"`]'

    #会员中帮助反馈页面-帮助反馈title
    chain27 = '**/XCUIElementTypeStaticText[`label == "帮助反馈"`]'

    #会员中心页关闭按钮
    close = '**/XCUIElementTypeButton[`label == "cancel phoneBind"`]'

    vod_close = '**/XCUIElementTypeButton[`label == "vod close"`]'

    #积分中心页面积分中心title
    chain29 = '**/XCUIElementTypeStaticText[`label == "积分中心"`]'

    #积分明细
    chain30 = '**/XCUIElementTypeStaticText[`label == "积分明细>"`]'

    #退出登录
    chain31 = '**/XCUIElementTypeButton[`label == "退出登录"`]'

    #播放记录页面title
    chain32 = '**/XCUIElementTypeStaticText[`label == "播放记录"`]'

    #播放记录页面编辑按钮
    chain33 = '**/XCUIElementTypeButton[`label == "编辑"`]'

    #过滤短视频text
    chain34 = '**/XCUIElementTypeStaticText[`label == "过滤短视频"`]'

    #过滤短视频按钮
    chain35 = '**/XCUIElementTypeSwitch[`value == "0"`]'
    chain40 = '**/XCUIElementTypeSwitch[`value == "1"`]'

    #播放记录编辑选项
    chain36 = '**/XCUIElementTypeButton[`label == "删除"`]'
    chain37 = '**/XCUIElementTypeButton[`label == "全选"`]'
    chain38 = '**/XCUIElementTypeButton[`label == "取消"`]'
    chain39 = '**/XCUIElementTypeButton[`label == "取消全选"`]'

    #播放记录中第一个播放记录
    chain41 = '**/XCUIElementTypeButton[`label == "record choice A"`][1]'
    xpath41 = '(//XCUIElementTypeButton[@name="record choice A"])[1]/preceding-sibling::XCUIElementTypeImage'
    chain42 = [(584, 177)]   #第一个媒资的名称


    #离线缓存页面 title
    chain43 = '**/XCUIElementTypeStaticText[`label == "离线缓存"`]'

    #离线缓存全部开始
    chain44 = '**/XCUIElementTypeButton[`label == "全部开始"`]'

    #离线缓存删除
    chain45 = '**/XCUIElementTypeButton[`label == "删除"`]'

    #可用内存展示
    xpath46 = '//XCUIElementTypeImage[@name="title-background"]/following-sibling::XCUIElementTypeStaticText[1]'

    #我的看单页面 title
    chain47 = '**/XCUIElementTypeStaticText[`label == "我的看单"`]'

    # 我的看单 编辑
    chain48 = '**/XCUIElementTypeStaticText[`label == "编辑"`]'

    # 我的看单 节目
    chain49 = '**/XCUIElementTypeStaticText[`label == "节目"`]'

    # 我的看单 视频
    chain50 = '**/XCUIElementTypeStaticText[`label == "视频"`]'

    #消息中心页 title
    chain51 = '**/XCUIElementTypeStaticText[`label == "消息中心"`]'

    #帮助反馈页 title
    chain52 = '**/XCUIElementTypeStaticText[`label == "帮助反馈"`]'

    #设置页title
    chain53 = '**/XCUIElementTypeStaticText[`label == "设置"`]'

    #设置页 修改密码
    chain54 = '**/XCUIElementTypeStaticText[`label == "修改密码"`]'

    #设置页 绑定号码
    chain55 = '**/XCUIElementTypeStaticText[`label == "绑定号码"`]'

    #设置页 青少年模式
    chain56 = '**/XCUIElementTypeStaticText[`label == "青少年模式"`]'

    #设置页 账号注销
    chain57 = '**/XCUIElementTypeStaticText[`label == "账号注销"`]'

    #设置页 非wifi网络下播放提醒
    chain58 = '**/XCUIElementTypeStaticText[`label == "非wifi网络下播放提醒"`]'

    #设置页 非wifi网络下播放提醒开关
    chain59 = '**/XCUIElementTypeSwitch[`label == "非wifi网络下播放提醒"`]'

    #设置页 非wifi网络下离线缓存
    chain60 = '**/XCUIElementTypeStaticText[`label == "非wifi网络下离线缓存"`]'

    #设置页 非wifi网络下离线缓存开关
    chain61 = '**/XCUIElementTypeSwitch[`label == "非wifi网络下离线缓存"`]'

    #自动跳过片头片尾
    chain62 = '**/XCUIElementTypeStaticText[`label == "自动跳过片头片尾"`]'

    #自动跳过片头片尾开关
    chain63 = '**/XCUIElementTypeSwitch[`label == "自动跳过片头片尾"`]'

    #同步芒果TV电视端播放记录
    chain64 = '**/XCUIElementTypeStaticText[`label == "同步芒果TV电视端播放记录"`]'

    #同步芒果TV电视端播放记录开关
    chain65 = '**/XCUIElementTypeSwitch[`label == "同步芒果TV电视端播放记录"`]'

    #个人信息保护政策
    chain66 = '**/XCUIElementTypeStaticText[`label == "个人信息保护政策"`]'

    # 其他法律文件
    chain67 = '**/XCUIElementTypeStaticText[`label == "其他法律文件"`]'

    # 隐私保护
    chain68 = '**/XCUIElementTypeStaticText[`label == "隐私保护"`]'

    # 常见问题
    chain69 = '**/XCUIElementTypeStaticText[`label == "常见问题"`]'

    # 清除缓存
    chain70 = '**/XCUIElementTypeStaticText[`label == "清除缓存"`]'

    # 缓存大小
    chain71 = '**/XCUIElementTypeStaticText[`label == "清除缓存"`]/following-sibling::XCUIElementTypeStaticText[1]'

    # 当前版本
    chain72 = '**/XCUIElementTypeStaticText[`label == "当前版本"`]'

    # 给我好评
    chain73 = '**/XCUIElementTypeStaticText[`label == "给我好评"`]'

    #关于我们
    chain74 = '**/XCUIElementTypeStaticText[`label == "关于我们"`]'

    # 关于我们页面 title
    chain75 = '**/XCUIElementTypeStaticText[`label == "关于我们"`]'

    # 修改密码页面
    chain76 = '**/XCUIElementTypeStaticText[`label == "修改密码"`][1]'

    # 密码限制提示
    chain77 = '**/XCUIElementTypeStaticText[`label == "密码为8-20位，且必须包含大小写字母，数字及符号"`]'

    #验证手机
    chain78 = '**/XCUIElementTypeStaticText[`label == "验证手机"`]'

    #青少年未开启状态
    chain79 = '**/XCUIElementTypeStaticText[`label == "青少年模式未开启"`]'

    #开启青少年按钮
    chain80 = '**/XCUIElementTypeButton[`label == "开启青少年模式"`]'

    #青少年页面title
    chain81 = '**/XCUIElementTypeStaticText[`label == "青少年模式"`]'

    #账号注销页面title
    chain82 = '**/XCUIElementTypeOther[`label == "账户注销协议"`]'

    #确认注销按钮
    chain83 = '**/XCUIElementTypeStaticText[`label == "确认注销"`]'

    #确认注销协议
    chain84 = '**/XCUIElementTypeStaticText[`label == "我已阅读注销协议"`]'

    #个人信息保护政策页title
    chain85 = '**/XCUIElementTypeStaticText[`label == "个人信息保护政策"`]'

    #其他法律文件页title
    chain86 = '**/XCUIElementTypeStaticText[`label == "其他法律文件"`]'

    #法律文件 服务协议
    chain87 = '**/XCUIElementTypeStaticText[`label == "服务协议"`]'

    #法律文件 历史文件
    chain88 = '**/XCUIElementTypeStaticText[`label == "历史文件"`]'

    #儿童个人信息保护政策
    chain89 = '**/XCUIElementTypeStaticText[`label == "儿童个人信息保护政策"`]'

    #服务协议title
    chain90 = '**/XCUIElementTypeStaticText[`label == "服务协议"`]'

    #历史文件title
    chain91 = '**/XCUIElementTypeOther[`label == "历史文件"`]'

    #儿童个人信息保护政策title
    chain92 = '**/XCUIElementTypeStaticText[`label == "儿童个人信息保护政策"`]'

    #隐私保护页title
    chain93 = '**/XCUIElementTypeStaticText[`label == "隐私保护"`]'

    #隐私保护页 隐私设置
    chain94 = '**/XCUIElementTypeStaticText[`label == "隐私设置"`]'

    #隐私保护页 隐私保护指南
    chain95 = '**/XCUIElementTypeStaticText[`label == "隐私保护指南"`]'

    #隐私设置页title
    chain96 = '**/XCUIElementTypeStaticText[`label == "隐私设置"`]'

    # 允许芒果TV访问位置信息
    chain97 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV访问位置信息"`]'

    # 允许芒果TV访问位置信息默认状态
    chain98 = '**/XCUIElementTypeStaticText[`label == "已开启"`][1]'

    # 允许芒果TV使用相机功能
    chain99 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV使用相机功能"`]'

    # 允许芒果TV使用相机功能默认状态
    chain100 = '**/XCUIElementTypeStaticText[`label == "已开启"`][2]'

    # 允许芒果TV使用相册存储和访问功能
    chain101 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV使用相册存储和访问功能"`]'

    # 允许芒果TV使用相册存储和访问功能默认状态
    chain102 = '**/XCUIElementTypeStaticText[`label == "去设置"`][1]'

    # 允许芒果TV使用麦克风功能
    chain103 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV使用麦克风功能"`]'

    # 允许芒果TV使用麦克风功能默认状态
    chain104 = '**/XCUIElementTypeStaticText[`label == "去设置"`][2]'

    # 允许芒果TV使用日历功能
    chain105 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV使用日历功能"`]'

    # 允许芒果TV使用日历功能默认状态
    chain106 = '**/XCUIElementTypeStaticText[`label == "去设置"`][3]'

    # 允许芒果TV向您展现个性化推荐广告
    chain107 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV向您展现个性化推荐广告"`]'

    # 允许芒果TV向您展现个性化推荐广告默认状态
    chain108 = '**/XCUIElementTypeSwitch[`label == "允许芒果TV向您展现个性化推荐广告, 为您推送与您相关的广告内容，您关闭个性化广告推荐后，我们将不会向您进行精准的广告推送，查看详情"`]'

    # 允许芒果TV向您展现个性化推荐视频
    chain109 = '**/XCUIElementTypeStaticText[`label == "允许芒果TV向您展现个性化推荐视频"`]'

    # 允许芒果TV向您展现个性化推荐视频默认状态
    chain110 = '**/XCUIElementTypeSwitch[`label == "允许芒果TV向您展现个性化推荐视频, 用于向您推荐相关度更高且对您有帮助、更适合您的优质视频内容"`]'

    # 隐私保护指南页title
    chain111 = '**/XCUIElementTypeStaticText[`label == "隐私保护指南"`]'

    #缓存清理成功提示toast
    chain112 = '**/XCUIElementTypeStaticText[`label == "清理成功"`]'

    #缓存清理成功确认
    chain113 = '**/XCUIElementTypeButton[`label == "确定"`]'

    # 关于我们页title
    chain114 = '**/XCUIElementTypeStaticText[`label == "关于我们"`]'


