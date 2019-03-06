#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
Semaphore(信号量)
厕所有3个坑，那最多只允许3个人上厕所，后面的人只能等里面有人出来了才能再进去
"""

import time
import threading


def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s" % n)
    semaphore.release()

if __name__ == '__main__':
    semaphore = threading.BoundedSemaphore(5)  # 最多允许5个线程同时运行
    for i in range(22):
        t = threading.Thread(target=run, args=(i,))
        t.start()

while threading.active_count() != 1:
       #print(threading.active_count())
    pass
else:
    print('----all threads done---')

