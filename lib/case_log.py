#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 16:19
# Author     : pan
# @File     : case_log.py
# @Software : PyCharm
from config.config import *
import json
def log_case_info(case_name,url,args,res,r):
    if isinstance(args,dict):
        args = json.dumps(args,ensure_ascii=False)#如果data是字典格式，转化为字符串
    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("请求参数：{}".format(args))
    logging.info("期望结果：{}".format(res))
    logging.info("实际结果：{}".format(r))