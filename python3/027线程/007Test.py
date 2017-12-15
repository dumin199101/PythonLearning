#coding=utf-8
from threading import Lock,Thread
import time
#死锁问题：你等我我等你，陷入死循环
#解决死锁：加入超时时间,使阻塞等待取消
def test1():
    if g_lockA.acquire():
        print("test1......")
        time.sleep(1)
        if g_lockB.acquire(timeout=1):
            print("test1------test2")
            g_lockB.release()
        g_lockA.release()


def test2():
    if g_lockB.acquire():
        print("test2......")
        time.sleep(1)
        if g_lockA.acquire(timeout=1):
            print("test2------test1")
            g_lockA.release()
        g_lockB.release()

g_lockA = Lock()
g_lockB = Lock()

t1 = Thread(target=test1)
t2 = Thread(target=test2)

t1.start()
t2.start()