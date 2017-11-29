#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#常见内建模块之集合
from collections import namedtuple,deque,defaultdict,OrderedDict,Counter
#拥有tuple的特性，也可以通过属性来调用
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)
print(p.y)
#list查询快，解决list插入删除慢的缺点:
q = deque(['a', 'b', 'c'])
q.append('d')
q.append('e')
print(q)
q.appendleft('f')
q.appendleft('g')
print(q)
q.pop()
print(q)
#defaultdict：引用key不存在时返回默认值
dd = defaultdict(lambda :'N/A')
dd['key'] = 'hello'
print(dd['key'])
print(dd['val'])
#OrderedDict:dict按照插入顺序排序
d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))
#Counter计数
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(dict(c))