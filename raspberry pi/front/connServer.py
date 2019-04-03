import socket

 
def runServer() : ## 서버열기
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) ## IP4v이기 때문에 AF_INET 사용
    sock.bind(('localhost', 4001))
    sock.listen(1)

    conn, addr = sock.accept()
    data = conn.recv(1024)
    print(data)



