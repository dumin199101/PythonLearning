#_*_coding:utf-8_*_
#异常处理：
#防止因为异常导致程序终止执行
try:
    # print("----------------")
    # 10 / 0
    open("1.txt","r")
except NameError:
    print("变量未声明")
except FileNotFoundError:
    print("文件不存在")
except ZeroDivisionError as e:
    print(e)
except (AttributeError,ValueError):
    print("属性参数错误")
except Exception:
    print("其余类型的错误")
else:
    print("未发现错误")
finally:
    print("Over....")