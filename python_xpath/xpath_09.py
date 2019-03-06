#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
XPath 轴
节点轴选择

ancestor 	        选取当前节点的所有先辈（父、祖父等）。
ancestor-or-self 	选取当前节点的所有先辈（父、祖父等）以及当前节点本身。
attribute 	        选取当前节点的所有属性。
child 	            选取当前节点的所有子元素。
descendant 	        选取当前节点的所有后代元素（子、孙等）。
descendant-or-self 	选取当前节点的所有后代元素（子、孙等）以及当前节点本身。
following 	        选取文档中当前节点的结束标签之后的所有节点。
namespace 	        选取当前节点的所有命名空间节点。
parent 	            选取当前节点的父节点。
preceding 	        选取文档中当前节点的开始标签之前的所有节点。
preceding-sibling 	选取当前节点之前的所有同级节点。
self 	            选取当前节点。
"""
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html"><span>first item</span></a></li>
         <li class="item-0"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print('获取所有祖先节点'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/ancestor::div')
print('只有div这个祖先节点'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/attribute::*')
print('第一个li节点的所有属性值'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print('属性为link1.html所有直接子节点'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/descendant::span')
print('只包含span节点而不包含a节点所有子孙节点'.center(50,"-"))
print(result)


result = html.xpath('//li[1]/following::*[2]/text()')
print('当前节点之后的所有节点,索引选择第二个'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/following::*[1]/@class')
print('当前节点之后的所有节点,索引选择第一个'.center(50,"-"))
print(result)

result = html.xpath('//li[1]/following-sibling::*')
print('获取当前节点之后的所有同级节点'.center(50,"-"))
print(result)

result = html.xpath('//li[4]/preceding-sibling::*[1]/@class')
print('获取当前节点之前的所有同级节点第一个'.center(50,"-"))
print(result)

result = html.xpath('//li[4]/preceding-sibling::li[@class="item-0"]//text()')
print('获取当前节点之前的所有同级节点中class属性值为item-0'.center(50,"-"))
print(result)

result = html.xpath('//li[4]/preceding-sibling::li[@class="item-0" and position()=2]//text()')
print('获取当前节点之前的所有同级节点中class属性值为item-0且第二个位置'.center(50,"-"))
print(result)


result = html.xpath('//li[4]/preceding-sibling::li[//text()="second item" and position()=2]/@class')
print('获取当前节点之前的所有同级节点中class属性值为item-0且第二个位置'.center(50,"-"))
print(result)

