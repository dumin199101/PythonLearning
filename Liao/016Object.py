#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#实例属性&类属性
class Student(object):
    score = 100
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    def print(self):
        print('%s:%s:%s'%(self.name,self.age,self.score))

bart = Student('Bart Simpson', 59,90)
print(bart.score)
bart.print()
print(Student.score)
bart.score = 50
print(bart.score) #此时访问的是实例属性
del bart.score
print(bart.score) #此时访问的是类属性
