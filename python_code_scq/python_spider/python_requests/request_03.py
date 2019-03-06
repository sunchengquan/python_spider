#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
POST请求
"""

import requests

data = {'name': 'germey', 'age': '22'}
r = requests.post("http://httpbin.org/post", data=data)
print(r.text)
