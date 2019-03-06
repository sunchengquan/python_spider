#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
父节点
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

"""
现在首先选中href属性为link4.html的a节点，然后再取其父节点，然后再取其class属性。
"""
selector = etree.HTML(text)
result = selector.xpath('//a[@href="link4.html"]/../@class')
print(result)

print('-'*50)
result = selector.xpath('//a[@href="link4.html"]/parent::*/@class')
print(result)
