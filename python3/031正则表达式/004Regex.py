# coding=utf-8
# \num 代表匹配的值
import re
s = "<html><h1>Hello World</h1></html>"
print(re.match(r"<(.*)><(.*)>.*</\2></\1>",s).group())
print(re.match(r"<(.*)><(.*)>.*</\2></\1>",s).groups())

# <html><h1>Hello World</h1></html>
# ('html', 'h1')