#coding=utf-8
#广播只存在UDP协议中，TCP协议中不存在：
#UDP广播：
#单播：1对1
#多播：1对多
#广播：1对all
#setsocketopt(level,opt,value)
import socket
dest = ("<broadcast>",8080)
udpSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udpSocket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
udpSocket.sendto("Hello".encode("gb2312"),dest)

