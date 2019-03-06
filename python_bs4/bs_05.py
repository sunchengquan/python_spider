#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/11/14:13'

"""
节点选择器
关联选择：需要先选中某一个节点元素，然后以它为基准再选择它的子节点、父节点、兄弟节点等，这里就来介绍如何选择这些节点元素
"""
from bs4 import BeautifulSoup


html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            Hello
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a><a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

#获取它的直接子节点
soup = BeautifulSoup(html, 'lxml')
# print(soup.p.contents)


# print(soup.p.children)
# for i, child in enumerate(soup.p.children):
#     print(i, child)

#所有的子孙节点的话，可以调用descendants属性
# print(soup.p.descendants)
# for i, child in enumerate(soup.p.descendants):
#     print(i, child)

# 父节点
# print(soup.a.parent)

#向外寻找父节点的祖先节点
# print(type(soup.a.parents))
# print(list(enumerate(soup.a.parents)))


#兄弟节点
# print('Next Sibling', soup.a.next_sibling)
# print('Prev Sibling', soup.a.previous_sibling)
# print('Next Siblings', list(enumerate(soup.a.next_siblings)))
# print('Prev Siblings', list(enumerate(soup.a.previous_siblings)))

# 兄弟节点和属性选择
print('Next Sibling', soup.find(id = 'link2').next_sibling)
print('Prev Siblings', soup.find(id = 'link2').previous_sibling)


#提取信息
print('Next Sibling:', soup.find(id = 'link2').next_sibling.string.strip())
print('Next Sibling:', soup.find(id = 'link2').next_sibling.attrs['href'].strip())