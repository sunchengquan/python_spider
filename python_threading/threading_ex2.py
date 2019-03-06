#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'


import time
import threading


class MyThread(threading.Thread):
    def __init__(self,n,sleep_time):
        super(MyThread,self).__init__()
        self.n =  n
        self.sleep_time = sleep_time
    def run(self):
        """
        函数名必须要写成“run”
        :return: None
        """
        print("runnint task ",self.n )
        time.sleep(self.sleep_time)
        print("task done,",self.n )

start_time = time.time()
t1 = MyThread("t1",2)
t2 = MyThread("t2",4)

t1.start()
t2.start()

t1.join() #=wait()
t2.join()
print("cost:",time.time() - start_time)
print("main thread....")
