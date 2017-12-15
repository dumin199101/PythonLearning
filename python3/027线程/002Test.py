#coding=utf-8
#通过继承Thread类的子类创建线程,线程的执行顺序跟调度算法相关，与创建顺序无关
import threading,time
class MyThread(threading.Thread):
    def run(self):
        for i in range(3):
            msg = "I'm"+self.name+"@"+str(i)
            time.sleep(1)
            print(msg)

for i in range(5):
    t = MyThread()
    t.start()