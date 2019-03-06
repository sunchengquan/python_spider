#!/usr/bin/env python
# -*- coding: utf-8 -*-
__date__ = '2018/9/12'
__author__ = 'sunchengquan'
__mail__ = 'sunchq14@lzu.edu.cn'


"""
SSL证书验证
"""

import requests
import logging
from requests.packages import urllib3

# response = requests.get('https://www.12306.cn')
# print(response.status_code)



# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


#不过我们发现报了一个警告，它建议我们给它指定证书。我们可以通过设置忽略警告的方式来屏蔽这个警告
# urllib3.disable_warnings()
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)

#或者通过捕获警告到日志的方式忽略警告
# logging.captureWarnings(True)
# response = requests.get('https://www.12306.cn', verify=False)
# print(response.status_code)


#指定一个本地证书用作客户端证书，这可以是单个文件（包含密钥和证书）或一个包含两个文件路径的元组
# response = requests.get('https://www.12306.cn', cert=('/path/server.crt', '/path/key'))
# print(response.status_code)


