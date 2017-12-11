#coding=utf-8
#闭包：如果一个函数内部定义了一个函数，并且用到了外部函数的变量，那么这个内部函数可以称之为闭包！
#在未调用内部函数之前，外部函数的变量不会释放！！！
def test(num):
    print("-----1------")
    def test1(num2):
        print("----2------")
        print(num+num2)
    print("------3-----")
    return test1

a = test(100)
a(200)