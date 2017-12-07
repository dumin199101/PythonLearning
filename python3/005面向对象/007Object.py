#_*_coding=utf-8
#单例模式：并且只初始化一次
class Dog(object):
    __instance = None
    __init_flag = False
    def __new__(cls,name):
        if cls.__instance==None:
            cls.__instance = super().__new__(cls)
        return cls.__instance
    def __init__(self,name):
        if Dog.__init_flag == False:
          self.name = name
          Dog.__init_flag=True
dog1 = Dog("aa")
print(id(dog1))
print(dog1.name)
dog2 = Dog("bb")
print(id(dog2))
print(dog2.name)
