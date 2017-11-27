#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#多继承:在设计类的继承关系时，通常，主线都是单一继承下来的，如果需要“混入”额外的功能，通过多重继承就可以实现，这种
#设计叫MixIn设计模式
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, RunnableMixIn):
    pass

d = Dog()
d.run()
