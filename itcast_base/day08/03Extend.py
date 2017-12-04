#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#子类不能继承父类私有属性跟私有方法
class Person(object):
    def __init__(self,name,age,addr):
        print("object is created")
        self.__name = name
        self.__age = age
        self.addr = addr
    def __del__(self):
        print("object is destroyed")
    def getInfo(self):
        print("good good study!")
    def __getInfo(self):
        print("day day up!")
class Student(Person):
    def printInfo(self):
        print(self.__name,self.__age,self.addr)
student = Student("du",22,"中国")
student.getInfo()
# student.printInfo() 报错
# student.__getInfo() 报错