from socket import *
import threading
import time
import RPi.GPIO as GPIO
import TurnSignal as TS

# 서버 연결
def acceptServer() :
    connectionSock, addr = serverSock.accept()
    return connectionSock, addr

# 후방쪽으로 신호를 보내는 함수
def sendBack(sock):
    sendData = ''
    while True:
        if TS.turn.direction == "Emer" :
            sendData = 'Emer ON!!'
        else :
            if TS.turn.direction == "Left" :
                sendData = 'Left ON!!'
            elif TS.turn.direction == "Right" :
                sendData = 'Right ON!!'
            else :
                sendData = ''

        sock.send(sendData.encode('utf-8'))
        time.sleep(1)

time.sleep(1)
# 후방쪽에서 신호를 받는 함수
def receiveBack(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8081 # 포트번호

#서버 연결설정
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

accepter = threading.Thread(target=acceptServer)
connectionSock, addr = acceptServer()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=sendBack, args=(connectionSock,))
receiver = threading.Thread(target=receiveBack, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
