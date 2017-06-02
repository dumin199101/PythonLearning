#coding=utf-8
import os
#列表生成式
print [x*x for x in range(1,10)]
print [x*x for x in range(1,10) if x%2==0] #加if条件
print [x+y for x in 'ABC' for y in 'DEF'] #双层循环
print [file for file in os.listdir('.')] #列出当前目录下的文件



