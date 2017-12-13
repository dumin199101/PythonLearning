#coding=utf-8
#内建函数：range(start,stop,step):生成器 map(func,iterable) reduce(func,iterable,initial) sorted(iteable)
from functools import reduce
a = range(10,20)
for i in a:
    print(i)

b = map(lambda x:x*x,a)
for i in b:
    print(i)

c = reduce(lambda x,y:x+y,[1,2,3,4],10)
print(c)

d = sorted(['a','b','e','c','f','d'],reverse=True)
print(d)
