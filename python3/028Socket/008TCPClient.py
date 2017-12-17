#coding=utf-8
#TCP客户端
from socket import *
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.1.141",7788))
clientSocket.send("Hello World".encode("utf-8"))
data = clientSocket.recv(1024)
print("Server Return Info:%s"%data.decode("utf-8"))
clientSocket.close()