#coding=utf-8
#__slots__属性：规定对象所具备的属性列表。
class Person(object):
    __slots__ = ("name","age")
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("du",22)
# p.addr = "beijing"
# print(p.addr)   #报错
