from socket import *
import threading
import time
import RPi.GPIO as GPIO
import TurnSignal as TS

# Server Connection
def acceptServer() :
    connectionSock, addr = serverSock.accept()
    return connectionSock, addr

# Send the Function back
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
# Receive a signal from behind
def receiveBack(sock):
    while True:
        recvData = sock.recv(1024)
        print('Back :', recvData.decode('utf-8'))


port = 8081 # Port number

# Server connection option
serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('223.194.169.191', port))
serverSock.listen(1)

print('Waiting for port %d...'%port)

accepter = threading.Thread(target=acceptServer)
connectionSock, addr = acceptServer()

print(str(addr), ' are connected.')

sender = threading.Thread(target=sendBack, args=(connectionSock,))
receiver = threading.Thread(target=receiveBack, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
