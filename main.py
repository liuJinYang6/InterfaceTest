#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-13 10:09
# @Author : Go ku
# @File : main.py

import os
import unittest
import datetime
from common.configEmail import ConfigEmail

import HTMLTestRunner

current_path = os.path.abspath(__file__)
# 上层目录路径
current_dir = os.path.dirname(current_path)
# 测试用例目录
testcase_path = current_dir + "\\testCases"


# 加载所有的测试
def creat_suite():
    discover = unittest.defaultTestLoader.discover(
        start_dir=testcase_path,
        pattern='test*.py',
        top_level_dir=None
    )
    return discover


if __name__ == '__main__':
    # 获取测试集
    suit = creat_suite()
    # 获取当前时间
    # date = datetime.datetime.now().strftime('%Y-%m-%d')

    # 创建测试报告
    report_path = current_dir + '\\testReports\\testReport.html'

    with open(report_path, 'wb') as fp:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title="测试报告",
            description="报告详情",
            tester="QA"
        )

        runner.run(suit)

    mail = ConfigEmail()
    mail.send_email()
