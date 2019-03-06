#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
遍历
"""
from pyquery import PyQuery as pq
doc = pq(filename='index.html')

# li = doc('.item-0.active')
# print(li)
# print(str(li))

li = doc('.wrap .item-1.active')
print(li)



# lis = doc('li').items()
# print(type(lis))
# for li in lis:
#     print(li, type(li))


"""
获取属性
"""

# a = doc('.item-0.active a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)

#包含多个节点时，调用attr()方法，只会得到第一个节点的属性
# a = doc('a')
# print(a, type(a))
# print(a.attr('href'))
# print(a.attr.href)

#获取所有的a节点的属性
# a = doc('a')
# for item in a.items():
#     print(item.attr('href'))


"""
获取文本
"""
# a = doc('.item-0.active a')
# print(a)
# print(a.text())

#获取这个节点内部的HTML文本
# li = doc('.item-0.active')
# print(li)
# print(li.html())

#结果是多个节点
#html()方法返回的是第一个li节点的内部HTML文本，而text()则返回了所有的li节点内部的纯文本，中间用一个空格分割开，即返回结果是一个字符串
# li = doc('li')
# print(li.html())
# print(li.text())
# print(type(li.text()))

