#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/11/9:38'


"""
daemon
每个线程都可以单独设置它的属性，如果设置为True，当父进程结束后，子进程会自动被终止。
join
每个子进程都调用了join()方法，这样父进程（主进程）就会等待子进程执行完毕。
"""

import time
import multiprocessing
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, loop):
        Process.__init__(self)
        self.loop = loop

    def run(self):
        for count in range(self.loop):
            time.sleep(1)
            print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))


if __name__ == '__main__':
    for i in range(2, 5):
        p = MyProcess(i)
        p.daemon = True
        p.start()
        p.join()

    print('Main process Ended!')

