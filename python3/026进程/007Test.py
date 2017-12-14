#coding=utf-8
#Process创建多进程
#子进程执行完再执行主进程
import time
from multiprocessing import Process
def test(num):
    for i in range(5):
        print("-------",num)
        time.sleep(1)

p = Process(target=test,args=(10,))
#开启进程
p.start()
p.join()
print("main")
