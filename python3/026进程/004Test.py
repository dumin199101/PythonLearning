#coding=utf-8
#对比多个fork:如果在外边是4个进程
import os
res = os.fork()
if res==0:
    print(1)
else:
    print(2)
res = os.fork()
if res==0:
    print(11)
else:
    print(22)
