"""
物品借用登记(调试使用版本)
肖子淅
日期：2023年01月16日
"""
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import pymysql
import json
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def B():
    if request.method == 'GET':
        return  render_template('info_test.html')
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        device_name = request.form.get('device_name')
        date = request.form.get('date')
        status = request.form.get('status')
        coon = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            password="qq969838847",
            db="xxx1"
        )
        cursor = coon.cursor()
        sql = "insert into wpdj(borrower,device_name,date) values (\"%s\",\"%s\",\"%s\")"%(borrower, device_name,date)
        cursor.execute(sql)
        coon.commit()
        cursor.close()
        coon.close()
        return "提交成功"


@app.route('/get_info', methods = ['GET','POST'])

def get_info():
    borrower = request.form.get('borrower')
    device_name = request.form.get('device_name')
    date = request.form.get('date')
    status = request.form.get('status')
    coon = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        password="qq969838847",
        db="xxx1"
        )
    # 查询借用登记列表
    sql2 = "select * from wpdj"
    coon.commit()
    curses = coon.cursor(cursor=pymysql.cursors.DictCursor)
    curses.execute(sql2)
    data = curses.fetchall()
    coon.close()
    return render_template("list_test.html", data=data)




if __name__  == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug = True)

