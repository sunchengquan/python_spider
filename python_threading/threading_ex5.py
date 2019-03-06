__author__ = "Alex Li"

"""
Join & Daemon
将m线程设置为Daemon线程,它做为程序主线程的守护线程,当主线程退出时,m线程也会退出,
由m启动的其它子线程会同时退出,不管是否执行完任务
"""

import time
import threading


def run(n):
    print("task ",n )
    time.sleep(2)
    print("task done",n,threading.current_thread())

start_time = time.time()
t_objs = [] #存线程实例
for i in range(50):
    t = threading.Thread(target=run,args=("t-%s" %i ,))
    t.setDaemon(True) #把当前线程设置为守护线程
    t.start()
    t_objs.append(t) #为了不阻塞后面线程的启动，不在这里join，先放到一个列表里

# for t in t_objs: #循环线程实例列表，等待所有线程执行完毕
#     t.join()

time.sleep(2)
print("----------all threads has finished...",threading.current_thread(),threading.active_count())
print("cost:",time.time() - start_time)
