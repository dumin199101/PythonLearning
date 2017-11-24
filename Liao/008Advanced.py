#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
from collections import Iterable
#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#截取列表中的前三个元素(包左不包右：起始索引，结束索引)
print(L[0:3])
print(L[:3]) #起始索引为0可以省略
print(L[-2:]) #倒数切片
L1 = list(range(100))
print(L1[0:20:5]) #每五个取一个

#迭代
d = {'a': 1, 'b': 2, 'c': 3}
for k in d:
    print(k)

for v in d.values():
    print(v)

for k,v in d.items():
    print(k,v)

#判断是否是可迭代对象
print(isinstance('abc',Iterable))

#索引下标+元素
for i,v in enumerate(L):
    print(i,v)

#列表生成式
L2 = [x*x for x in range(0,20)]
print(L2)
L3 = [x*x for x in range(0,10) if x%2==0] #同时做筛选
print(L3)


