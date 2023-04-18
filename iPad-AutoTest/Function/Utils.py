"""
IPAD自动化测试
肖子淅
日期：2022年07月26日
提供mac terminal 操作交互
"""
import os

class Utils():
    def exeLocalcmd(self, str):
        print(str)
        with os.popen(str) as stdout:
            result = stdout.read()
        return result


if __name__ == '__main__':
    util = Utils().exeLocalcmd("idevice_id -l")