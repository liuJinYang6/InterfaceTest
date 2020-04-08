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
        try:

            response = requests.get(url=url, params=eval(params))

            real = response.content

            status_code = response.status_code

            real = response.json()['errorCode']

            return status_code, real

        except Exception:

            print("request error,please check out!")

            return None, None

    def post(self, url, params):
        """
        封装requsets.post()方法
        """
        try:
            response = requests.post(url=url, data=eval(params))

            status_code = response.status_code

            real = response.json()['errorCode']

            return status_code, real

        except Exception:

            print("request error,please check out!")

            return None, None

    def run(self, url, method, params):

        if method == 'get' or method == 'GET':
            status_code, real = self.get(url, params)
            return status_code, real

        if method == 'post' or method == 'POST':
            status_code, real = self.post(url, params)
            return status_code, real


if __name__ == '__main__':
    pass
