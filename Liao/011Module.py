#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#模块：
#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'
#使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'dumin'
import sys
def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
#Python解释器把一个特殊变量__name__置为__main__，而如果在其他地方导入该hello模块时，if判断将失败
if __name__=='__main__':
    test()

#使用第三方模块：pip
#安装：pip install Pillow:基于PIL的Python图像处理库

#我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，
# 它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

