# coding=utf-8
# match(pattern,str):检测是否开始匹配，如果匹配成功返回一个match对象，可以通过group方法获取匹配结果，匹配失败返回None
import re
result = re.match("hellop","hellophp")
if result is not None:
    print(result.group())
else:
    print(result)