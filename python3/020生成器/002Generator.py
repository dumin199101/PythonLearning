#coding=utf-8
#在函数内部使用yield做生成器
#yield的作用：1.终止函数运行，将值返回
#如果是生成器，那么再调用函数，函数不会执行而是返回一个生成器对象。
#斐波那契数列
def createNum(m):
    print("start")
    n = 0
    a,b = 0,1
    while n<m:
        # print(b)
        print("----------1-------")
        yield b
        print("----------2-------")
        a,b = b,a+b
        n = n+1
        print("----------3-------")
    print("end")

a = createNum(5)
print(a)
next(a)
# start
# ----------1-------
next(a)
# ----------2-------
# ----------3-------
# ----------1-------