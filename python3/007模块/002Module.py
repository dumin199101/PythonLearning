#_*_coding=utf-8_*_
#使用from 模块名 import * 方式导入时可以应用__all__=['getMsg']来规定可以导入的方法列表
from sendMsg import *
sendMsg()
getMsg()

# from sendMsg import getMsg
# getMsg()