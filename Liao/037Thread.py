#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#ThreadLocal保存线程局部变量，任意读写互不干扰,不用做复杂的参数传递
import threading
# 创建全局ThreadLocal对象:
local_var = threading.local()
def process_student():
    # 获取当前线程关联的student:
    std = local_var.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def  process_thread(name):
    # 绑定ThreadLocal的student:
    local_var.student = name
    process_student()

t1 = threading.Thread(target=process_thread,args=('Alice',),name='Thread-1')
t2 = threading.Thread(target=process_thread,args=('Bob',),name='Thread-2')
t1.start()
t2.start()
t1.join()
t2.join()