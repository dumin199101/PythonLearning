#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#继承object类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print('%s:%s'%(self.name,self.age))

bart = Student('Bart Simpson', 59)
bart.print()
