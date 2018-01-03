#coding=utf-8
#Web服务器:读取文件信息
from socket import *
from multiprocessing import Process
import re
ROOT_DIR = "./html"
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
    lines = data.decode("utf-8").splitlines()
    for line in lines:
        print(line)
    request_start_line = lines[0]
    filename = re.match(r"\w+ +([^ ]*) ",request_start_line).group(1)
    print(ROOT_DIR+filename)
    print("*"*100)
    try:
        file = open(ROOT_DIR+filename,"rb")
    except IOError:
        # 给客户端做出响应
        response_line = "HTTP/1.1 404 NOT Found\r\n"
        response_header = "Server:Tomcat\r\n"
        response_data = "File is not exists!"
    else:
        fileinfo = ""
        while True:
            content = file.read(1024)
            if len(content)==0:
                break
            fileinfo +=content.decode("utf-8")
        file.close()
        # 给客户端做出响应
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server:Tomcat\r\n"
        response_data = fileinfo
    finally:
        cli.send((response_line + response_header + "\r\n" + response_data).encode("utf-8"))
        cli.close()


if __name__ == '__main__':
    serverSocket = socket(AF_INET,SOCK_STREAM)
    serverSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    serverSocket.bind(('',8899))
    serverSocket.listen(5)
    while True:
        #监听客户端连接
        cli,addr = serverSocket.accept()
        p = Process(target=clientHandle,args=(cli,addr))
        p.start()
        cli.close()