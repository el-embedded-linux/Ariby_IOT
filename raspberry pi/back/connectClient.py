from socket import *
import threading
import time
import RPi.GPIO as GPIO

btn = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def send(sock):
    sendData = ''
    while True:
        if GPIO.input(btn) :
            sendData = 'Check!'
        else :
            sendData = ''
        sock.send(sendData.encode('utf-8'))
        time.sleep(1)

def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print(recvData.decode('utf-8'))


port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass
