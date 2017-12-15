#coding=utf-8
#线程同步：保证按顺序执行：
from threading import Thread,Lock
class Test1(Thread):
    def run(self):
        while True:
            #加锁，如果锁未释放，那么不能加锁
            if a.acquire():
                print("----taskA-----")
                b.release()

class Test2(Thread):
    def run(self):
        while True:
            #加锁，如果锁未释放，那么不能加锁
            if b.acquire():
                print("----taskB-----")
                c.release()


class Test3(Thread):
    def run(self):
        while True:
            #加锁，如果锁未释放，那么不能加锁
            if c.acquire():
                print("----taskC-----")
                a.release()

t1 = Test1()
a = Lock()
t1.start()

t2 = Test2()
b = Lock()
b.acquire()
t2.start()

t3 = Test3()
c = Lock()
c.acquire()
t3.start()

