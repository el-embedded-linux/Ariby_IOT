import threading
import socket
from BackCam import *

class front_udp_server():
    data = None
    image = None
    getMessage = None

    #initializer
    def __init__(self):
        self.backcam_sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.backcam_sock.bind( ('',8082) )
        t = threading.Thread(target=self.recvFrame, args=())
        t.start()

    def recvFrame(self):
        while True:
            self.data , self.addr = self.backcam_sock.recvfrom(65535)
            pos = self.data.decode('utf-8').split(',');
            if pos[0] == "car":
                left = int(pos[2])+(int(pos[4])-int(pos[2]))//2
                top = int(pos[1])+(int(pos[3])-int(pos[1]))//2
                t = int((int(pos[4])-int(pos[2]))+(int(pos[3])-int(pos[1])))//4
                print(str(left)+"/"+str(top)+"/"+str(t))
                backcam.pos = [left,top,t]

        self.backcam_sock.close()

front_udp_server = front_udp_server()
