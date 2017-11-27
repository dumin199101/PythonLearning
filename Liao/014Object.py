#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#继承跟多态
class Animal(object):
    def run(self):
        print("Animal is runnning")

class Dog(Animal):
    pass

class Cat(Animal):
    pass

Dog().run()
Cat().run()

#重写run
class Dog(Animal):
    def run(self):
        print("Dog is running")

class Cat(Animal):
    def run(self):
        print("Cat is running")

Dog().run()
Cat().run()

#多态：狗既是狗类，也属于动物类
#开闭原则：
# 对扩展开放：允许新增Animal子类；
#对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
