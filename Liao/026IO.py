#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#写文件
#方式1
f = open('io.txt','w')
f.write('Hello World!')
f.close()

#方式2：
try:
    f = open('io2.txt', 'w')
    f.write('Hello World!!!')
finally:
    if f:
        f.close()

#推荐方式：
with open('io3.txt','w') as f:
    f.write('Hello Python')