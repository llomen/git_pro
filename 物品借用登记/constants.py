"""
数据库相关配置
肖子淅
日期：2023年01月16日
"""
from flask_sqlalchemy import SQLAlchemy

class Configs:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:qq969838847@127.0.0.1:3306/XXX1'
    # 每次请求结束后自动提交数据库中改动
    #SQLAlchemy_COMMIT_ON_TEARDOWN=True

