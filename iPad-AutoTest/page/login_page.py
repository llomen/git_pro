"""
IPAD自动化测试
肖子淅
日期：2022年04月27日
"""
import time
from page.BasePage import BasePage
import image_match
import page.wode_page
import cv2
import numpy as np
from PIL import ImageGrab





class LoginPage(BasePage):
    # 登录/注册按钮
    chain1 = '**/XCUIElementTypeButton[`label == "登录/注册"`]'

    # 快捷登录
    chain2 = '**/XCUIElementTypeStaticText[`label == "快捷登录"`]'

    # 登录按钮
    chain3 = '**/**[`label == "登 录"`]'
    xpath3 = '//XCUIElementTypeStaticText[@name="登 录"]'
    point3 = [(533, 451)]
    classname = '登 录'
    image_path = '../img/login_btn.PNG'

    # 个人信息保护勾选框
    chain4 = '**/XCUIElementTypeButton[`label == "mg checkbox"`]'

    # 关闭快捷登录页面
    chain5 = '**/XCUIElementTypeButton[`label == "cancel login"`]'

    # 使用其他账号登录
    chain6 = '**/XCUIElementTypeButton[`label == "使用其他账号登录"`]'

    # 手机号登录-手机号输入框
    chain7 = '**/XCUIElementTypeTextField[`value == "请输入手机号"`]'

    # 默认归属地
    chain8 = '**/XCUIElementTypeStaticText[`label == "中国+86"`]'

    # 验证码输入框
    chain9 = '**/XCUIElementTypeTextField[`value == "请输入验证码"`]'

    # 获取验证码按钮
    chain10 = '**/XCUIElementTypeButton[`label == "获取校验码"`]'

    # 账号登录按钮
    chain11 = '**/XCUIElementTypeButton[`label == "账号登录"`]'

    # 账号注册按钮
    chain12 = '**/XCUIElementTypeButton[`label == "注册"`]'

    # 其他登录方式
    chain13 = '**/XCUIElementTypeStaticText[`label == "其他登录方式"`]'

    # 微信登录
    chain14 = '**/XCUIElementTypeButton[`label == "icon wechat login"`]'

    # 微博登录
    chain15 = '**/XCUIElementTypeButton[`label == "icon weibo login"`]'

    # qq登录
    chain16 = '**/XCUIElementTypeButton[`label == "icon qq login"`]'

    # 邮箱登录
    chain17 = '**/XCUIElementTypeButton[`label == "icon mail login"`]'

    # APPle id登录
    chain18 = '**/XCUIElementTypeButton[`label == "share Apple"`]'

    # 邮箱登录页面-邮箱登录
    chain19 = '**/XCUIElementTypeStaticText[`label == "邮箱登录"`]'

    # 邮箱登录页面-返回按钮
    chain20 = '**/XCUIElementTypeButton[`label == "mine back"`]'

    # 邮箱登录页面-关闭按钮
    chain21 = '**/XCUIElementTypeButton[`label == "cancel login"`]'

    # 邮箱登录页面 邮箱地址输入框
    chain22 = '**/XCUIElementTypeTextField[`value == "请输入邮箱地址"`]'

    # 邮箱登录页面 邮箱密码输入框
    chain23 = '**/XCUIElementTypeSecureTextField[`value == "请输入密码"`]'

    # 邮箱登录页面 忘记密码
    chain24 = '**/XCUIElementTypeStaticText[`label == "忘记密码"`]'

    # 快捷登录登录按钮
    point25 = [(385, 475)]

    #设置
    chain25 = '**/XCUIElementTypeStaticText[`label == "设置"`]'

    #退出登录
    chain26 = '**/XCUIElementTypeButton[`label == "退出登录"`]'

    slider_ele = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[2]'

    background_ele = '**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage[1]'





    def mail_login(self,mail,mail_secret):
        self.send_keys(self.chain22,mail)
        self.send_keys(self.chain23,mail_secret)
        self.hide_keyborad()
        self.click_ele(self.chain4)
        #self.click_ele(self.chain3)
        #self.driver.find_element_by_xpath(self.xpath3).click()
        #self.driver.find_element_by_name(self.classname).click()
        #self.driver.find_element_by_image(self.image_path).click()
        self.driver.tap(self.point3, 1000)
        time.sleep(10)


    def into_mail_login(self):
        "邮箱登录之前存在快捷登录"
        self.click_ele(self.chain1)
        self.click_ele(self.chain6)
        self.click_ele(self.chain17)

    def quick_login(self):
        self.click_ele(self.chain4)
        self.driver.tap(self.point25,1000)
        time.sleep(5)


    def logout(self):
        self.driver.swipe(20, 700, 20, 400, 1000)
        self.click_ele(self.chain25)
        self.driver.swipe(800,700,800,400, 10000)
        self.click_ele(self.chain26)


    def mobile_login(self,phone_number):
        "手机登录"
        self.click_ele(self.chain1)
        self.click_ele(self.chain7)
        self.send_keys(self.chain7, phone_number)
        self.click_ele(self.chain10)

    def get_location(self, loc):
        "获取元素四点坐标"
        ele_size = self.find_ele(loc).size
        # 元素的宽
        width = ele_size['width']
        # 元素的高
        height = ele_size['height']
        ele_coordinate = self.find_ele(loc).location
        # 元素中心横坐标
        x = ele_coordinate['x']
        # 元素中心纵坐标
        y = ele_coordinate['y']
        #左上角
        p1 = x-width/2 , y-height/2
        #左下角
        p2 = x-width/2 , y+height/2
        #右上角
        p3 = x+width/2, y-height/2
        #右下角
        p4 = x+width/2, y+height/2


    def cut(self, loc, filename):
        "cv2库根据元素坐标四点截图"
        self.driver.get_screenshot_as_file('/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/Function/cut.jpg')
        path = '/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/Function/cut.jpg'
        "获取元素四点坐标"
        ele_size = self.find_ele(loc).size
        # 元素的宽
        width = ele_size['width']
        # 元素的高
        height = ele_size['height']
        ele_coordinate = self.find_ele(loc).location
        # 元素左上角横坐标
        x = ele_coordinate['x']
        # 元素左上角纵坐标
        y = ele_coordinate['y']
        img = cv2.imread(path)
        #cut = img[int(y-(height/2)):int(y+(height/2)), int(x-width/2):int(x+width/2)]
        cut = img[2*y:2*(y+height), 2*x:2*(x+width)]
        cv2.imwrite(filename + '.jpg', cut)




    def get_element_slide_distance(self, slider_ele, background_ele, correct=0):
        """
        根据传入滑块，和背景的节点，计算滑块的距离

        该方法只能计算 滑块和背景图都是一张完整图片的场景，
        如果背景图是通过多张小图拼接起来的背景图，
        该方法不适用，请使用get_image_slide_distance这个方法
        :param slider_ele: 滑块图片的节点
        :type slider_ele: WebElement
        :param background_ele: 背景图的节点
        :type background_ele:WebElement
        :param correct:滑块缺口截图的修正值，默认为0,调试截图是否正确的情况下才会用
        :type: int
        :return: 背景图缺口位置的X轴坐标位置（缺口图片左边界位置）
        """
        # 获取验证码的图片
        #slider_url = slider_ele.get_attribute("src")
        #background_url = background_ele.get_attribute("src")
        # 下载验证码背景图,滑动图片
        slider = "slider.jpg"
        background = "background.jpg"
        #self.onload_save_img(slider_url, slider)
        #self.onload_save_img(background_url, background)
        # 读取进行色度图片，转换为numpy中的数组类型数据，
        slider_pic = cv2.imread(slider, 0)
        background_pic = cv2.imread(background, 0)
        # 获取缺口图数组的形状 -->缺口图的宽和高
        #width, height = slider_pic.shape[::-1]
        # 将处理之后的图片另存
        slider01 = "slider01.jpg"
        background_01 = "background01.jpg"
        cv2.imwrite(background_01, background_pic)
        cv2.imwrite(slider01, slider_pic)
        # 读取另存的滑块图
        slider_pic = cv2.imread(slider01)
        # 进行色彩转换
        slider_pic = cv2.cvtColor(slider_pic, cv2.COLOR_BGR2GRAY)
        # 获取色差的绝对值
        slider_pic = abs(255 - slider_pic)
        # 保存图片
        cv2.imwrite(slider01, slider_pic)
        # 读取滑块
        slider_pic = cv2.imread(slider01)
        # 读取背景图
        background_pic = cv2.imread(background_01)
        # 比较两张图的重叠区域
        result = cv2.matchTemplate(slider_pic, background_pic, cv2.TM_CCOEFF_NORMED)
        # 获取图片的缺口位置
        top, left = np.unravel_index(result.argmax(), result.shape)
        # 背景图中的图片缺口坐标位置
        #print("当前滑块的缺口位置：", (left, top, left + width, top + height))
        return(left)










