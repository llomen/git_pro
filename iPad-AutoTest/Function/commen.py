"""
公用方法
肖子淅
日期：2022年07月20日
"""
import cv2
import numpy as np
from page import BasePage



class Commen(BasePage):

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
        # 左上角
        p1 = x - width / 2, y - height / 2
        # 左下角
        p2 = x - width / 2, y + height / 2
        # 右上角
        p3 = x + width / 2, y - height / 2
        # 右下角
        p4 = x + width / 2, y + height / 2


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
        # cut = img[int(y-(height/2)):int(y+(height/2)), int(x-width/2):int(x+width/2)]
        cut = img[2 * y:2 * (y + height), 2 * x:2 * (x + width)]
        cv2.imwrite(filename + '.jpg', cut)
