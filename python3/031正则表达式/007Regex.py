# coding=utf-8
# 贪婪跟非贪婪:默认贪婪模式（尽可能多的匹配），通常存在包含匹配关系。非贪婪模式（尽可能少匹配，加？即可）
import re
s = "<html><p><h1>Hello World</h1></p></html>"
a = re.sub(r"<.+?>"," ",s)
print(a)