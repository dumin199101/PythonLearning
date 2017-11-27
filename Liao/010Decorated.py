#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#装饰器
def now():
    print("2017-09-01")
f = now
f()
#通过__name__属性来获取函数名
print(now.__name__)
print(f.__name__)

#增强now函数的功能：代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
    def wrapper(*args,**kw):
        print('call %s():'%func.__name__) #实现打印
        return func(*args,**kw) #调用原始函数
    return wrapper

@log
def now1():
    print("2017-09-01")
#相当于执行了now1 = log(now1)
now1()
