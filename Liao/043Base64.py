#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#base64编码解码：
import base64
#由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'abcd'))
print(base64.urlsafe_b64encode(b'http://www.micu.com/dfs/fdsf.html'))
print(base64.b64decode(b'YWJjZA=='))
print(base64.urlsafe_b64decode(b'aHR0cDovL3d3dy5taWN1LmNvbS9kZnMvZmRzZi5odG1s'))