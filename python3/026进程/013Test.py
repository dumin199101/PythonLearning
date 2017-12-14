#coding=utf-8
#进程间通讯：在进程池中的应用
from multiprocessing import Pool,Manager
import time,random

#写数据进程
def write(q):
    for value in ['A','B','C']:
        print("PUT %s into queue"%value)
        q.put(value)
        time.sleep(random.random()*3)

#读数据进程：
def read(q):
           for i in range(q.qsize()):
               value = q.get(True)
               print("GET %s from queue"%value)

q = Manager().Queue()
pool = Pool()
#使用阻塞式创建,不用在read中使用死循环了
pool.apply(write,(q,))
pool.apply(read,(q,))
pool.close()
pool.join()
