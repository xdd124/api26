#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:23
# Author     : pan
# @File     : post请求-传统表单.py
# @Software : PyCharm
import requests

url = "http://httpbin.org/post"

data = {
    "name":"zhangsan",
    "age":"18"
}
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}
r = requests.post(url=url,headers=headers,data=data)
print(r.text)