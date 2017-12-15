#coding=utf-8
from threading import Lock,Thread
import time
#死锁问题：你等我我等你，陷入死循环
#流程：t1先执行，用LockA加锁，打印test1....接着t2执行，用LockB加锁，打印test2,紧接着t1再执行时发现B上锁了，就阻塞等待
#LockB锁释放，接着执行t2,发现LockA上锁，就阻塞等待LockA释放，这样就形成了死锁
def test1():
    if g_lockA.acquire():
        print("test1......")
        time.sleep(1)
        if g_lockB.acquire():
            print("test1------test2")
            g_lockB.release()
        g_lockA.release()


def test2():
    if g_lockB.acquire():
        print("test2......")
        time.sleep(1)
        if g_lockA.acquire():
            print("test2------test1")
            g_lockA.release()
        g_lockB.release()

g_lockA = Lock()
g_lockB = Lock()

t1 = Thread(target=test1)
t2 = Thread(target=test2)

t1.start()
t2.start()