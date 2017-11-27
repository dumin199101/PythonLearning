#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#枚举类1：
from enum import Enum,unique
Month = Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print(Month.Apr.value)
print(Month.Apr.name)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value) #value属性则是自动赋给成员的int常量，默认从1开始计数。

#枚举类2：
@unique #保证没有重复值
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1.name)
print(day1.value)

for name,member in Weekday.__members__.items():
    print(name,"=>",member,member.value)