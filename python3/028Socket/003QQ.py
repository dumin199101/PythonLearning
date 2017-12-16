#coding=utf-8
#多线程实现QQ聊天
#注意解码问题，循环
from threading import Thread
from socket import *
#发送数据
def send_data():
    while True:
        inputInfo = input("<<请输入要发送的信息:")
        s.sendto(inputInfo.encode("gb2312"),(inputAddr,int(inputPort)))

#接收数据
def recv_data():
    while True:
        info,addr = s.recvfrom(1024)
        print("\r>>%s:%s"%(addr,info.decode("gb2312")),end="")

s = None
inputPort = 0
inputAddr = inputInfo = ''

def main():
    global s,inputPort,inputAddr,inputInfo
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind(('',7788))
    inputAddr = input("请输入IP地址:")
    inputPort = input("请输入端口:")
    #创建两个线程：
    t1 = Thread(target=send_data)
    t2 = Thread(target=recv_data)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()

