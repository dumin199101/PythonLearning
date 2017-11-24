#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
from functools import reduce
#map：注重过程:将L1中的每一个元素应用于f1,map函数的返回值是一个map对象
L1 = [1,2,3,4,5]
def f1(x):
    return x*x
print(list(map(f1,L1)))

#reduce：注重结果：将上一次结果跟下一个元素应用f1函数做运算
def f2(x,y):
    return x+y
print(reduce(f2,L1))

#filter：过滤
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd,[1,2,3,4,5,6])))

#sorted:排序
L2 = [21,34,11,23,-2,43,-21]
print(sorted(L2,key=abs,reverse=True))

#lambda表达式:其实就是匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5])))