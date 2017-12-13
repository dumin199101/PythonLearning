#coding=utf-8
#内建属性：__new__,__init__,__del__,__str__,__repr__,
# __getattribute__:属性拦截器
# __doc__:获取文档信息
# __dict__：获取属性列表
# __bases__：获取当前类的父类，通过类名调用
# __class__：获取当前实例的类
class Animal(object):
    '''
       父类：动物类
    '''
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def eat(self):
        print("eat!!!")


class Person(Animal):
    '''
      人类
    '''
    def __init__(self,name,age,job):
        super(Person,self).__init__(name,age) #重写父类：super(当前类名,self)
        self.job = job
    addr = "beijing"
    def sleep(self):
        print("sleep!!!")
    def __getattribute__(self, item):
        if item=="name":
            print("Log...")
            return "huahua is here"
        else:
            return object.__getattribute__(self,item)


p = Person("huahua",22,"lawer")
print(p.__class__)
print(Person.__bases__)
print(p.__dict__)
print(p.__doc__)
print(p.name)
print(p.addr)

