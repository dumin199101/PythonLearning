#coding=utf-8
#多进程服务器
#Process放在__main__中执行，否则不执行
from socket import *
from multiprocessing import Process

def dealClientData(newSocket,destAddr):
        while True:
            content = newSocket.recv(1024)
            if len(content)>0:
                print("receive data from %s:[%s]"%(str(destAddr),content.decode("gb2312")))
            else:
                print("子进程关闭:[%s]" %destAddr)
                break
        newSocket.close()




def main():
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    addr = ('',8787)
    serverSocket.bind(addr)
    serverSocket.listen(100)
    try:
        while True:
            #服务器监听客户端连接
            newSocket,destAddr = serverSocket.accept() #阻塞
            print("主进程，开启子进程接下来负责处理：%s"%str(destAddr))
            #多进程处理
            p = Process(target=dealClientData,args=(newSocket,destAddr))
            p.start()
    finally:
        serverSocket.close()

if __name__ == '__main__':
    main()

# def test():
#     print("hello")
#
# if __name__=="__main__":
#     for i in range(4):
#         p = Process(target=test)
#         p.start()