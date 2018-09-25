# _*_coding:utf-8 _*_
__author__ = 'Jay'

# 客户端
'''
客户端实现socket通信一般步骤：
使用socket()函数创建客户端套接字
使用connect()函数发出也服务器建立连接的请求（调用前可以不用bind()端口号，由系统自动完成）
连接建立后使用send()函数发送数据，或使用recv()函数接收数据
使用closesocet()函数关闭套接字
'''
import socket

client = socket.socket() #声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

while True:
    msg = input(">>:").strip()
    if len(msg) == 0:continue
    client.send(msg.encode("utf-8"))
    data = client.recv(10240)
    print("recv:",data.decode())

client.close()