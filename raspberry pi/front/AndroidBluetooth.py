import bluetooth
import threading

class AndroidBluetooth():
    callback = None
    client_socket = None
    #initializer
    def __init__(self):
        server_socket=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
        port = 1
        server_socket.bind(("",port))
        server_socket.listen(1)
        readyToConnect = threading.Thread(target=self.readyToConnect, args=(server_socket,))
        readyToConnect.start()

    def setCallback(self, func):
        self.callback = func

    def readyToConnect(self, server_socket):
        while True:
            self.client_socket,address = server_socket.accept()
            print("안드로이드가 연결되었습니다.. : ",address)
            clientConnected = threading.Thread(target=self.clientConnected, args=())
            clientConnected.start()

    def clientConnected(self):
        while True:
            try:
                data = self.client_socket.recv(1024)
                dataToString = data.decode("utf-8")
                if self.callback!=None:
                    self.callback(dataToString)
                    self.send(dataToString)
                if dataToString == "quit":
                    break

            except ConnectionError as err:
                break
        print("안드로이드 연결이 종료되었습니다.")
        self.client_socket.close()
        self.client_socket = None

    def send(self, text):
        if self.client_socket!=None:
            self.client_socket.send(text.encode("utf-8"))

    def stop(self):
        if self.client_socket!=None:
            self.send("quit")
            self.client_socket.close()
            self.client_socket = None

def func(data):
    print(data)

androidBluetooth = AndroidBluetooth()
#androidBluetooth.setCallback(func)
