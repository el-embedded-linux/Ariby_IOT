import threading
import socket

class udp_server():
    data = None
    image = None
    getMessage = None

    #initializer
    def __init__(self):
        self.backcam_sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.backcam_sock.bind( ('',8081) )
        t = threading.Thread(target=self.recvFrame, args=())
        t.start()

    def recvFrame(self):
        while True:
            self.data , self.addr = self.backcam_sock.recvfrom(65535)
            if self.getMessage != None:
                self.getMessage(self.data.decode('utf-8')) #callback frameUpdate
        self.backcam_sock.close()

udp_server = udp_server()
