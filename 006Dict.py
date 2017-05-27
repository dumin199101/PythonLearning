#coding=utf-8
#dict：字典
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
#获取
print d['Michael']
#修改
d['Bob'] = 67
print d
#判断键是否存在
if d.get('Adam'):
    print d['Adam']
else:
    print d.get('Adam',-1)
#删除
d.pop('Bob')
print d
#set：一组key的集合，输入参数为一个list
