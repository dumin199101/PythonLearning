#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#获取对象信息：
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print(self):
        print('%s:%s'%(self.name,self.age))

bart = Student('Bart Simpson', 59)
bart.print()

print(isinstance(bart,Student))
print(dir(bart)) #获取对象的属性跟方法
print(hasattr(bart,'name'))
print(getattr(bart,'name'))
setattr(bart,'age',22)
print(getattr(bart,'age'))