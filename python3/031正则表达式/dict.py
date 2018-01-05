# coding=utf-8
# dir()跟__dict__,__getattr__:


class Person(object):
    # 类属性
    country = "China"

    # 实例属性
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # 属性不存在时调用：
    def __getattr__(self, item):
        self.item = 100
        return "所调用的属性:"+item+"不存在,自行设定："+str(self.item)


p = Person("du",22)
# print(dir(p)) #对象的属性跟方法列表
# print(p.__dict__) #获取对象的属性
# print(Person.__dict__) #获取类属性
print(p.tel)

