#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


"""
属性匹配
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

selector = etree.HTML(text)
result = selector.xpath('//li[@class="item-0"]')
print('属性匹配'.center(50,"-"))
print(result)



"""
文本获取

想获取li节点内部的文本，就有两种方式：
一种是选取a节点再获取文本
另一种就是使用//

"""

result = selector.xpath('//li[@class="item-0"]/text()')
print('文本获取'.center(50,"-"))
print(result)


print('-'*50)
result = selector.xpath('//li[@class="item-0"]/a/text()')
print(result)

print('-'*50)
result = selector.xpath('//li[@class="item-0"]//text()')
print(result)

#属性获取
print('-'*50)
result = selector.xpath('//li/a/@href')
print(result)





html1 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test-1">需要的内容1</div>
    <div id="test-2">需要的内容2</div>
    <div id="testfault">需要的内容3</div>
</body>
</html>
'''

html2 = '''
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title></title>
</head>
<body>
    <div id="test3">
        我左青龙，
        <span id="tiger">
            右白虎，
            <ul>上朱雀，
                <li>下玄武。</li>
            </ul>
            老牛在当中，
        </span>
        龙头在胸口。
    </div>
</body>
</html>
'''

selector = etree.HTML(html1)
content = selector.xpath('//div[starts-with(@id,"test")]/text()')
for each in content:
    print(each)

print('-'*50)
selector = etree.HTML(html2)
content_1 = selector.xpath('//div[@id="test3"]/text()')
for each in content_1:
    print(each)
print('-'*50)


data = selector.xpath('//div[@id="test3"]')[0]
print(data)
info = data.xpath('string(.)')
print(info)
content_2 = info.replace('\n','').replace(' ','')
print(content_2)