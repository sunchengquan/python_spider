#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
节点选择器
嵌套选择
"""
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>

"""



soup = BeautifulSoup(html, 'lxml')

print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)