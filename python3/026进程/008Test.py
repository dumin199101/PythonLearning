#coding=utf-8
#Process创建多进程
#终止进程
import time
from multiprocessing import Process
def test(num):
    for i in range(5):
        print("-------",num)
        time.sleep(1)

p = Process(target=test,args=(10,))
#开启进程
p.start()
#终止进程
p.terminate()
print("main")