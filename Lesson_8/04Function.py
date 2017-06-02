#coding=utf-8
'day04 字符串处理函数跟函数的参数'
__author__ = 'lieyan123091'
#判断是否是空格
space = '        '
print space.isspace()
#mystr.join(str) str每个字符后边都连接mystr
print "Hello".join("XXXX") # XHelloXHelloXHelloX
str = "Hello World Java Python World Good"
#字符串左对齐，剩余宽度用指定字符填充
print str.ljust(100,"$")
#去除字符串空格
str1 = " CCCCC Good "
print str1.lstrip()
print str1.rstrip()
print str1.strip()
#字符串从右边查找
print str.rfind("Java")
#字符串分割
print str.partition('World') #('Hello ', 'World', ' Java Python World Good')
print str.rpartition("World") #('Hello World Java Python ', 'World', ' Good')

#函数
#定义
def fun1():
    "函数的注释"
    print "这是一个函数"
    return
#调用
fun1()
print "#"*100
#函数传参：值 引用
def changeme(mylist=[]):
    '引用传递'
    mylist.append([1,2,3,4])
    print "函数内部的mylist:",mylist
    return
mylist = [2,2,3,4]
changeme(mylist)
print "函数外部的mylist",mylist
def changeval(val):
    '值传递'
    val = 100
    print "函数内部的val:",val
    return
val = 50
changeval(val)
print "函数外部的val",val

#可变参数 关键字参数 默认参数

#lambda匿名函数
sum = lambda x,y:x+y
print sum(1,2)






