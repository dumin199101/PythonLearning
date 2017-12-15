#coding=utf-8
#异步：主进程不确定什么时候执行回调，在执行别的任务时，如果接受到回调信号，立马执行
from multiprocessing import Pool
import os,time
def test1(args):
    print("-----pid------:%s"%os.getpid())
    print("-----args-----:%s"%args)


def test2():
    print("进程池中的进程：pid=%s,ppid=%s"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("-----%d------"%i)
        time.sleep(1)
    return "Hello World"

pool = Pool()
pool.apply_async(func=test2,callback=test1)
#主进程：
while True:
    time.sleep(1)
    print("主进程PID：%s"%os.getpid())