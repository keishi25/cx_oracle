import socket
from contextlib import closing


def client(host, port, sock_buffer_size, cmd):

    # ソケット通信.TCPの場合は、SOCK_STREAMを使用する
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with closing(sock):
        sock.connect((host, port))
        # sock送信
        sock.send(cmd.encode("UTF-8"))
        # sock受信
        recv_msg = sock.recv(sock_buffer_size).decode('utf-8', 'replace')
        print("Response:" + recv_msg)

    return


if __name__ == '__main__':
    # ソケット送信
    host = '127.0.0.1'
    port = 4000
    sock_buffer_size = 64
    cmd = "私はclientです"

    client(host, port, sock_buffer_size, cmd)
