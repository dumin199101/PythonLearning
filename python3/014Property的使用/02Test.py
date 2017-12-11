#coding=utf-8
#property的使用：自动调用getter,setter方法：
class Person(object):
    def __init__(self):
        self.__num = 100
    @property
    def num(self):
        return  self.__num
    @num.setter
    def num(self,num):
        self.__num = num


p = Person()
print(p.num)
p.num = 200
print(p.num)