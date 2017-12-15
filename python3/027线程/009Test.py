#coding=utf-8
#生产者与消费者模式：在配置不均的情况下达到生产与消费均衡状态
from queue import Queue
from threading import Thread
import time
#生产者
class Producer(Thread):
    def run(self):
        count = 1
        while True:
            if q.qsize()<1000:
                for i in range(100):
                    name = "生产产品"+str(count)
                    print(name)
                    count+=1
                    q.put(i)
            time.sleep(1)

#消费者
class Consumer(Thread):
    def run(self):
        while True:
            if q.qsize()>100:
                for i in range(3):
                    print(self.name+"消费产品"+str(q.get(True)))
            time.sleep(1)



#初始化：
q = Queue()
for i in range(500):
    q.put("初始化产品"+str(i))

for i in range(2):
    p = Producer()
    p.start()

for i in range(8):
    c = Consumer()
    c.start()