#coding=utf-8
#通过Process子类创建子进程
from multiprocessing import Process
import time
class ChildProcess(Process):
    def __init__(self):
        super().__init__()
        print("Child is start")
    #定义run方法
    def run(self):
        while True:
            print("Im child")
            time.sleep(1)

p = ChildProcess()
p.start()

#父进程：
while True:
    print("Im parent")
    time.sleep(1)