#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
GET请求
"""
import re
import requests

# r = requests.get('http://httpbin.org/get')
# print(r.text)


# 参数
# r = requests.get('http://httpbin.org/get?name=germey&age=22')
# print(r.text)


# data = {
#     'name': 'germey',
#     'age': 22
# }
# r = requests.get("http://httpbin.org/get", params=data)
# print(r.text)

#JSON格式的
# r = requests.get("http://httpbin.org/get")
# print(type(r.text))
# print(r.json())
# print(type(r.json()))


#添加headers
# r = requests.get("https://www.zhihu.com/explore")
# print(r.text)
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("https://www.zhihu.com/explore", headers=headers)
print(r.text)





#抓取网页
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
# }
# r = requests.get("https://www.zhihu.com/explore", headers=headers)
# pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
# titles = re.findall(pattern, r.text)
# print(titles)

#抓取二进制数据
# r = requests.get("https://github.com/favicon.ico")
# print(r.text)
# print(r.content)
# with open('favicon.ico', 'wb') as f:
#     f.write(r.content)

