#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#多进程与多线程
# 总结一下就是，多任务的实现有3种方式：
#     多进程模式；
#     多线程模式；
#     多进程+多线程模式。

#fork()调用一次，返回两次。子进程永远返回0，父进程返回子进程ID，子进程只需要调用getppid()就可以拿到父进程的ID

import os

print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))