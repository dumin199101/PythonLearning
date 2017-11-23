#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
classmates = ['Michael', 'Bob', 'Tracy']
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.append('LY')
print(classmates)
classmates.insert(1,'DD')
print(classmates)
classmates.pop()
print(classmates)
classmates[1] = 'HH'
print(classmates)

classmates = ('Michael', 'Bob', 'Tracy',['HH','CC'])
print(classmates)
classmates[3][0] = 'BB'
print(classmates)
