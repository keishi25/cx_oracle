import socket
from contextlib import closing



def server(host, port, backlog, sock_buffer_size):

    print('waiting for request')
    # １．ソケット生成.TCPの場合は、SOCK_STREAMを使用する
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    with closing(sock):
        # ２．ソケット登録
        sock.bind((host, port))
        # ３．ソケット接続準備
        sock.listen(backlog)  # backlog=サーバにacceptされていないクライアントからの接続要求を保持しておくキューの最大長
        # ４．ソケット接続
        while True:
            conn, address = sock.accept()
            with closing(conn):
                # ５．ソケット受信
                msg = conn.recv(sock_buffer_size)
                msg = msg.decode('utf-8', 'replace')
                print(msg)
                msg_send = "サーバからの返信"
                # ６．ソケット返信.bytes(=バイト型)で返信を行う
                conn.send(msg_send.encode('UTF-8'))
    return


if __name__ == '__main__':
    host = '127.0.0.1'
    port = 4000
    backlog = 1
    sock_buffer_size = 64

    server(host, port, backlog, sock_buffer_size)
    quit()
