#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#迭代器：
#1.count(start,step)无限迭代：
import itertools
# natures = itertools.count(1000000,2)
# for n in natures:
#     print(n)
#cycle():不断迭代某个值
# natures = itertools.cycle('ABC')
# for i in natures:
#     print(i)
#repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数
ns = itertools.repeat('A',10)
for s in ns:
    print(s)
#takewhile()创建一个有限序列：
natures = itertools.count(1)
ns = itertools.takewhile(lambda x:x<=10,natures)
for s in ns:
    print(s)
#chain()可以把一组迭代对象串联起来，形成一个更大的迭代器：
for s in itertools.chain('ABC','DEF'):
    print(s)
#groupby()把迭代器中相邻的重复元素挑出来放在一起：
# 实际上挑选规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被认为是在一组的，而函数返回值作为组的key。
for key,group in itertools.groupby('AAabbBBCCABC',lambda s:s.upper()):
    print(key,list(group))