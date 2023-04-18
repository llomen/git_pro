"""
IPAD自动化测试
肖子淅
日期：2022年12月06日
"""
import pymysql
from flask import Flask,jsonify,request,Response
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import constants

app = Flask(__name__)  # 创建一个服务，赋值给APP
app.config.from_object(constants.Configs)
db = SQLAlchemy(app)

class WPDJ(db.Model):
    __tablename__ = 'wpdj'
    id = db.Column(db.Integer, primary_key=True)
    borrower = db.Column(db.String(50),nullable=False)
    device_name = db.Column(db.String(50),nullable=False)
    date = db.Column(db.DateTime, default = datetime.now)
    status = db.Column(db.String(50))

if __name__  == "__main__":
    with app.app_context():
        db.create_all()
