import bluetooth
import threading

class AndroidBluetooth():
    callback = None

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
            client_socket,address = server_socket.accept()
            print("안드로이드가 연결되었습니다.. : ",address)
            clientConnected = threading.Thread(target=self.clientConnected, args=(client_socket,))
            clientConnected.start()

    def clientConnected(self, client_socket):
        while True:
            try:
                data = client_socket.recv(1024)
                dataToString = data.decode("utf-8")
                if self.callback!=None:
                    self.callback(dataToString)

                if dataToString == "quit":
                    break
            except ConnectionError as err:
                break
        print("안드로이드 연결이 종료되었습니다.")
        client_socket.close()

def func(data):
    print(data)

androidBluetooth = AndroidBluetooth()
androidBluetooth.setCallback(func)
