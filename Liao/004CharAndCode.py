#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#字符串和编码
#讨论：字符串的编码问题
#计算机最早使用8个比特作为一个字节，一个字节所能表示的最大整数是255（二进制转化为十进制），2个字节所能表示的最大整数是
#65535,所以出现了最早的编码表ASCII码表，只有127个字符。为了处理多语言编码的乱码问题，出现了Unicode码表。Unicode通常用
#两个字节表示一个字符，但是出现了一个新问题：存储空间的浪费。本着节约的精神，出现了UTF-8编码表，UTF-8编码把一个Unicode字符
# 根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节。用UTF-8编码就能节省空间。
#在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

#在Python3中字符串是以Unicode进行编码的
print('包含中文的str')
print(ord('A'))
print(chr(65))
print('\u4e2d\u6587') #根据字符整数编码转换为十六进制的unicode码

#字符串在内存中的Unicode表示，如果存储到磁盘上就会转换为以字节为单位的bytes，以Unicode表示的str会通过encode方法表示为
#指定编码的bytes
print('ABC') #一个字符多个字节
print(b'ABC') #一个字符一个字节
print('ABC'.encode('utf-8')) #b'ABC'
print(b'ABC'.decode('utf-8')) #ABC

#len函数计算字符串的字符数跟字节的字节数
print(len('ABC'))
print(len('中文'.encode('utf-8')))

#格式化
print('Hello, %s' % 'world')
print('欢迎你, %s，再见%s'%('小拜年','小松鼠'))



