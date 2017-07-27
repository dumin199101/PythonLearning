#coding=utf-8
'''
字符串
'''
#下标
str = 'lieyan123091lovepython'
print str[0]
print str[1]
#切片
print str[1:8:2] #起始位置，结束位置，步长,包←不包→
print str[5:] #截取到最后
print str[-1:-3:-1] #步长为负数
print str[::-1] #反过来