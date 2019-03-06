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
import threading
import os, time, random
from multiprocessing import Process, Queue


# 写数据进程执行的代码:
def writer(q):
    print('Process of writer: %s' % os.getpid())
    for value in ['A', 'B', 'C', "D", 'A', 'B', 'C', "D", 'A', 'B', 'C', "D", "D"]:
        print('Put %s to queue...' % value)
        q.put(value)


# 读数据进程执行的代码:
def reader(q1, name,thread_num):
    time.sleep(2)
    while not q1.empty():
        try:
            value = q1.get(timeout=3)
            if value == "D":
                q1.put("E")
        except Exception as e:
            break
            # print("xxxxx:", e)
            # exit(0)
        print('Reader%d , process[%s] thread-%s get %s from queue. ' % (name, os.getpid(), thread_num, value))


def thread(q1, name):
    threads = []
    while not q1.empty():
        for thread in threads:
            if not thread.is_alive():
                threads.remove(thread)
        thread_num = 1
        while len(threads) < 2:
            thread = threading.Thread(target=reader, args=(q1, name, thread_num))
            thread.setDaemon(True)
            thread.start()
            threads.append(thread)
            thread_num += 1
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    q1 = Queue()
    pw = Process(target=writer, args=(q1,))
    pw.start()
    pw.join()

    p = []
    for i in range(2):
        pr = Process(target=thread, args=(q1, i+1))
        pr.start()
        p.append(pr)
    for i in p:
        i.join()

    print('finish')

