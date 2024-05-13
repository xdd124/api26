#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/5/6 16:24
# Author     : pan
# @File     : basecase.py
# @Software : PyCharm
import unittest,requests,json,sys,ast
from config.config import *
from lib.read_excel import *
from lib.case_log import log_case_info

sys.path.append("../..")#统一将包的搜索路径提升到项目根目录下

class BaseCase(unittest.TestCase):#继承unittest.TestCase
    r = readexcel()
    @classmethod
    def setUpClass(cls):
        if cls.__name__ !='BaseCase':
            cls.data_list = cls.r.excel_to_list(data_file,cls.__name__)

    def get_case_data(self,case_name):
        return self.r.get_test_data(self.data_list,case_name)

    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('header')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')
        if method.upper() == 'GET':#GET类型请求
            res = requests.get(url=url,params=json.loads(args))
        elif data_type.upper() == 'FORM':#表单格式请求
            res = requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_name,url,args,expect_res,res.text)
            self.assertIn(expect_res,res.text)
        elif data_type.upper() == 'JSON':#JSON格式请求
            res = requests.post(url=url,json=json.loads(args),headers=json.loads(headers))
            log_case_info(case_name,url,args,expect_res,res.json())
            self.assertIn(expect_res,res.text)
