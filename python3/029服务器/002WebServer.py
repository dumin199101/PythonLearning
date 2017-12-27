#coding=utf-8
#多线程服务器
from socket import *
import threading
def dealClientData(newSocket,destAddr):
        while True:
            content = newSocket.recv(1024)
            if len(content)>0:
                print("receive data from %s:[%s]"%(str(destAddr),content.decode("gb2312")))
            else:
                print("子线程关闭:[%s]" %destAddr)
                break
        # newSocket.close()


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
addr = ('',6666)
serverSocket.bind(addr)
serverSocket.listen(5)
try:
    while True:
        #服务器监听客户端连接
        newSocket,destAddr = serverSocket.accept() #阻塞
        print("主进程，开启子线程接下来负责处理：%s"%str(destAddr))
        #多线程处理
        p = threading.Thread(target=dealClientData,args=(newSocket,destAddr))
        p.start()
finally:
    serverSocket.close()
