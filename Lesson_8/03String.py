#coding=utf-8
'day03 Python字符串处理函数'
__author__ = 'lieyan123091'
#字符串声明
str = 'Hello \'world\''
print type(str),str #<type 'str'>
str1 = 'Hello'
print type(str1),str1 #<type 'str'>
str2 = '''
Hello
'''
print type(str2),str2
str3 = """ haha
Hello 'Good' "World"
GOOD STUDY
"""
print type(str3),str3


#访问元素
print str1[0],str1[-1]
#分片操作
print str1[1:3]

#字符串修改只是修改了指针指向,字符串本身并没有发生变化
print id(str1)
str1 = 'Gog'
print id(str1)

#操作符：
print str + " Python"
print "#"*100 #字符串重复多次
print 'h' in str1
print 'a' not in str1
print r'\rGood\n' #原始输出，不转义

#字符串格式化输出
print "Hello World %s,I love %s" % ('Python','World')

print "#"*100

str = "hello world java python php java"
#字符串查找：返回子串第一次查找到的位置，找不到返回-1
print str.find('java')
print str.find('f')
print str.find('java',30)  #指定从某个位置开始查找
#字符串长度
print len(str)
#返回子串第一次查找到的位置，找不到抛出异常
print str.index('java')
#统计子串出现次数
print str.count('java')
#解码(二进制---unicode)，编码（unicode---二进制）
print 'HelloWorld'.decode('gbk')
print u'HelloWorld'.encode('gbk')
print '中国'.decode('utf-8')
print u'中国'.encode('utf-8')
#字符串替换
print str.replace('java','python',1)
#字符串分割
print str.split(' ')
mylist = str.split(' ')
for s in mylist:
    print s
#首字母大写
print str.capitalize()
#居中显示,以空格填充
print str.center(100,'$')
#判断以子串结尾
print str.endswith('java')
print str.startswith('Hello')
#去除字符串两边的空格
print str.strip()
#判断是否是字母或数字
str1 = 'ABC123'
str2 = '123'
str3 = 'abc'
print str.isalnum()
print str1.isalnum()
print str.isalpha()
print str2.isdigit()
#判断是否是大小写
print str3.islower()
print str1.lower()
print str1.isupper()
print str1.upper()













