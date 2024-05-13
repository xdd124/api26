#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/15 15:14
# Author     : pan
# @File     : get请求-带参数.py
# @Software : PyCharm
import requests

#方法一
# url = "http://www.tuling123.com/openapi/api?key=ec961279f453459b9248f0aeb6600bbe&info=你好"
#方法二
url = "http://www.tuling123.com/openapi/api"
params={
    "key":"ec961279f453459b9248f0aeb6600bbe",
    "info":"你好"
}

r = requests.get(url,params=params)
print(r.text)