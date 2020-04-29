#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-08 22:45
# @Author : Go ku
# @File : requestAssert.py


class RequestAssert(object):
    """断言接口请求结果"""

    def check(self, real_result, expect_result):
        """
        :param real_result: 实际结果
        :param expect_result: 预期结果
        :return: Sussce 或 False 断言结果
        """
        if str(real_result) == str(expect_result):

            return "Success"

        else:

            return "False"
