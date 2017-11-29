import socket,time
import threading
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听客户端连接:
s.bind(('127.0.0.1', 8888))
s.listen(5) #监听客户端连接的数量
print('Waiting for connection...')
def tcplink(sock,addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b"Welcome")
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8')) #返回数据给客户端
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    sock,addr = s.accept() #接收连接
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink,args=(sock,addr)) #单线程在处理连接的过程中，无法接受其他客户端的连接
    t.start()







