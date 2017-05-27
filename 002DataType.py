#coding=utf-8
#整型
a = 10;
#浮点型
b = 1.5
c = 1.23e9;
#字符串
#转义字符串
d = "I\'m \"OK\"!"
#不转义特殊字符
e = r'\t\t\t123'
print a,b,c,d,e

#换行打印
print '''Hello
World
Python
'''
#布尔值（注意大小写）True False
print True,False
#对布尔值进行and,or,not运算
print True and True
print True and False
print False and False
print True or True
print True or False
print False or False
print not True
print not False

#空值 None不等同于0
print None

#变量：变量本身类型不固定的语言称之为动态语言
#解析下边这个例子：Python解释器：1.在内存创建一个字符串'ABC',在内存中创建一个变量a指向'ABC',最终运行结果为ABC
aa = 'ABC'
bb = aa
aa = 'DEF'
print bb

#运算
print 10/3 #3
print 10.0/3 #3.33333333
print 10%3 #1
print 10//3 #3 地板除

#常量:使用大写
NAME = '嘟嘟'
print NAME
