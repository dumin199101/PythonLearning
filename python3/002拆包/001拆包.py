#_*_coding:utf-8_*_
#拆包
def test(a,b,c=33,*args,**kw):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kw)

test(11,22,33,44,55,66,77,task=88,done=99)
print("-"*10)
A = (44,55,66)
B = {"name":"xiaoming","age":22}
test(11,22,33,*A,**B)