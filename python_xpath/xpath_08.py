#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
按序选择
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
content = selector.xpath('//li[1]/a/text()')
print('第一个li节点'.center(50,"-"))
print(content)

result = selector.xpath('//li[last()]/a/text()')
print('最后一个li节点'.center(50,"-"))
print(result)

result = selector.xpath('//li[position()<3]/a/text()')
print('位置小于3的li节点'.center(50,"-"))
print(result)

result = selector.xpath('//li[last()-2]/a/text()')
print('倒数第三个li节点'.center(50,"-"))
print(result)

