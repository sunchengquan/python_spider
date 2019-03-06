#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'

"""
事件处理的机制：
全局定义了一个“Flag”，如果“Flag”值为 False，那么当程序执行 event.wait 方法时就会阻塞；
如果“Flag”值为True，那么执行event.wait 方法时便不再阻塞。
clear：将“Flag”设置为False
set：将“Flag”设置为True

通过Event来实现两个或多个线程间的交互，
下面是一个红绿灯的例子，即起动一个线程做交通指挥灯，生成几个线程做车辆，车辆行驶按红灯停，绿灯行的规则
"""
import time
import threading

event = threading.Event()

def lighter():
    count = 0
    event.set() #先设置绿灯
    while True:
        if count >5 and count < 10: #改成红灯
            event.clear() #把标志位清了
            print("\033[41;1mred light is on....\033[0m")
        elif count >10:
            event.set() #变绿灯
            count = 0
        else:
            print("\033[42;1mgreen light is on....\033[0m")
        time.sleep(1)
        count +=1

def car(name):
    while True:
        if event.is_set(): #代表绿灯
            print("[%s] running..."% name )
            time.sleep(1)
        else:
            print("[%s] sees red light , waiting...." %name)
            event.wait()
            print("\033[34;1m[%s] green light is on, start going...\033[0m" %name)


light = threading.Thread(target=lighter,)
light.start()

car1 = threading.Thread(target=car,args=("Tesla",))
car1.start()


