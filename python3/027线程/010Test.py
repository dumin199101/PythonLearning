#coding=utf-8
#ThreadLocal对象：解决线程中的传参问题，同时不同线程避免变量污染
import threading
#创建全局对象
local_obj = threading.local()
def test():
    name = local_obj.name
    print("name is %s,thread name is %s"%(name,threading.current_thread().name))

def process(name):
    local_obj.name = name
    test()

t1 = threading.Thread(target=process,name="Thread-One",args=("haha",))
t2 = threading.Thread(target=process,name="Thread-Two",args=("gaga",))
t1.start()
t2.start()
t1.join()
t2.join()


