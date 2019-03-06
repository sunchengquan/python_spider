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
import multiprocessing


# 写数据进程执行的代码:
def writer(q):
    print('Process of writer: %s' % os.getpid())
    for value in ['A', 'B', 'C',"D"]:
        print('Put %s to queue...' % value)
        q.put(value)



# 读数据进程执行的代码:
def reader(q,name):
    print('Process of reader%d: %s' % (name,os.getpid()))

    while 1:
        if not q.empty():
            time.sleep(random.random())
            try:
                value = q.get(timeout=1)
                if value == 'D':
                    q.put('E')
            except Exception as e:
                print(e)
                break
            print('Reader%d get %s from queue.' % (name , value))
        else:
            break

if __name__ == '__main__':
    manager = multiprocessing.Manager()
    q = manager.Queue()
    p = multiprocessing.Pool(2)
    pw = p.apply_async(writer, args=(q,))
    time.sleep(0.5)
    pr = p.apply_async(reader, args=(q, 1))
    pr1 = p.apply_async(reader, args=(q, 2))
    p.close()
    p.join()

    print('end')

