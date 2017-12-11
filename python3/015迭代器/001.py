#coding=utf-8
#可迭代对象：Iterable:可以使用for循环遍历
#1.list,tuple,dict,str,set
#2.generator:生成器跟带yield的generator function
from collections import Iterable
print(isinstance([11,22],Iterable))
print(isinstance({'a':"a",'b':'b'},Iterable))
print(isinstance((11,22),Iterable))
print(isinstance('abc',Iterable))
print(isinstance({11,22,33},Iterable))
print(isinstance((x for x in range(10)),Iterable))

