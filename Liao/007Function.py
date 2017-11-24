#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#函数
def power(n,m):
    s = 1
    while m>0:
        m = m - 1
        s = s * n
    return s
num = power(5,3)
print(num)

#默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

num = power(5)
print(num)

#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end(L=[]):
    L.append('END')
    return L
res = add_end([1,2,3]) #正常调用
print(res)

res = add_end()
print(res)
res = add_end() #此处记住了上次调用的结果
print(res)

#改进：使用不可变对象None
def add_end(L=None):
    if L is None:
        L = []
    L.append('End')
    return L
res = add_end()
print(res)
res = add_end()
print(res)

#可变参数
def calc(*nums):
    sum = 0
    for num in nums:
        sum = sum + num * num
    return sum

res = calc(1,2)
print(res)
res = calc(3,4,5)
print(res)

#关键字参数
def info(name,age,**other):
    print("name:",name,"age:",age,"other:",other)
info('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
