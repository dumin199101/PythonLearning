#coding=utf-8
#协程：底层是生成器。进程中有线程，线程中有协程。进程跟线程占用CPU资源，会做任务切换，效率低。
#IO密集型：需要网络功能，大量等待网络数据到来（多线程、协程），计算密集型：占用大量CPU资源（多进程）
# pip install greenlet
# greenlet实现多任务，实现手动切换控制
from greenlet import greenlet
import time
def test1():
    while True:
        print("---------A-------------")
        g2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print("---------B-------------")
        g1.switch()
        time.sleep(0.5)

g1 = greenlet(test1)
g2 = greenlet(test2)
g1.switch()