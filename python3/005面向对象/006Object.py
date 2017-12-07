#_*_coding:utf-8_*_
#init方法初始化 new方法创建对象 这两个方法共同构成了构造方法
class Dog(object):
    def __init__(self):
        print("init")
    def __del__(self):
        print("del")
    def __new__(cls):
        print("new")
        return super().__new__(cls)
    def __str__(self):
        return "str"

dog = Dog()

