#coding=utf-8
#list
classmates = ['Michael', 'Bob', 'Tracy']
print classmates
#获得list个数
print len(classmates)
#访问
print classmates[0]
#append追加
classmates.append('Adam')
print classmates
#追加到指定位置
classmates.insert(1,'Jack')
print classmates
#删除末尾元素
print classmates.pop()
print classmates
#删除指定位置的元素
classmates.pop(1)
print classmates
#替换指定元素
classmates[1] = 'Sarah'
print classmates
#拼接list
T = classmates + ['KK','MM']
print T #['Michael', 'Sarah', 'Tracy', 'KK', 'MM']
classmates.append(['JJ','GG'])
print classmates #['Michael', 'Sarah', 'Tracy', ['JJ', 'GG']]

#tuple:元素不可修改，长度不可修改，可以看成是一个list的子集
t = (1,2)
print t
#只定义一个元素
tt = (1,)
print tt
#访问元组
print t[0]


