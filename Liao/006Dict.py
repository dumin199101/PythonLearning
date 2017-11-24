#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#查
print(d['Bob'])
#增
d['Adam'] = 88
print(d)
#key不允许重复，如果有重复的key，后边的覆盖前边的
d['Bob'] = 100
print(d)
#判断指定的key是否存在:存在返回指定的value，不存在返回None或者指定的默认值
print(d.get('Tracys',-1))
#删除
d.pop('Bob')
print(d)