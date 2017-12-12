#coding=utf-8
#Python作为动态语言代表：动态添加类属性跟方法
import types
class Person(object):
    def __init__(self,name):
        self.name = name

p = Person("dudu")
#动态添加属性
p.age = 22
print(p.age)
#动态添加实例方法
def run(self):
    print("-----run-----%s"%self.name)
p.run = types.MethodType(run,p)
p.run()

#动态添加类方法：
@classmethod
def eat(cls):
    print("---------eat---------")
Person.eat = eat
Person.eat()
#动态添加静态方法：
@staticmethod
def sleep():
    print("---------sleep---------")
Person.sleep = sleep
Person.sleep()