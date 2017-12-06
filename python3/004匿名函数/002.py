#_*_coding=utf-8_*_
#匿名函数：匿名函数做实参，使用eval函数做转换
def test(a,b,func):
    result = func(a,b)
    return result

input = input("请输入一个匿名函数：")
func = eval(input)
result = test(11,22,func)
print(result)