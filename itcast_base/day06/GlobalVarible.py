#coding=utf-8
#全局变量+局部变量 可变变量+不可变变量
num = 100
def test():
    num = 200 #全局变量(不可变变量)不能直接修改，这里相当于定义了一个变量
    print "全局变量num重新赋值：".decode("utf-8"),num #200

def test2():
    print "打印全局变量num:".decode("utf-8"),num #100

test()
test2()

lists = [11,22,33,44]
def test3():
    print "打印全局变量lists:".decode("utf-8"),lists #打印全局变量lists: [11, 22, 33, 44]
    lists.append(55)
    print "打印全局变量lists".decode("utf-8"),lists  #打印全局变量lists [11, 22, 33, 44, 55]

def test4():
    print "打印全局变量lists".decode("utf-8"),lists #打印全局变量lists [11, 22, 33, 44, 55]

test3()
test4()

#改变全局变量（不可变变量）加global关键字
num2 = 200

def test5():
    global num2
    print "打印全局变量num2：".decode("utf-8"),num2 #200
    num2 +=200
    print "全局变量num2重新赋值：".decode("utf-8"),num2 #400

def test6():
    print "打印全局变量num2:".decode("utf-8"),num2 #400

test5()
test6()


