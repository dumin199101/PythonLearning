#coding=utf-8
#select版服务器：原理：轮询机制，32位最多接受1024个套接字，64位最多接受2048个套接字
#select(可读，可写，异常)
import select,socket,sys
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('',7788))
server.listen(10)
inputs = [server,sys.stdin]
running = True
while True:
    # 调用 select 函数，阻塞等待
    readable,writable,exceptional = select.select(inputs,[],[])
    for sock in readable:
        if sock==server:
            cli,addr = sock.accept()
            inputs.append(cli)
        elif sock==sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                inputs.remove(sock)
                sock.close()
    if not running:
        break
server.close()



