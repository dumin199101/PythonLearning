#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#创建多线程：threading模块：使用Lock保证线程共享变量的一致性
import time,threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n  #此处为多次操作，会发生线程安全问题
    balance = balance - n

def run_thread(n):
    for i in range(10000000):
        #先获取锁：
        lock.acquire()
        try:
            #放心的改吧
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

