# 网络编程

## Socket套接字

### 套接字类型

- 流式套接字 SOCK_STREAM 基于TCP协议
- 数据报套接字 SOCK_DGRAM 基于UDP协议
- 原始套接字 SOCK_RAW 允许对较底层的协议直接访问

### 套接字Address Family

- AF_INET IPv4寻址
- AF_INET6 IPv6寻址
- AF_UNIX 进程间通信寻址

### TCP编程

#### socket模块

```Python
# socket.socket(family=-1, type=-1, proto=-1, fileno=None)
# family是套接字Address Family
# type是套接字类型
# proto

# 创建TCP套接字
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定套接字到本地IP与端口
HOST = '127.0.0.1'
PORT = 8001
s.bind((HOST, PORT))

# 监听连接
s.listen(5)

# 接收连接
s.accept()

s.recv
s.send
s.close


```
