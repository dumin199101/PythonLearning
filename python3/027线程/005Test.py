#使用互斥锁解决线程共享全局变量的问题
from threading import Thread,Lock

g_num = 0

def test1():
    global g_num
    #加锁
    g_lock.acquire()
    for i in range(1000000):
        g_num += 1
    #释放锁
    g_lock.release()

    print("---test1---g_num=%d"%g_num)

def test2():
    global g_num
    g_lock.acquire()
    for i in range(1000000):
        g_num += 1
    g_lock.release()
    print("---test2---g_num=%d"%g_num)


g_lock = Lock()

p1 = Thread(target=test1)
p1.start()


p2 = Thread(target=test2)
p2.start()

print("---g_num=%d---"%g_num)