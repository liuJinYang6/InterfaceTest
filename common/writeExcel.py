#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-08 23:14
# @Author : Go ku
# @File : writeExcel.py
import xlrd
from xlutils.copy import copy
import os


class WriteExcel(object):
    """将测试结果写入excel"""

    def __init__(self):
        # 获取测试数据路径
        self.excel_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testData\\data.xls'
        # 读取excel并实例一个复制对象
        self.workbook = xlrd.open_workbook(self.excel_path)
        # 复制读取源excel对象
        self.wb = copy(self.workbook)
        # 实例一个sheet页对象
        self.ws = self.wb.get_sheet(0)

    def write(self, id, assert_result, status_code):
        """
        :param status_code:请求状态码
        :param assert_result: 断言结果
        :param id:写入excel的横坐标
        :return:
        """
        # 写入断言结果
        self.ws.write(int(id), 6, assert_result)
        # 写入请求状态码
        self.ws.write(int(id), 7, status_code)
        # 保存写入结果
        self.wb.save(self.excel_path)
        print("保存成功")


if __name__ == '__main__':
    w = WriteExcel()
    w.write(2, 'Succes', '200')
