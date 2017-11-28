#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#读文件
try:
    f = open('io.txt','r')
    str = f.read()
    print(str)
finally:
    if f:
        f.close()
#方式2：
    with open('io3.txt','r',encoding='utf-8') as f:
        str = f.read()
        print(str)

#其它方法：read(size) readline() readlines()

#字符编码：
    with open('io3.txt', 'r',encoding='utf-8') as f:
        str = f.read()
        print(str)

#二进制文件例如图片、音频采用rb方式
