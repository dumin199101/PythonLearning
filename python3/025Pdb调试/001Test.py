#coding=utf-8
#pdb调试
#python -m pdb 1.py
# continue c ：继续执行程序
# step s ：进入函数内部
# next n ：向下执行一行
# breakpoint b ：断点列表
# list l : 查看当前行
# return r :执行到函数尾
# quit q : 退出
# print p :打印变量
# args a : 查看参数

#手动开启
# import pdb
# pdb.set_trace()


def add(x,y):
    sum = x + y
    return sum

print("start...")
a = 100
b = 200
# pdb.set_trace()
res = add(a,b)
print("result is %d"%res)
print("end...")