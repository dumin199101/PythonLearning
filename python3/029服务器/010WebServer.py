#coding=utf-8
#gevent版本的服务器
#gevent:检测耗时操作，将控制权交出,给其它协程
from gevent import monkey; monkey.patch_socket()
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        gevent.sleep(1)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

# <Greenlet at 0x29ce0e0: f(5)> 0
# <Greenlet at 0x29ce638: f(5)> 0
# <Greenlet at 0x29ce6d0: f(5)> 0
# <Greenlet at 0x29ce0e0: f(5)> 1
# <Greenlet at 0x29ce6d0: f(5)> 1
# <Greenlet at 0x29ce638: f(5)> 1
# <Greenlet at 0x29ce0e0: f(5)> 2
# <Greenlet at 0x29ce638: f(5)> 2
# <Greenlet at 0x29ce6d0: f(5)> 2
# <Greenlet at 0x29ce0e0: f(5)> 3
# <Greenlet at 0x29ce6d0: f(5)> 3
# <Greenlet at 0x29ce638: f(5)> 3
# <Greenlet at 0x29ce0e0: f(5)> 4
# <Greenlet at 0x29ce638: f(5)> 4
# <Greenlet at 0x29ce6d0: f(5)> 4