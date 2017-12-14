#coding=utf-8
#进程间通讯：
from multiprocessing import Process,Queue
import time,random

#写数据进程
def write(q):
    for value in ['A','B','C']:
        print("PUT %s into queue"%value)
        q.put(value)
        time.sleep(random.random()*3)

#读数据进程：
def read(q):
   while True:
       if not q.empty():
           value = q.get(True)
           print("GET %s from queue"%value)
       else:
           break

q = Queue()
pw = Process(target=write,args=(q,))
pr = Process(target=read,args = (q,))
pw.start()
pw.join()
pr.start()
pr.join()