#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2020-04-07 21:37
# @Author : Go ku
# @File : configHttp.py

import requests


class ConfigHttp(object):
    """二次封装request方法"""

    def get(self, url, params):
        """
        封装requsets.get()方法
        """
        response = requests.get(url=url, params=params)

        real = response.content

        status_code = response.status_code

        real = response.text

        return status_code, real

    def post(self, url, params):
        """
        封装requsets.post()方法
        """
        response = requests.post(url=url, data=params)

        status_code = response.status_code

        real = response.text

        return status_code, real

    def run(self, url, method, params):

        if method == 'get' or method == 'GET':
            status_code, real = self.get(url, params)

        if method == 'post' or method == 'POST':
            status_code, real = self.post(url, params)
