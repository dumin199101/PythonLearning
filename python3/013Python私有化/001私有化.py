#coding=utf-8
#Python私有化
#xx:公共变量
#_xx:from 模块 import * f方式导入时，禁止其它模块使用，但是如果是import 模块名时仍然可以使用
#__xx:无法在外部直接访问（原因：名字重整）
#__xx__:魔术方法
class Person(object):
    def __init__(self):
        self.__num = 100
    def getNum(self):
        return  self.__num
    def setNum(self,num):
        self.__num = num

p = Person()
# print(p.__num) #直接访问报错
#p.__num = 200
#print(p.__num) #先设置再访问
#通过get、set方法获取跟设置
print(p.getNum())
p.setNum(300)
print(p.getNum())

print(p._Person__num) #可以访问
