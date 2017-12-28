#coding=utf-8
#gevent版本的服务器
#gevent:检测耗时操作，将控制权交出,给其它协程。自动切换
#猴子补丁：将标准库切换到对应的gevent库
from gevent import monkey; monkey.patch_all()
import gevent

def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)

g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()

# <Greenlet at 0x2d310e0: f(5)> 0
# <Greenlet at 0x2d310e0: f(5)> 1
# <Greenlet at 0x2d310e0: f(5)> 2
# <Greenlet at 0x2d310e0: f(5)> 3
# <Greenlet at 0x2d310e0: f(5)> 4
# <Greenlet at 0x2d31210: f(5)> 0
# <Greenlet at 0x2d31210: f(5)> 1
# <Greenlet at 0x2d31210: f(5)> 2
# <Greenlet at 0x2d31210: f(5)> 3
# <Greenlet at 0x2d31210: f(5)> 4
# <Greenlet at 0x2d312a8: f(5)> 0
# <Greenlet at 0x2d312a8: f(5)> 1
# <Greenlet at 0x2d312a8: f(5)> 2
# <Greenlet at 0x2d312a8: f(5)> 3
# <Greenlet at 0x2d312a8: f(5)> 4