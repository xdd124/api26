#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/26 15:03
# Author     : pan
# @File     : config.py
# @Software : PyCharm
import logging,time
import os
from optparse import OptionParser

now = time.strftime("%Y%m%d_%H%M%S",time.localtime())
today = time.strftime("%Y-%m-%d",time.localtime())

#项目路径
#prj_path是当前文件的绝对路径的上一级，__file__指当前文件
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(prj_path,"data") #数据目录，暂时在项目目录下
test_path = os.path.join(prj_path,"test") #用例目录，暂时在项目目录下
test_case_path = os.path.join(prj_path,"test","case")
log_file = os.path.join(prj_path, "log","log_{}.txt".format(today))
report_file = os.path.join(prj_path, "report","report_{}.html".format(now))
data_file = os.path.join(prj_path,"data","test_user_data.xlsx")
testlist_file = os.path.join(prj_path,"test","testlist.txt")
last_fails_file = os.path.join(prj_path,"last_failures.pickle")

#log文件配置
logging.basicConfig(
    level=logging.DEBUG,#log level
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',#log格式
    datefmt='%Y-%m-%d %H:%M:%S',#日期格式
    filename=log_file,#日志输出文件
    filemode='a'
)

#数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_ps = 'root'
db = 'xzs'

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '3402635787@qq.com'
smtp_ps = 'nmjmbxbidrsjchgc'
sender = smtp_user
receiver = '3402635787@qq.com'
subject = '接口测试报告'
send_email_after_run=False #是否发送邮件

#命令行参数解析
parser = OptionParser()
parser.add_option("--collect_only",action='store_true',dest='collect_only',help='仅列出所有用例')
parser.add_option("--rerun_fails",action='store_true',dest='rerun_fails',help='运行上次失败的用例')
parser.add_option("--tag",action='store',default='level1',dest='tag',help='运行指定tag的用例')
parser.add_option("--testlist",action='store_true',dest='testlist',help='运行test/testlist.txt列表指定用例')
parser.add_option('--testsuite',action='store',dest='testsuite',help='运行指定的TestSuite')
#生效参数
(options,args) = parser.parse_args()

if __name__ == '__main__':
    logging.info("接口测试")