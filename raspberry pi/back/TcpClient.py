from socket import *
import threading
import time


class TcpClient():

    ADDRESS = '192.168.0.2'
    PORT = 8081
    clientSock = None
    connecter = None
    isconnect = False
    func = None

    def __init__(self):
        pass

    def setCallback(self, func):
        self.func = func

    def connect(self):
        self.clientSock = socket(AF_INET, SOCK_STREAM)
        connect_thread = threading.Thread(target=self.connect_thread, args=())
        connect_thread.start()

    def connect_thread(self):
        print("연결중입니다.")
        time.sleep(5)
        self.clientSock.connect((self.ADDRESS, self.PORT))
        receiver = threading.Thread(target=self.receive, args=())
        receiver.start()

    def send(self,text):
        try:
            self.clientSock.send(text.encode('utf-8'))
        except:
            self.connect()
        time.sleep(1)

    def receive(self):
        while True:
            try:
                recvData = self.clientSock.recv(1024)
            except:
                self.clientSock.close()
                self.connect()
                break

            text = recvData.decode('utf-8')
            if text != '' and text != 'ping':
                if self.func != None:
                    self.func(text)

            if text == 'ping':
                self.send('pong')

tcpClient = TcpClient()
tcpClient.connect()
