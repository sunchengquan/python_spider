#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
按序选择
"""

import lxml.html
text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <p class="item-0"><a href="link1.html">second item</a></p>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <p class="item-0"><a href="link1.html">first item</a></p>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''

selector = lxml.html.fromstring(text)
result = selector.cssselect('li:nth-child(1)')
print('第一个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('li:first-child')
print('第一个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('p:first-child')
print('第一个p节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('p:first-of-type')
print('第一个p节点'.center(50,"-"))
print([i.text_content().strip() for i in result])



result = selector.cssselect('li:nth-child(2)')
print('第二个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('li:nth-of-type(2)')
print('第二个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])



result = selector.cssselect('li:nth-last-child(2)')
print('倒数第二个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('li:nth-last-of-type(2)')
print('倒数第二个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])


result = selector.cssselect('li:last-child')
print('最后一个li节点'.center(50,"-"))
print([i.text_content().strip() for i in result])

result = selector.cssselect('p:last-child')
print('最后一个p节点'.center(50,"-"))
print([i.text_content().strip() for i in result])
result = selector.cssselect('p:last-of-type')
print('最后一个p节点'.center(50,"-"))
print([i.text_content().strip() for i in result])