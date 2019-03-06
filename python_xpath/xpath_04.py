#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
子节点/
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
result = selector.xpath('//li/a')
print(result)

print('-'*50)


"""
子孙节点//
"""
result = selector.xpath('//ul//a')
print(result)

print('-'*50)
#ul节点下面没有直接的a子节点
result = selector.xpath('//ul/a')
print(result)