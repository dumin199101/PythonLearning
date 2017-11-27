#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#面向对象高级：__slots__:限制对象属性
class Student(object):
    pass

#动态给对象绑定属性
s = Student()
s.name = "du"
print(s.name)

#动态给对象绑定一个方法
def set_age(self,age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)
s.set_age(25)
print(s.age)

#给一个实例绑定的方法对另一个实例不起作用
# s2 = Student()
# s2.set_age(22)
# print(s2.age)

#给class绑定方法
Student.set_age = set_age
s2 = Student()
s2.set_age(22)
print(s2.age)

#试用__slots__:限制对象的属性
class Person(object):
    __slots__ = ('name','age')

p = Person()
p.name = 'Michale'
p.age = 22
#p.score = 100 #此处报错

#__slots__仅对当前实例起作用，对其子类无效。除非在子类中也定义__slots__属性，否则就是子类+父类__slots__属性
class Worker(Person):
    pass
worker = Worker()
worker.job = "搬运"
print(worker.job)


