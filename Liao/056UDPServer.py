import socket
#UDP编程：
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#绑定端口：
s.bind(('127.0.0.1',9999))
print('Bind UDP on 9999...')
while True:
    #接收数据：
    data,addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr) #此处的端口号为进程的端口号
    reply = 'Response from Server:Hello, %s!' % data.decode('utf-8')
    s.sendto(reply.encode('utf-8'),addr) #发送数据给客户端


