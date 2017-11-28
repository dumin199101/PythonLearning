#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#内存流：StringIO BytesIO
from io import StringIO
from io import BytesIO
#写数据
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

#读数据
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s=='':
        break
    print(s.strip())

#StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
f = BytesIO()
f.write('中国'.encode('utf-8'))
print(f.getvalue().decode('utf-8'))

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
str = f.read()
print(str.decode('utf-8'))


