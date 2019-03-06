#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
父节点
"""
from pyquery import PyQuery as pq
doc = pq(filename='index.html')


items = doc('.list')
container = items.parent()
# print(type(container))
# print(container)

items = doc('.list')
parents = items.parents()
# print(type(parents))
# print(parents)

parent = items.parents('.wrap')
print(parent)



"""
兄弟节点
"""
li = doc('.list .item-0.active')
print(li.siblings())

li = doc('.list .item-0.active')
print(li.siblings('.active'))