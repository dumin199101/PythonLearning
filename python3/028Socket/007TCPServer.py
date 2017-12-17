#coding=utf-8
#TCP服务端：
from socket import *
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",7788))
serverSocket.listen(5)
clientSocket,clientInfo = serverSocket.accept()
data = clientSocket.recv(1024)
print("%s:%s"%(str(clientInfo),data.decode("utf-8")))
clientSocket.send(data)
clientSocket.close()
serverSocket.close()