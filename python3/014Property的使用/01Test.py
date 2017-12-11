#coding=utf-8
#property的使用：自动调用getter,setter方法：
class Person(object):
    def __init__(self):
        self.__num = 100
    def getNum(self):
        return  self.__num
    def setNum(self,num):
        self.__num = num
    num = property(getNum,setNum)

p = Person()
print(p.num)
p.num = 200
print(p.num)