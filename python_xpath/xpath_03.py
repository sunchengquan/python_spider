#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
所有节点
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
selector = etree.HTML(text)
result = selector.xpath('//*')
print(result)


"""
所有li节点
"""
print('-'*50)
result = selector.xpath('//li')
print(result)
print(result[0])


print('-'*50)
result = selector.cssselect('ul')
print(result)
print(result[0])