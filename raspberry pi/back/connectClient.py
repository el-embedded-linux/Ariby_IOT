import socket

def clientRun():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect(('localhost', 4001))
        s.sendall(b'Connected Client') ## str과 같은 문자열을 보낼 때는 b를 적고 써야한다.

if __name__ == '__main__' :
    clientRun()
