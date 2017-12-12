#coding=utf-8
#使用for in遍历打印生成器的内容：有多少个打印多少个
def createNum(m):
    n = 0
    a,b = 0,1
    while n<m:
        yield b
        a,b = b,a+b
        n = n+1

a = createNum(5)
for num in a:
    print(num)
