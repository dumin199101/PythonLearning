# coding=utf-8
# 正则表达式基本使用
import re
# 1.findall():返回值是一个列表
s = "hello1 world hello2 python hello3 php"
print(re.findall("hello\d",s))
# 2.sub（pattern,replace,string）：替换，第二个参数可以是一个函数
a = re.sub("hello","haha",s)
print(a)
#参数result代表匹配到的每一个，返回值是一个字符串
def replace(result):
    print(result.group())
    return str(int(result.group())+50)
b = re.sub("\d",replace,s)
print(b)
# 3.split(pattern,str):返回值是列表
print(re.split(r"\s",s))