import cv2
import threading
from PyQt5.QtGui import *
import socket
import pickle

class BackCam():
    isStoped = True
    data = None
    image = None
    #initializer
    def __init__(self,frameUpdate):
        self.dataUpdate = frameUpdate
        self.isStoped = False
        self.backcam_sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.backcam_sock.bind( ('',8080) )
        t = threading.Thread(target=self.recvFrame, args=())
        t.start()

    def recvFrame(self):
        while True:
            self.data , self.addr = self.backcam_sock.recvfrom(65535)
            self.data = pickle.loads(self.data, fix_imports=True, encoding="bytes")
            self.data = cv2.imdecode(self.data, cv2.IMREAD_COLOR)
            self.data = cv2.resize(self.data, dsize=(800, 480), interpolation=cv2.INTER_AREA) #라즈베리파이 스크린 사이즈에 맞게 RESIZE
            self.image = QImage(self.data, self.data.shape[1], self.data.shape[0], self.data.shape[1] * 3,QImage.Format_RGB888) #create QIamge
            #self.data = QPixmap(self.data) #create QPixmap
            self.dataUpdate() #callback frameUpdate
            if self.isStoped:
                break
        self.backcam_sock.close()

    def stop(self):
        self.isStoped = True
