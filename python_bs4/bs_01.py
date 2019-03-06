#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

# 首先必须要导入 bs4 库

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
# 创建 beautifulsoup 对象
# soup = BeautifulSoup(html)
soup = BeautifulSoup(html, 'lxml')

# 另外，我们还可以用本地 HTML 文件来创建对象，例如

# soup = BeautifulSoup(open('index.html'))


# 下面我们来打印一下 soup 对象的内容，格式化输出

print(soup.prettify())
print(soup.title.string)


"""
Beautiful Soup支持的解析器
BeautifulSoup(markup, "html.parser")
BeautifulSoup(markup, "lxml")
BeautifulSoup(markup, "xml")
BeautifulSoup(markup, "html5lib")
"""