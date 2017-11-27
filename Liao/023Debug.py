#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#Python中的Debug

#1.print
# def foo(s):
#     n = int(s)
#     print('>>> n = %d' % n)
#     return 10 / n
#
# def main():
#     foo('0')

# main()

#2.assert使用断言，断言失败，抛出异常
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
#
# def main():
#     foo('0')
#
# if __name__ == '__main__':
#     main()

#3.使用logging方式：四种级别：debug,info,warning,error,设置层级越高，低级别就不显示
#你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息
import logging
logging.basicConfig(level=logging.DEBUG)
s = '0'
n = int(s)
logging.debug("Error!!!")
logging.info('n = %d' % n)
print(10 / n)