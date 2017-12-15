#coding=utf-8
#GIL（全局解释器锁）：同一时刻只有一个进程在执行，为解决这个问题使用C来解决：
# include "stdio.h"
# int main(){
#    printf("hello world");
#    return 0;
# }

#执行 gcc test.c  ---->a.out 执行即可
#编译库文件：gcc test.c -shared -o xxx.lib.so

from ctypes import *
from threading import Thread

#加载动态库：
lib = cdll.LoadLibrary("./loop.lib.so")
#子进程使用C来执行
t = Thread(target=lib.deadLoop)
t.start()
#主进程使用Python
while True:
    pass



