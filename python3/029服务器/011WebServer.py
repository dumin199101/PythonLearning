#coding=utf-8
#gevent版本服务器
import gevent
from gevent import monkey,socket
monkey.patch_all()

def handle_request(cli):
    while True:
        data = cli.recv(1024)
        if not data:
            cli.close()
            break
        print("recv:",data)
        cli.send(data)


def server(port):
    s = socket.socket()
    s.bind(('',port))
    s.listen(5)
    while True:
        cli,addr = s.accept()
        gevent.spawn(handle_request,cli)




if __name__ == '__main__':
    server(9998)