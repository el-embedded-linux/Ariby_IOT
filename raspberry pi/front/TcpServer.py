from socket import *
import threading
import time


class TcpServer():

    PORT = 8081
    serverSock = None
    connectionSock = None
    checkTrg = False

    def __init__(self):
        pass

    def create(self):
        # Server connection option
        self.serverSock = socket(AF_INET, SOCK_STREAM)
        self.serverSock.bind(('', self.PORT))
        self.serverSock.listen(1)

        print('Waiting for port %d...'%self.PORT)
        accepter = threading.Thread(target=self.acceptServer)
        accepter.start()



    # Server Connection
    def acceptServer(self) :
        while True:
            self.connectionSock, addr = self.serverSock.accept()
            print(str(addr), ' are connected.')

            receiver = threading.Thread(target=self.receive)
            checker = threading.Thread(target=self.connectionCheck)

            receiver.start()
            checker.start()

    def send(self,text):
        self.connectionSock.send(text.encode('utf-8'))
        time.sleep(1)

    def receive(self):
        while True:
            try:
                recvData = self.connectionSock.recv(1024)
            except:
                print("소켓이 종료되었습니다.")
                break

            text = recvData.decode('utf-8')
            if text != '' and text != 'pong':
                print("client : "+recvData.decode('utf-8'))

            if text=='pong':
                self.checkTrg = False


    def connectionCheck(self):
        start = time.time()
        while True:
            while time.time()-start < 2:
                pass
            self.checkTrg = True
            self.send("ping")
            start = time.time()
            while self.checkTrg:
                if time.time()-start > 1:
                    self.connectionSock.close()
                    return

tcpServer = TcpServer()
tcpServer.create()

while True:
    text = input()
    tcpServer.send(text)
