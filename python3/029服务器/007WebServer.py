#coding=utf-8
#epoll版服务器：事件通知机制，无套接字上限。
# EPOLLIN（可读） EPOLLOUT（可写） EPOLLET（边缘触发，只通知一次） EPOLLLT(水平触发，通知多次直到触发为止)
from socket import *
import select

#创建套接字
s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#绑定
s.bind(('',7788))
#变为被动
s.listen(10)
#创建一个epoll对象
epoll = select.epoll()
#将创建的套接字加入到epoll事件监听
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

connections = address = {}

#循环等待客户端发过来的数据：
while True:
   epoll_list = epoll.poll()

   for fd,event in epoll_list:
         #如果是socket创建的套接字被激活
         if fd==s.fileno():
             cli,addr = s.accept()
             print("有新的客户端到来%s"%str(addr))

             connections[cli.fileno()] = cli
             address[cli.fileno()] = addr
             epoll.register(cli.fileno(),select.EPOLLIN|select.EPOLLET)

         elif event==select.EPOLLIN:
             #从激活fd上接收：
             data = connections[fd].recv(1024)
             if len(data)>0:
                 print("recv:%s"%data)
             else:
                 epoll.unregister(fd)
                 connections[fd].close()
                 print("offline----%s"%(str(address[fd])))

