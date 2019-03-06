#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
css选择器，一种快速定位元素的方法
BeautifulSoup
scrapy
pyquery
支持css选择器
"""

"""
CSS 选择器常用规则
.class  .intro      选择 class="intro" 的所有元素
#id     #firstname  选择 id="firstname" 的所有元素
*                   选择所有元素
p                   选择所有 <p> 元素
div,p               选择所有 <div> 元素和所有 <p> 元素
div p               选择 <div> 元素内部的所有 <p> 元素
div > p             选择所有父级是div元素的p元素
[target]            选择带有 target 属性所有元素
[target=_blank]     选择 target="_blank" 的所有元素
[title~=flower]     选择 title 属性包含单词 "flower" 的所有元素
a[src*="abc"]       选择其 src 属性中包含 "abc" 子串的每个 <a> 元素
a[src^="https"]     选择其 src 属性值以 "https" 开头的每个 <a> 元素
a[src$=".pdf"]      选择其 src 属性以 ".pdf" 结尾的所有 <a> 元素
:not(p)             选择每个并非p元素的元素
p:first-child       指定只有当<p>元素是其父级的第一个子级的样式(第一个孩子)
p:first-of-type     选择每个p元素是其父级的第一个p元素（第一个儿子）
p:last-child        选择每个p元素是其父级的最后一个子级（最后一个孩子）
p:last-of-type      选择每个p元素是其父级的最后一个p元素（最后一个儿子）
p:only-child        选择每个p元素是其父级的唯一子元素（唯一的孩子）
p:only-of-type      选择每个p元素是其父级的唯一p元素（唯一的儿子）
p:nth-child(2)      选择每个p元素是其父级的第二子元素（第二个的孩子）
p:nth-of-type(2)    选择每个p元素是其父级的第二个p元素（第二个的儿子）
p:nth-last-child(2) 选择每个p元素的是其父级的第二个子元素，从最后一个子项计数
p:nth-last-of-type(2) 选择每个p元素的是其父级的第二个p元素，从最后一个子项计数
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
result = selector.cssselect('ul')
print(result)