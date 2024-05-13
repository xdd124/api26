#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 14:45
# Author     : pan
# @File     : get请求.py
# @Software : PyCharm
import requests

url = "https://www.baidu.com"

#发送一个get请求
r = requests.get(url)
#响应的文本信息
print(r.text)
#响应的二进制格式
print(r.content)
#响应的头部信息
print(r.headers)
#响应的状态码
print(r.status_code)
#响应的编码格式
print(r.encoding)
