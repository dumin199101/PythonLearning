#coding=utf-8
#多线程：主线程跟子线程同时执行
import threading,time
def test():
    time.sleep(5)
    print("child thread...")

for i in range(5):
    t = threading.Thread(target=test)
    t.start()

#主线程：
print("main thread")
print("end")
