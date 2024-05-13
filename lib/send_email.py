#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/28 14:34
# Author     : pan
# @File     : send_email.py
# @Software : PyCharm
import smtplib#用于建立smtp连接
from email.mime.text import MIMEText#邮箱需要专门的MIME格式
from email.mime.multipart import MIMEMultipart#支持上传附件
from email.header import Header#用于使用中文邮件主题
from config.config import *
def send_email(report_file):
    #编写邮件内容
    with open(report_file,encoding='utf-8') as f:#获取附件文件
        email_body = f.read()#读取附件文件内容
    msg = MIMEMultipart()#混合MIME格式（支持上传附件）
    msg.attach(MIMEText(email_body,'html','utf-8'))#添加html格式邮件正文
    #组装email头（发件人，收件人，主题）
    msg['From'] = sender#发件人
    msg['To'] = receiver#收件人
    msg['Subject'] = Header(subject,'utf-8')#中文邮件主题，指定utf-8编码
    #构造附件，传送当前文件夹下的report.html文件
    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')#二进制格式打开
    att1['Content-Type'] = 'application/octet-stream'
    att1['Content-Disposition'] = 'attachment;filename="report.html"'
    msg.attach(att1)
    try:
        #连接smtp服务器并发送邮件
        smtp = smtplib.SMTP_SSL(smtp_server)
        smtp.login(smtp_user,smtp_ps)#发送人邮箱和授权码
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info("===========邮件发送成功===========")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()