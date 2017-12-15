#coding=utf-8
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.bind(("192.168.1.101",7777))
data = s.recvfrom(1024)
#(b'Hello upd,i am coming', ('192.168.1.101', 60665))
content,addr = data
print(content.decode("utf-8"))
