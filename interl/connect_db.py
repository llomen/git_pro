"""
肖子淅
日期：2024年07月24日
链接数据库
"""
#utf-8
import pymysql,traceback,sys

class MysqlUtil:
    def __init__(self):
        '''
        链接数据库
        '''
        self.host = '10.200.131.79'
        self.user = 'ito-admin'
        self.password = 'aJjCu1f1'
        self.port = 3306
        self.charset = 'utf8'
        self.database = 'ito'


    def fetchone(self,sql):
        """
        查询单个结果
        :param database:
        :param sql:
        :return:返回所有查询结果
        """
        self.db = pymysql.connect(
            host = self.host,user = self.user,password = self.password,db = self.database,
            port = self.port,charset = self.charset)
        self.cursor = self.db.cursor(
            cursor=pymysql.cursors.DictCursor
        )
        try:
            self.cursor.execute(sql)
            result = self.cursor.fetchall()
            return result
        except Exception:
            print('error', Exception)
            self.db.rollback()
        finally:
            self.db.close()


