#_*_coding=utf-8_*_
#自定义异常：触发异常捕获异常
class ShortInputException(Exception):
    def __init__(self,length,standard):
        self.length = length
        self.standard = standard

def test():
    try:
        str = input("请输入一个长度大于3的字符串")
        if len(str)<3:
            raise ShortInputException(len(str),3) #触发这个异常 创建异常对象
    except ShortInputException as e: #得到异常对象
        #捕获这个异常
        print("ShortInputException:输入的长度是%d,长度最少应该是：%d"%(e.length,e.standard))
    finally:
        print("Over...")
test()