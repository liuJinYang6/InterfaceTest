#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-13 10:09
# @Author : Go ku
# @File : readConfig.py


import configparser
import os


class ReadConfig(object):
    """读取.ini配置文件"""

    def __init__(self):
        # print(os.path.abspath(__file__))
        # print(os.path.dirname(os.path.abspath(__file__)))
        # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\config.ini")
        # 获取配置文件路径
        config_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\\config.ini"
        # 实例化configparse对象
        self.conf = configparser.ConfigParser()
        # 调用读取方法读取config.ini
        self.conf.read(config_path, encoding="utf-8-sig")

    def get_email(self):
        """获取邮件配置项内容"""
        mail_host = self.conf.get("EMAIL", "mail_host")
        mail_user = self.conf.get("EMAIL", "mail_user")
        mail_pass = self.conf.get("EMAIL", "mail_pass")
        mail_port = self.conf.get("EMAIL", "mail_port")
        sender = self.conf.get("EMAIL", "sender")
        receiver = self.conf.get("EMAIL", "receiver")
        subject = self.conf.get("EMAIL", "subject")
        content = self.conf.get("EMAIL", "content")
        tester = self.conf.get("EMAIL", "testuser")

        # print(mail_host, mail_user, mail_pass, mail_port, sender, receiver, subject, content, tester)
        return mail_host, mail_user, mail_pass, mail_port, sender, receiver, subject, content, tester


if __name__ == '__main__':
    a = ReadConfig()
    a.get_email()
