#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#分布式进程：Worker进程
import time,sys,queue
from multiprocessing.managers import BaseManager
class QueueManager(BaseManager):
    pass
# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')
# 连接到服务器，也就是运行task_master.py的机器:
server_addr = '127.0.0.1'
print('Connect to Server:%s'%server_addr)
# 端口和验证码注意保持与task_master.py设置的完全一致:
manager = QueueManager(address=(server_addr,5000),authkey=b'abc')
# 从网络连接:
manager.connect()
# 获取Queue的对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 从task队列取任务,并把结果写入result队列:
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('run task %d * %d...' % (n, n))
        r = '%d * %d = %d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')
# 处理结束:
print('worker exit.')
