#coding=utf-8
#Web服务器:动态网站
#WSGI协议：
# env:请求头，字典方式封装
# application(env,start_response):
#  start_response('200 OK',[(响应头),(响应头)])
#  return 响应体
from socket import *
from multiprocessing import Process
import re,sys
ROOT_DIR = "./html"
PY_DIR = "./WSGI"
response_headers = ""

def start_response(status,headers):
    #构造状态行，响应头
    global response_headers
    response_headers = "HTTP/1.1 "+status+"\r\n"
    for header in headers:
        response_headers+="%s:%s\r\n"%header



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
    if filename.endswith(".py"):
        #动态文件
        try:
            m = __import__(filename[1:-3])
        except:
            response_headers = "HTTP/1.1 404 Not Found\r\n"
            response_body = "Not Found!"
        else:
            env = {}
            response_body = m.application(env,start_response)
        finally:
            cli.send((response_headers + "\r\n" + response_body).encode("utf-8"))
            cli.close()
    else:
        #静态文件
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
    sys.path.insert(1,PY_DIR) #将该目录加入搜寻路径中
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