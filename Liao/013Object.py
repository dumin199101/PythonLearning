#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#访问限制
class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def print(self):
        print('%s:%s'%(self.__name,self.__age))
    def get_name(self):
        print("Name:",self.__name)

bart = Student('Bart Simpson', 59)
bart.print()
#print(bart.__name) 访问报错
bart.get_name()
