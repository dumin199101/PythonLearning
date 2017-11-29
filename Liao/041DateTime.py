#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#常见内建模块之时间日期
from datetime import datetime,timedelta
#获取当前时间
now = datetime.now()
print(now)
#获取指定时间
dt = datetime(2016,12,2,12,23,11)
print(dt)
#datetime转换为时间戳：
ts = dt.timestamp()
print(ts)
#timestamp转换为datetime
ts = 1480652591.0
dt = datetime.fromtimestamp(ts)
print(dt)
#str解析为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print(cday)
#datetime格式化为str
now = datetime.now()
print(now.strftime('%Y-%m-%d %H:%M:%S'))
#datetime加减
now = datetime.now()
tomorrow =  now + timedelta(days=1)
print(tomorrow)

