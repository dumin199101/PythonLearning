# coding=utf-8
#在字符串中查找，但是不是从开头匹配
import re
result = re.search("(\d{3})(\w{2})(\d{4})","cc123aa1234")
if result is not None:
    print(result.group())
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    print(result.groups())
else:
    print(result)