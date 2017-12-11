#coding=utf-8
#迭代器：可以使用next()获取下一个值的对象成为迭代器：Iterator
from collections import Iterator
print(isinstance([11,22,33],Iterator)) #false
print(isinstance(iter([11,22,33]),Iterator)) #使用iter进行转换
a = iter([11,22,33])
print(next(a))
print(next(a))
print(next(a))