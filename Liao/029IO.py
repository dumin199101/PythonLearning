#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#目录
import os
print("操作系统类型：",os.name) #nt:windows posix:Unix
print("环境变量：",os.environ)
path = os.environ.get('PATH')
print(path)

#操作文件跟目录：一部分在os模块，一部分在os.path模块
print(os.path.abspath('.')) #当前目录的绝对路径
path = os.path.join('testdir') #注意seq.join()跟os.path.join(path1,path2)，避免不同操作系统下分隔符问题，os.path.split()拆分路径
#os.mkdir(path) #创建目录
# os.rmdir(path) #删除目录
#获得文件扩展名
name = os.path.splitext("1.txt")
print(name)
#文件重命名：
# os.rename('io2.txt','io_2.txt')
#删除文件：
# os.remove('io_2.txt')
#复制文件使用shutil模块
#列出当前文件夹所有python文件：
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(files)