#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
#md5跟sha1算法：
import hashlib
md5 = hashlib.md5()
md5.update("How to get score".encode('utf-8'))
print(md5.hexdigest())
sha1 = hashlib.sha1()
sha1.update("How to get score".encode('utf-8'))
print(sha1.hexdigest())