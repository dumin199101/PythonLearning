#coding=utf-8
#函数
#绝对值函数
print abs(100)
print abs(-100)
print abs(12.89)
#比较函数：如果x<y，返回-1，如果x==y，返回0，如果x>y，返回1
print cmp(1,3)
print cmp(1,1)
print cmp(1,-1)
#数据类型转换
print int('123')
print int(12.34)
print float('12.34')
print str(123)
# print unicode(u'中国')
print bool(1)
print bool(0)
#自定义函数：如果函数没有返回值，会有一个默认的返回值None，return None可以简写为return
def my_abs(x):
    if x>0:
        print x
    else:
        print -x
res = my_abs(-10)
print res #返回值为None
#空函数
def no():
    pass
res1 = no()
print res1
#返回值有多个
def my_return(a,b):
    a = a+1
    b = b+1
    return a,b
a,b = my_return(1,2)
print a,b
res2 = my_return(1,2) #返回值实质是一个tuple
print res2,type(res2)
#默认参数
def func1(name,age=12):
    print '姓名：',name,"，年龄：",age
func1('杜')
func1('dudu',22)
#调用时参数顺序不一致
def func2(name,age=12,sex='male'):
    print '姓名：',name,"，年龄：",age,"，性别：",sex
func2('wang',sex='female',age=23)
#可变参数:list或者tuple
def func3(*args):
    sum = 0
    for num in args:
        sum = sum+num*num
    return sum
res4 = func3(1,2,3)
#直接传入一个list
list1 = [1,2,3]
res5 = func3(*list1)
print res4,res5
#关键字参数：dist
def func4(name,age,**kw):
    print '姓名：', name, "，年龄：", age, "，其它信息：", kw
dist1 = {'addr':'beijing','tel':'119'}
func4('du',25,**dist1)




