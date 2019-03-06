#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
代理设置
"""
import requests

# proxies = {
#     "http": "http://10.10.1.10:3128",
#     "https": "http://10.10.1.10:1080",
# }
#
# requests.get("https://www.taobao.com", proxies=proxies)



#若代理需要使用HTTP Basic Auth，可以使用类似http://user:password@host:port这样的语法来设置代理
# proxies = {
#     "http": "http://user:password@10.10.1.10:3128/",
# }
# requests.get("https://www.taobao.com", proxies=proxies)

#requests还支持SOCKS协议的代理 pip3 install 'requests[socks]'

# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
# requests.get("https://www.taobao.com", proxies=proxies)






