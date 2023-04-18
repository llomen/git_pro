"""
IPAD自动化测试
肖子淅
日期：2022年04月27日
功能：控制执行用例并生成报告！！！！
"""
from appium import webdriver
import time
import unittest
from page import base
import HTMLTestRunner,logging
from jingxuan import jingxuan_test
from wode import wo_test
from pianku import pianku_test
from login import login_test
from search import search_test
from HTMLTestRunner import HTMLTestRunner
from page.jingxuan_page import JingxuanPage



now = time.strftime("%Y-%m-%d_%H_%M_%S",time.localtime())

#定义一个测试容器
testunit = unittest.TestSuite()

#测试容器内添加测试用例
testunit.addTest(unittest.makeSuite(jingxuan_test))
testunit.addTest(unittest.makeSuite(wo_test))
testunit.addTest(unittest.makeSuite(pianku_test))
testunit.addTest(unittest.makeSuite(login_test))
testunit.addTest(unittest.makeSuite(search_test))



# -------生成hmtl报告-------------
# html报告保存路径
HTMLfilepath = r'/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/Function/report' + '/' + now + r"_result.html"
print("HTML报告生成路径：", HTMLfilepath)
fp = open(HTMLfilepath, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='ipad自动化测试报告',
    description='测试结果描述'
)

# -------------------------------------------------导出日志-------------------------------------------------

# log日志保存路径
Logfilepath = r'/Users/xiaozixi/Desktop/自动化测试/iPad-AutoTest/Function/report' + '/' + now + r"_result.log"  # 保存路径，文件名字为：时间_result.log

print("log日志生成路径: ", Logfilepath)  # 输出日志路径

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=Logfilepath,
                    filemode='w')
logger = logging.getLogger()
logger.info(testunit)
runner.run(testunit)  # 执行测试套件
fp.close()
