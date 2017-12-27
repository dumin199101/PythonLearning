#coding=utf-8
#单进程服务器
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
addr = ('',7788)
serverSocket.bind(addr)
serverSocket.listen(5)
while True:
    #服务器监听客户端连接
    newSocket,destAddr = serverSocket.accept() #阻塞
    print("主进程，接下来负责处理：%s"%str(destAddr))
    try:
        while True:
            content = newSocket.recv(1024)
            if len(content)>0:
                print("receive data from %s:[%s]"%(destAddr,content))
            else:
                break
    finally:
        newSocket.close()
serverSocket.close()

