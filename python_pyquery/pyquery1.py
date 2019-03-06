#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

html = '''
<div>
    <ul>
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
'''
from pyquery import PyQuery as pq
import requests
# doc = pq(html)
# print(doc('li'))



# doc = pq(url='http://cuiqingcai.com')
# print(doc('title'))


doc = pq(requests.get('https://www.ncbi.nlm.nih.gov/gene/1559').text.encode('utf-8'))
print(doc('title'))

doc = pq(filename='result.html')
print(doc('title'))

