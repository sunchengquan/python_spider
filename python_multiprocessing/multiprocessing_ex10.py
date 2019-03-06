#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/10/17:48'


"""
进程间通信

Process 之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python 的 multiprocessing 模块包装了底层的机制，
提供了队列(Queue)、管道(Pipes)等多种方式来交换数据。

我们以队列(Queue)为例，在父进程中创建两个子进程，一个往队列里写数据，一个从队列里读数据：

"""

import os, time, random
from multiprocessing import Process, Queue



# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)




if __name__ == '__main__':
    q = Queue()  # 父进程创建 Queue，并传给各个子进程：
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动子进程 pw，写入
    pr.start()  # 启动子进程 pr，读取
    pw.join()  # 等待pw结束
    pr.terminate()  # pr进程里是死循环，无法等待其结束，只能强行终止:

