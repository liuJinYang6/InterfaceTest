#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-07 22:39
# @Author : Go ku
# @File : testInterface.py

import unittest
from ddt import ddt, unpack, data  # ddt导包就是用这种方法，避免使用ddt.data 和 ddt.unpack
from common.readExcel import ReadExcel
from common.configHttp import ConfigHttp
from common.requestAssert import RequestAssert
from common.writeExcel import WriteExcel

# 读取Excel实例化
re = ReadExcel()
# 获取测试数据
testdata = re.read()
# 请求实例化
req = ConfigHttp()
# 断言实例化
result = RequestAssert()
# 写入Excel实例化
wr = WriteExcel()


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

    @data(*testdata)
    @unpack
    def testInterface(self, id, interfaceUrl, name, method, value, expect, real, status):
        # 请求接口，得到返回值
        real_status_code, real_result = req.run(interfaceUrl, method, value)

        print(real_status_code, real_result)
        # 断言接口返回值，得到断言结果

        assert_result = result.check(real_result, expect)
        print(assert_result)

        # 将断言结果写入excel
        wr.write(id, assert_result, real_status_code)


if __name__ == '__main__':
    suite = unittest.TestSuite()

    suite.addTest(MyTest('testInterface'))

    runner = unittest.TestRunner()

    runner.run(suite)
