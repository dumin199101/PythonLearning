#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#析构方法：__del__
#生效：1.程序运行完毕 2.变量引用销毁：
class Person(object):
    def __init__(self):
        print("object is created")
    def __del__(self):
        print("object is destroyed")
person = Person();
print("1")
person2 = person
person3 = person
del person,person2,person3
print("2")

# object is created
# 1
# object is destroyed
# 2
