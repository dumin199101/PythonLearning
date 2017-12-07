#_*_coding:utf-8_*_
#子类不能继承父类的私有属性跟私有方法
class Animal(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def __str__(self):
        return "Infos:name:%s,age:%d"%(self.__name,self.__age)
    def __del__(self):
        print("对象被释放了...")
    __repr__ = __str__
    def __info(self):
        print("打印动物的信息")
    def bark(self):
        print("叫...")

class Dog(Animal):
    #重写父类方法：
    def bark(self):
        super().bark() #使用super调用父类方法
        print("狗叫...")

dog = Dog("xiaohua",2)
dog.bark()
# dog.__info()  #无法调用私有方法
# print(dog.__name) #无法调用私有属性

print(dog) #调用__str__方法



