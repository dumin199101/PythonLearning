#coding=utf-8
#TFTP文件下载器
#TFTP协议：
  # 1.读写请求：操作码：1（读）2(写) ，文件名，0,模式：octet(八位组)，0
  # 2.数据包:操作码：3（2字节） ，块编号（2字节），数据（512字节）
  # 3.ACK：操作码：4 ，块编号
  # 4.Error：操作码：5
#注意解包后的数据为元组，pack打包数据为byte
import struct
from socket import *
import os

def main():
    downloadFileName = input("请输入你要下载的文件名：")
    # 1.创建socket
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    #2.发起读写请求
    requestFileData = struct.pack("!H%dsb5sb"%len(downloadFileName),1,downloadFileName.encode("utf-8"),0,"octet".encode("utf-8"),0)
    udpSocket.sendto(requestFileData,("192.168.1.141",69))

    f = open(downloadFileName,"wb")
    flag = True
    num = 0
    #3.接收服务器传递回来的数据
    while True:
        responseData = udpSocket.recvfrom(1024)
        recvData,serverInfo =responseData
        #解析数据
        opNum = struct.unpack("!H",recvData[:2])
        packetNum = struct.unpack("!H",recvData[2:4])
        print(packetNum[0],opNum)

        if opNum[0]==3:
            num = num + 1
            # 超过两个字节，重写计数
            if num == 65536:
                num = 0

            # 写入文件：
            if num==packetNum[0]:
                #防止丢包重新写入
                f.write(recvData[4:])
                num = packetNum[0]
            # 整理ACK的数据包
            ackData = struct.pack("!HH", 4, packetNum[0])
            udpSocket.sendto(ackData, serverInfo)
        elif opNum[0]==5:
            print("sorry，没有这个文件....")
            flag = False
        #跳出循环条件：
        if len(recvData)<516:
            break


    if flag == False:
        os.unlink(downloadFileName)
    else:
        f.close()

if __name__ == '__main__':
    main()