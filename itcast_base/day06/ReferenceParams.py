#coding=utf-8
def test(a,b=100):
    print a+b

test(10)

def test2(a,*b,**c):
    print a
    print b #(200,300)
    print c["name"]
    print c["age"]

test2(100,200,300,name="dudu",age=22)

