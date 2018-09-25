# _*_coding:utf-8 _*_
__author__ = 'Jay'

# 服务端
'''
服务器端实现socket一般步骤：
使用socket()函数创建服务器端通信套接字
使用bind()函数将创建的套接字与服务器地址绑定
使用listen()函数使服务器套接字做好接收连接请求准备
使用accept()接收来自客户端由connect()函数发出的连接请求
根据连接请求建立连接后，使用send()函数发送数据，或者使用recv()函数接收数据
使用closesocket()函数关闭套接字（可以先用shutdown()函数先关闭读写通道）
'''
import socket
server = socket.socket()
server.bind(('localhost',6969)) #绑定要监听端口
server.listen(5) #监听

print("我要开始等电话了")
while True:
    conn, addr = server.accept()  # 等电话打进来
    # conn就是客户端连过来而在服务器端为其生成的一个连接实例
    print(conn, addr)
    print("电话来了")
    count = 0
    while True:
        data = conn.recv(1024)
        print("recv:",data)
        if not data:
            print("client has lost...")
            break
        conn.send(data.upper())
        count+=1
        if count >10:break

server.close()