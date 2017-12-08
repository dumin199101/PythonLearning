#coding=utf-8
#set集合：使用a = {11,22,33}表示，无重复元素
a = {11,22,33}
print(type(a))

b = [11,22,33,22,11,33,44,22]
print(set(b))

# <class 'set'>
# {33, 11, 44, 22}

#交叉并：
c = {11,22,33}
d = {11,34,66,22}
print(c.intersection(d))
print(c.union(d))
print(c.difference(d))