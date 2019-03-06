#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
多属性
"""

import lxml.html

text = '''
<li class="li li-first"><a href="link1.html">first item</a></li>
<li class="li "><a href="link2.html">second item</a></li>
<li class="li li-first" name="item"><a href="link3.html">third item</a></li>
<li class="li" name="item"><a href="link4.html">fourth item</a></li>
'''

selector = lxml.html.fromstring(text)
result = selector.cssselect('li.li >a')
print('属性匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])


result = selector.cssselect('li.li >a[href*="2"]')
print('属性匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])


result = selector.cssselect('li.li-first >a')
print('属性匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])

result = selector.cssselect('li.li.li-first >a')
print('属性多值匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])


result =selector.cssselect('li.li[name=item] > a')
print('多属性匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])

result =selector.cssselect('li.li.li-first[name=item] > a')
print('多属性匹配'.center(50,"-"))
print([i.text_content().strip() for i in result])





