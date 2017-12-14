#coding=utf-8
#进程
#调度算法：
#   时间片轮转，优先级调度
#并发：4个CPU同时执行8个程序
#并行：4个CPU同时执行4个程序
#主进程：返回子进程的ID
#子进程：返回0
import os
res = os.fork()
if res==0:
    print("子进程,ID:%d,ParentID:%d"%(os.getpid(),os.getppid()))
else:
    print("父进程,ID:%d"%os.getpid())
