#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


import time
import threading


class MyThread(threading.Thread):
    """
    继承父类threading.Thread
    """
    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        """
        函数名必须要写成“run”
        把要执行的代码写到run函数里面 线程在创建后会直接运行run函数
        :return: None
        """
        print("Starting " + self.name)
        print_time(self.name, self.delay, 5)
        print( "Exiting " + self.name)



def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = MyThread(1, "Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# 开启线程
thread1.start()
thread2.start()

print("Exiting Main Thread")

