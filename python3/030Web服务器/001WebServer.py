#coding=utf-8
#Web服务器：返回固定返回值
from socket import *
from multiprocessing import Process
def clientHandle(cli,addr):
    """
    多进程处理函数,处理客户端请求
    :param cli:
    :param addr:
    :return:
    """
    data = cli.recv(1024)
    print("Receive Data from %s:%s"%(addr,data.decode("utf-8")))
    #给客户端做出响应
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "Server:Tomcat\r\n"
    response_data = "Hello World,I am here!"
    cli.send((response_line+response_header+"\r\n"+response_data).encode("utf-8"))
    print("Response Data:%s"%response_data)
    cli.close()


if __name__ == '__main__':
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.bind(('',7788))
    serverSocket.listen(5)
    while True:
        #监听客户端连接
        cli,addr = serverSocket.accept()
        p = Process(target=clientHandle,args=(cli,addr))
        p.start()
        cli.close()

# Receive Data from ('192.168.1.101', 50521):GET / HTTP/1.1
# Host: 192.168.1.101:7788
# User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
# Accept-Encoding: gzip, deflate
# Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
# Upgrade-Insecure-Requests: 1
# X-Lantern-Version: 4.4.1