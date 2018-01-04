#coding=utf-8
import time
#获取时间戳
print(time.time())
#获取时间元组
print(time.localtime())
print(time.localtime(time.time()-10000000))
#获取fmt格式当前时间
print(time.ctime())
#格式化日期
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))