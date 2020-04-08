#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-08 22:45
# @Author : Go ku
# @File : requestAssert.py
from unittest import TestCase


class RequestAssert(object):
    """断言接口请求结果"""

    def check(self, real_result, expect_result):
        """
        :param real_result: 实际结果
        :param expect_result: 预期结果
        :return:
        """
        if str(real_result) == str(expect_result):

            return "Sussce"

        else:

            return "False"


