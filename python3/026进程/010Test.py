#coding=utf-8
#进程池创建子进程
from multiprocessing import Pool
import os,random,time

def worker(msg):
    t_start = time.time()
    print("%s开始执行，进程号为：%d"%(msg,os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,运行耗时%0.2f秒"%(t_stop-t_start))

pool = Pool(3)
for i in range(10):
    pool.apply_async(worker,(i,))

print("---start----")
pool.close()
pool.join()
print("---end---")

