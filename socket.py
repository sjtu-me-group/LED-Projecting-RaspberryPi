import socket

flag = True

# 主进程定义socket对象server = socket.socket(),并且要在程序结束时关闭server.close()
def receive(server):
    # 绑定ip和端口
    server.bind(('localhost', 6666))

    # 监听绑定的端口
    server.listen()

    # 方便识别打印一个我在等待
    print("I'm waiting the connect...")


    # 这里用两个值接受，因为链接上之后使用的是客户端发来请求的这个实例
    # 所以下面的传输要使用conn实例操作
    conn, addr = server.accept()

    # 打印链接成功
    print('Connect success!')
    f=open('./data.py','w')
    # 进入循环
    while flag:

        # 接受数据并赋给data
        data = conn.recv(1024).decode()

        # 判断
        if data != None:

            # 写入收到数据
            print('收到：', data)
            f.write(data)
        


        else:

            return None
