#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/18 15:27
# Author     : pan
# @File     : pymysqldb.py
# @Software : PyCharm
import pymysql
try:
    #打开数据库的链接
    conn = pymysql.connect(host="localhost",port=3306,
                            db="xzs",user="root",
                            password="root",charset="utf8")
    #创建一个游标对象
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM t_user WHERE id=2")
    data = cursor.fetchone()
    print(data)
except Exception as e:
    print("出错了！错误信息为：{}".format(e))
finally:
    #关闭游标
    cursor.close()
    #关闭链接
    conn.close()