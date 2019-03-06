#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
会话维持

两次请求时设置一样的cookies不就行了？可以，但这样做起来显得很烦琐，我们有更简单的解决方法
"""

import requests

requests.get('http://httpbin.org/cookies/set/number/123456789')
r = requests.get('http://httpbin.org/cookies')
print(r.text)

s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)

s = requests.session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)