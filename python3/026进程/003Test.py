#coding=utf-8
#全局变量在进程间不共享
import os
g_num = 100
res = os.fork()
if res==0:
    print("process1")
    g_num+=1
    print("g_num is %d"%g_num)
else:
    print("process2")
    print("g_num is %d" % g_num)
