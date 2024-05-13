#! /usr/bin/evn python
# -*- coding: utf-8 -*-
# @Time     : 2024/4/27 8:45
# Author     : pan
# @File     : send_email_base.py
# @Software : PyCharm
import smtplib#用于建立smtp连接
from email.mime.text import MIMEText#邮箱需要专门的MIME格式
#编写邮件内容
msg = MIMEText('邮件内容','plain','utf-8')#plain指普通文本格式邮件内容
#组装email头（发件人，收件人，主题）
msg['From'] = '3402635787@qq.com'#发件人
msg['To'] = '3402635787@qq.com'#收件人
msg['Subject'] = '接口自动化'#邮件主题
#连接smtp服务器并发送邮件
stmp = smtplib.SMTP_SSL('smtp.163.com')
stmp.login('3402635787@qq.com','nmjmbxbidrsjchgc')#发送人邮箱和授权码
stmp.sendmail('3402635787@qq.com','3402635787@qq.com',msg.as_string())
stmp.quit()