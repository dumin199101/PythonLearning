#coding=utf-8
#线程共享全局变量
import threading,time
g_num = 100
def test1():
    for i in range(3):
        global g_num
        g_num+=1
        time.sleep(1)
    print("test1中的g_num is %s"%g_num)

def test2():
    print("test2中的g_num is %s" % g_num)

print("初始化的g_num is %s"%g_num)
t1 = threading.Thread(target=test1)
t1.start()
time.sleep(5)
t2 = threading.Thread(target=test2)
t2.start()
