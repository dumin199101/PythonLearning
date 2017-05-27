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
#set：一组key的无序集合，输入参数为一个list:重复的项会被过滤
s = set(['Hello','World','Python','Hello','World'])
print s
#添加元素到set
s.add('Java')
print s
#删除元素
s.remove('Python')
print s
#利用set取交集并集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print "交集：",s1&s2
print "并集：",s1|s2



