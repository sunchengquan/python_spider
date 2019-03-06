#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
文本
属性
"""

import lxml.html

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a link="link5.html">fifth item</a>
     </ul>
 </div>
'''

selector = lxml.html.fromstring(text)
result = selector.cssselect('li.item-0')
print('属性匹配'.center(50,"-"))
print(result)

result = selector.cssselect('li.item-0')
print('文本获取'.center(50,"-"))
print([i.text_content().strip() for i in result])

result = selector.cssselect('li >a ')
print('获取属性'.center(50, "-"))
print([i.get('href') for i in result])


result = selector.cssselect('li.item-0::')
print('文本获取'.center(50, "-"))
print(result)
