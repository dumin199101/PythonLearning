#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#正则表达式
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None
import re
print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
test = '010-12345'
if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('ok')
else:
    print('failed')
#切分字符串
print( 'a b   c'.split(' '))
print(re.split(r'\s+', 'a b   c'))
#利用正则分组：
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(m.group(0)) #原始串
print(m.group(1))
print(m.group(2))

#贪婪匹配：正则默认贪婪匹配，尽可能多的匹配字符
res = re.match(r'^(\d+)(0*)$', '102300').groups()
print(res) #由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。
#非贪婪匹配：加个?就可以让\d+采用非贪婪匹配(尽可能少的匹配)：
res = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(res)

#正则编译
#1.编译
regex = re.compile(r'^(\d{3})-(\d{3,8})$')
#2.使用
res = regex.match('010-12345').groups()
print(res[0],res[1])