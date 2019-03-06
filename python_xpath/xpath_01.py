#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
XPath，全称XML Path Language，即XML路径语言，
它是一门在XML文档中查找信息的语言。它最初是用来搜寻XML文档的，但是它同样适用于HTML文档的搜索
更多用法：官网：http://www.w3school.com.cn/xpath
"""

"""
XPath常用规则
路径表达式
/    从当前节点选取直接子节点
//   从当前节点选取子孙节点
.    选取当前节点
..   选取当前节点的父节点
@    选取属性

谓语（备注/补充说明）
/bookstore/book[1]              选取属于bookstore子元素的第一个book元素
/bookstore/book[last()]         选取属于bookstore子元素的最后一个book元素
/bookstore/book[last()-1]       选取属于bookstore子元素的倒数第二个book元素
/bookstore/book[position()<3]   选取最前面的两个属于bookstore子元素的book元素
//title[@lang]                  选取所有拥有名为lang的属性的title元素
//title[@lang='eng']            选取所有title元素,且这些元素拥有值为eng的lang属性

通配符
*  匹配任何元素节点
@* 匹配任何属性节点


选取若干路径
//book/title | //book/price   选取book元素的所有title和price元素
//title  | //price            选取文档中的所有title和price元素
/bookstore/book/title | //price  选取属于bookstore元素的book元素的所有title元素，以及文档中的所有的price元素

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
html = etree.HTML(text)
#调用tostring()方法即可输出修正后的HTML代码
result = etree.tostring(html)
#结果是bytes类型，decode（）方法转换成str类型
print(result.decode('utf-8'))
print(html)




