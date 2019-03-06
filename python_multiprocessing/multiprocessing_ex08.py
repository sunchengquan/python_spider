#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'sunchengquan'
__mail__ = '1641562360@qq.com'
__date__ = '2018/9/10/17:37'


"""
进程池 Pool

如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
apply_async(func[, args[, kwds[, callback]]]) 它是非阻塞，apply(func[, args[, kwds]])是阻塞的。
close() 关闭pool，使其不在接受新的任务。
terminate() 结束工作进程，不在处理未完成的任务。
join() 主进程阻塞，等待子进程的退出， join方法要在close或terminate之后使用。
"""

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)  # 设置进程池大小
    for i in range(5):
        p.apply(long_time_task, args=(i,))  # 设置每个进程要执行的函数和参数


    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
