#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
属性多值匹配
"""
from lxml import etree
text = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''

selector = etree.HTML(text)
content = selector.xpath('//li[@class="li"]/a/text()')
print(content)


#contains()函数，第一个参数传入属性名称，第二个参数传入属性值
print('属性多值匹配'.center(50,"-"))
result = selector.xpath('//li[contains(@class, "li")]/a/text()')
print(result)









'''
多属性匹配
'''
#and 是XPath中的运算符
text = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html = etree.HTML(text)
result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
print('多属性匹配'.center(50,"-"))
print(result)

text = """

<bookstore>

<book>
  <title lang="zh">Harry Potter</title>
  <price>25.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

<book author="sunchengquan">
  <title lang="eng" >Learning Python</title>
  <price>30.95</price>
</book>

</bookstore>

"""

html = etree.HTML(text)
result = html.xpath('//bookstore/book[price > 30]/title/text()')
print('多属性匹配'.center(50,"-"))
print(result)
result = html.xpath('//bookstore/book[price > 30 and @author="sunchengquan"]/title/text()')
print(result)


