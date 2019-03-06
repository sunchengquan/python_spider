#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/11/14:13'

"""
方法选择器
find_all()
"""
from bs4 import BeautifulSoup


html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''



soup = BeautifulSoup(html, 'lxml')

#根据节点名来查询元素
# print(soup.find_all(name='ul'))
# print(type(soup.find_all(name='ul')[0]))

# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))

# for ul in soup.find_all(name='ul'):
#     print(ul.find_all(name='li'))
#     for li in ul.find_all(name='li'):
#         print(li.string)

#属性来查询
# print(soup.find_all(attrs={'id': 'list-1'}))
# print(soup.find_all(attrs={'name': 'elements'}))    # print(soup.find_all(name='element'))

# print(soup.find_all(id='list-1',class_='list'))
# print(soup.find_all(class_='element'))



#匹配节点的文本
#text参数可用来匹配节点的文本，传入的形式可以是字符串，可以是正则表达式对象
import re
html = '''
<div class="panel">
    <div class="panel-body">
        <a name='sun' id='link1'>Hello, this is a link</a>
        <a class='s1 s2'>Hello, this is a link, too</a>
        <a class='s1'>Hello, sun</a>
    </div>
</div>
'''

soup = BeautifulSoup(html, 'lxml')
# print(soup.find_all(text=re.compile('link')))


#多属性查询
print(soup.find_all(id=re.compile('link'),attrs={'name':'sun'}))

#多值属性
print(soup.find_all('a'))
print(soup.find_all('a',class_='s1'))
print(soup.find_all('a',class_='s2'))
print(soup.find_all('a',class_='s1 s2'))
print(soup.find_all('a',class_='s2 s1'))
