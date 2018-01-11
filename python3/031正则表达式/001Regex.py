# coding=utf-8
# match(pattern,str):检测是否开始匹配，如果匹配成功返回一个match对象，可以通过group方法获取匹配结果，匹配失败返回None
import re
result = re.match("(\d{3})(\w{2})(\d{4})","123aa1234")
if result is not None:
    print(result.group())
    print(result.group(0))
    print(result.group(1))
    print(result.group(2))
    print(result.group(3))
    print(result.groups())
else:
    print(result)

# 123aa1234
# 123aa1234
# 123
# aa
# 1234
#('123', 'aa', '1234')