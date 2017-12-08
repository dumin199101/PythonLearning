#coding=utf-8
#python中的包管理：
#如果一个文件夹中存在__init__.py文件，那么这个文件就可以看成是Python的包
#import 包时会自动执行__init__.py文件，但是用不了里边的模块，如果想用里边的模块需要import导入模块:from . import 模块名
# __all__ = []：在__init__.py文件中声明__all__变量会在from 包 import 模块时规定可以导入的模块
__all__ = ['recvMsg','sendMsg']
#from . import recvMsg,sendMsg
from . import *
