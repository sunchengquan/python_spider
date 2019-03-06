#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
 实例引入
"""

import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

"""
r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')
"""
