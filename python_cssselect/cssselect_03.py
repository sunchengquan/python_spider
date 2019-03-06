#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
子节点
子孙节点
"""

import lxml.html

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
selector = lxml.html.fromstring(text)
result = selector.cssselect('li a')
print('li节点内所有子节点a'.center(50,"-"))
print(result)

result = selector.cssselect('ul a')
print('ul节点内所有子节点a'.center(50,"-"))
print(result)

result = selector.cssselect('li>a')
print('以li节点为父节点，所有子节点a'.center(50,"-"))
print(result)

result = selector.cssselect('ul>a')
print(result)
