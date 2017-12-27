#coding=utf-8
#单进程非阻塞（思想类似：轮询，数量多的话不过会有延时）
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
addr = ('',7777)
serverSocket.bind(addr)
#设置为非阻塞
serverSocket.setblocking(False)
serverSocket.listen(100)
clientAddrList = []
while True:
    #服务器监听客户端连接
    try:
        clientSocket,destAddr = serverSocket.accept() #服务器未收到连接会报异常
    except:
        pass
    else:
        print("创建一个新的客户端：%s"%str(destAddr))
        clientSocket.setblocking(False)
        clientAddrList.append((clientSocket,destAddr))

     #接收数据
    for clientSocket,destAddr in clientAddrList:
        try:
            content = clientSocket.recv(1024) #服务器未收到数据会报异常
        except:
           pass
        else:
            if len(content) > 0:
                print("receive data from %s:[%s]" % (destAddr, content))
            else:
                clientSocket.close()
                clientAddrList.remove((clientSocket,destAddr))
                print("%s 已经下线" % str(destAddr))
