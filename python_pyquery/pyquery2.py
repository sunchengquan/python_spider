#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
基本CSS选择器
"""
from pyquery import PyQuery as pq
doc = pq(filename='index.html')

print(doc('#container .list li'))
# print(type(doc('#container .list li')))

"""
子节点
"""
items = doc('.list')
print(type(items))
print(items)

lis = items.find('li')
print(type(lis))
print(lis)
lis = items.children()
print(type(lis))
print(lis)

lis = items.children('.active')
print(lis)