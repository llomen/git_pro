"""
IPAD自动化测试
肖子淅
日期：2022年04月27日
"""
import time
from selenium.webdriver.support.wait import WebDriverWait
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import image_match


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_ele(self, loc):
        return self.driver.find_element_by_ios_class_chain(loc)

    def find_ele_xpath(self, loc):
        return self.driver.find_element_by_xpath(loc)

    def click_element(self, loc):
        '原click_ele改名而来'
        time.sleep(5)
        self.find_ele(loc).click()
        time.sleep(5)


    #  找不到元素就通过坐标点击
    def click_ele_point(self, loc):
        time.sleep(10)
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
        location_new = (int(x + width / 2), int(y + height / 2))
        time.sleep(5)
        self.driver.tap([location_new], 50)
        print(location_new)
        time.sleep(5)

    def click_ele(self, loc):
        '如果是visible是true的，采用原click_element点击方式，否则使用click_ele_point'
        if self.find_ele(loc).get_attribute('visible') == 'true':
            self.click_element(loc)
        else:
            self.click_ele_point(loc)






    def click_ele_xpath(self, loc):
        time.sleep(5)
        self.find_ele_xpath(loc).click()
        time.sleep(5)

    def send_keys(self,loc,vaule):
        self.find_ele(loc).clear()
        time.sleep(5)
        self.find_ele(loc).send_keys(vaule)
        time.sleep(5)


    def hide_keyborad(self):
        self.click_ele('**/XCUIElementTypeButton[`label == "隐藏键盘"`]')
        time.sleep(5)

    def search_enter(self):
        #键盘搜索按钮
        self.driver.tap([(1000, 630)], 10)
        time.sleep(10)


    def tap_point(self, x, y):
        #搜索结果页播放按钮
        self.driver.tap([(x,y)], 10)
        time.sleep(10)







