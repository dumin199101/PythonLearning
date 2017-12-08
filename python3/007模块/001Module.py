#_*_coding=utf-8_*_
#模块：模块的本质就是python文件
#默认先从当前目录下找，如果找不到再从系统目录下找
#__name__属性如果是自己调用__name__==__main__,如果是其它模块中调用，__name__==文件名
#调用方式1：
import sendMsg
sendMsg.sendMsg()
sendMsg.getMsg()
#调用方式2
from sendMsg import getMsg
getMsg()
print(__name__)
def test():
    print("自己模块调用")
if __name__=="__main__":
    test()

