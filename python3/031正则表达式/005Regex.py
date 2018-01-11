# coding=utf-8
# （）过多用起名字的方式：定义：?P<key1> 使用：?P=key1
import re
s = "<html><h1>Hello World</h1></html>"
print(re.match(r"<(?P<key1>.*)><(?P<key2>.*)>.*</(?P=key2)></(?P=key1)>",s).group())