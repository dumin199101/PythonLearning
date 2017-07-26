#coding=utf-8
import time
name = raw_input(u"请输入姓名")
age = raw_input(u"请输入年龄")
qq = raw_input(u"请输入QQ")
print u"系统正在打印中..."
time.sleep(3)
print(u"您的姓名：%s,年龄：%d,QQ:%s"%(name,int(age),qq))
