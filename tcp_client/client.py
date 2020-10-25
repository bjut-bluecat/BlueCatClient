from socket import *


class TcpClient:
    def __init__(self):
        # 1.创建tcp_client_socket 套接字对象
        self.tcp_client_socket = socket(AF_INET, SOCK_STREAM)
        # 作为客户端，主动连接服务器较多，一般不需要绑定端口

        # 2.连接服务器
        self.tcp_client_socket.connect(("127.0.0.1", 8888))

    def send_meg(self, name, pwd):
        # 3.向服务器发送数据
        print("name:", name, " pwd:", pwd)
        meg = "001"
        while len(name) < 20:
            name = name + '@'
        while len(pwd) < 20:
            pwd = pwd + '@'
        meg =meg + name + pwd
        self.tcp_client_socket.send(meg.encode())
        # 在udp协议中使用的sendto() 因为udp发送的为数据报，包括ip port和数据，           # 所以sendto()中需要传入address，而tcp为面向连接，再发送消息之前就已经连接上了目标主机

        # 4.接收服务器返回的消息
        recv_data = self.tcp_client_socket.recv(1024)  # 此处与udp不同，客户端已经知道消息来自哪台服务器，不需要用recvfrom了

        if recv_data:
            print("返回的消息为:", recv_data.decode('gbk'))
        else:
            print("对方已离线。。")


    def destory_client(self):
        self.tcp_client_socket.close()


def main():
    client = TcpClient()
    client.send_meg()


if __name__ == '__main__':
    main()
