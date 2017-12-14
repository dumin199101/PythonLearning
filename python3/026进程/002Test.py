#coding=utf-8
#多进程demo
import os
import time
res = os.fork()
if res==0:
    while True:
        print(1)
        time.sleep(1)
else:
    while True:
        print(2)
        time.sleep(1)