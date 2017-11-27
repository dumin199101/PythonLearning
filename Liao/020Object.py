#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#内置方法
#1.__str__&__repr__
class Student(object):
    def __init__(self,name):
        self.name =  name
    def __str__(self):
        return 'Student object (name: %s)' % self.name #这个地方使用return返回
    __repr__ = __str__ #__repr__是给开发者看的,__str__是给用户看的，两者内容一致
    def __getattr__(self, item):
        if item=='score':
            return "score is default!"
    def __call__(self, *args, **kwargs):
        print("__call__ is Execute")
print(Student("Michale")) #打印对象时自动调用

#__iter__:返回迭代对象，Python的for循环会不断调用该对象的__next__方法，直到遇到StopIteration错误推出循环
#__getitem__:类比List返回对应的项
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        if self.a>100:
            raise StopIteration()
        return self.a
    def __getitem__(self, item):
        a, b = 1, 1
        for x in range(item):
            a, b = b, a + b
        return a
for n in Fib():
    print(n)
print(Fib()[2])

#__getattr__:当调用一个不存在的类方法或属性：
s = Student("Lisi")
print(s.score)

#__call__:直接在实例本身调用，而非通过instance.method()来调用
s2 = Student("HH")
s2()

#通过callable()判断是否可调用
print(callable(s2))