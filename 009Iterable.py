#coding=utf-8
from collections import Iterable
#字典迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print key,d[key]
for k,v in d.iteritems():
    print k,v
for v in d.itervalues():
    print v
#判断是否可迭代
print isinstance('ABC',Iterable)
#下标循环list
for i,val in enumerate(['A','B','C']):
    print i,val
#多重循环
for x,y in [(1,2),(2,3),(3,4)]:
    print x,y

