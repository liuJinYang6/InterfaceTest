#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-07 22:01
# @Author : Go ku
# @File : readExcel.py

import xlrd
import os


class ReadExcel(object):
    """从Excel读取测试数据"""

    def __init__(self):
        # 获取测试数据路径
        excel_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\testData\\data.xls'
        # print(excel_path)
        # 打开excel文件
        workbook = xlrd.open_workbook(filename=excel_path)
        # 打开sheet页
        self.sheet = workbook.sheet_by_index(0)
        # 存储测试数据
        self.data = []

    def read(self):
        '''读取测试数据,返回测试数据'''
        for n in range(1, self.sheet.nrows):

            row = self.sheet.row_values(n)

            self.data.append(row)

        return self.data


if __name__ == '__main__':

    re = ReadExcel()

    a = re.read()

    print(a)
