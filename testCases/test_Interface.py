#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-07 22:39
# @Author : Go ku
# @File : test_Interface.py

import unittest
import ddt


@ddt
class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        '''可以用来准备测试环境的前置条件'''
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        '''可以用来完成测试完成后的数据清洗工作'''
        pass

    def setUp(self) -> None:
        '''
        每个测试用例的前置条件
        每个testcase运行前都会执行一遍
        '''
        pass

    def tearDown(self) -> None:
        '''
        每个测试用例完成的数据清洗
        每个testcase结束后都会执行一次
        '''
        pass

    @data(*kwargs)
    @unpack
    def testInterface(self, id,interfaceUrl,name,Method,value,expect,real,status):

        # todo 测试用例执行
        pass

