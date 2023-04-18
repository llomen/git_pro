"""
物品借用登记(正式使用版本)
肖子淅
日期：2023年01月16日
"""
from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import pymysql
import json

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])

def B():
    if request.method == 'GET':
        return  render_template('info.html')
    if request.method == 'POST':
        borrower = request.form.get('borrower')
        device_name = request.form.get('device_name')
        date = request.form.get('date')
        coon = pymysql.Connect(
            host="localhost",
            port=3306,
            user="root",
            password="qq969838847",
            db="xxx1"
        )
        cursor = coon.cursor()
        sql = "insert into WUPINGDENGJI values (\"%s\",\"%s\",\"%s\")"%(borrower,device_name,date)
        cursor.execute(sql)
        coon.commit()
        cursor.close()
        coon.close()
        return "提交成功"


@app.route('/get_info', methods = ['GET'])

def get_info():
    borrower = request.form.get('borrower')
    device_name = request.form.get('device_name')
    date = request.form.get('date')
    coon = pymysql.Connect(
        host="localhost",
        port=3306,
        user="root",
        password="qq969838847",
        db="xxx1"
        )
    # 查询借用登记列表
    sql2 = "select * from WUPINGDENGJI"
    coon.commit()
    curses = coon.cursor(cursor=pymysql.cursors.DictCursor)
    curses.execute(sql2)
    data = curses.fetchall()
    coon.close()
    return render_template("list.html", data=data)


if __name__  == "__main__":
    app.run(host= '0.0.0.0', port=5000, debug = True)

