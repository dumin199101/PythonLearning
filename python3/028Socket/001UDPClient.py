#coding=utf-8
#单工：收音机，同一时刻只能接收
#半双工：对讲机：同一时刻只能接收或发送
#全双工：电话：同一时刻既能接收又能发送
from socket import *
s = socket(AF_INET,SOCK_DGRAM)
s.sendto("Hello upd,i am coming".encode("utf-8"),("192.168.1.101",7777))

