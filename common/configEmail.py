#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-13 9:49
# @Author : Go ku
# @File : configEmail.py

import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readConfig import ReadConfig


class ConfigEmail(object):
    """封装发送邮件功能"""

    def __init__(self):
        r = ReadConfig()
        mail_host, mail_user, mail_pass, mail_port, sender, receiver, subject, content, tester = r.get_email()
        # 第三方smtp服务
        self.mail_host = mail_host  # 设置服务器

        self.mail_port = mail_port  # 设置端口

        self.mail_user = mail_user  # 用户

        self.mail_pwd = mail_pass  # 密码

        # 发件人
        self.sender = sender
        # 收件人
        self.recever = receiver

        # 邮件标题
        self.subject = subject
        # 邮件正文
        self.content = content
        # 邮件信息
        self.message = MIMEMultipart()

    def congfig_email(self):
        """配置邮件内容信息"""

        # 获取测试报告路径
        report_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testReports\\testReport.html'
        # print(report_path)

        # 读取测试报告
        with open(report_path, 'rb') as fp:
            sendfile = fp.read()

        # 附件信息设置
        att = MIMEText(sendfile, 'plain', 'utf-8')
        att['Content-Type'] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'

        #  添加附件
        self.message.attach(att)

        # 邮件信息设置
        self.message['From'] = self.sender
        self.message['To'] = self.recever
        self.message['Subject'] = Header(self.subject, 'utf-8')
        self.message.attach(MIMEText(self.content, 'plain', 'utf-8'))

    def send_email(self):
        """发送邮件"""
        self.congfig_email()
        try:
            s = smtplib.SMTP()
            # 连接stmp服务器
            s.connect(self.mail_host, self.mail_port)
            # 登录邮箱
            s.login(self.mail_user, self.mail_pwd)
            # 发送邮件
            s.sendmail(self.sender, self.recever, self.message.as_string())
            print("发送成功！")

        except smtplib.SMTPException as msg:
            print(msg)
            print("Error!发送邮件失败")


if __name__ == '__main__':
    c = ConfigEmail()
    c.send_email()
