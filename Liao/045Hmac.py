#!/usr/bin/env python3
# _*_ coding=utf-8 _*_
import hmac
message = b'Hello World!'
key = b'123abc'
h = hmac.new(key,message,digestmod='MD5')
print(h.hexdigest())