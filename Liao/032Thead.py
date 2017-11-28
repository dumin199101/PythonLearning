#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#多进程与多线程:multiprocessing模块的Process类实现
from multiprocessing import Process
import os
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')
