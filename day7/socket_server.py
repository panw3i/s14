import  socket

# 服务器端

server = socket.socket()
server.bind(('localhost',6969))  # 绑定监听的端口
server.listen()  # 监听
print("开始等")
server.accept() # 等待

data = server.recv(1024)
print("recv:",data)
server.send(data.uppper())

server.close()