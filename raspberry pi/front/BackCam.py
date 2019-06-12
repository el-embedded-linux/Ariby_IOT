import cv2
import threading
from PyQt5.QtGui import *
import socket
import pickle
import time
class BackCam():
    data = None
    image = None
    frameUpdate = None
    pos = None
    timer = 0
    drawingPos = None
    #initializer
    def __init__(self):
        self.backcam_sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.backcam_sock.bind( ('',8080) )
        t = threading.Thread(target=self.recvFrame, args=())
        t.start()

    def recvFrame(self):
        while True:
            self.data , self.addr = self.backcam_sock.recvfrom(65535)
            self.data = pickle.loads(self.data, fix_imports=True, encoding="bytes")

            self.data = cv2.imdecode(self.data, cv2.IMREAD_COLOR)
            self.data = cv2.cvtColor(self.data, cv2.COLOR_BGR2RGB) # BGR TO RGB

            if self.pos != None:
                self.drawingPos = self.pos
                self.timer = time.time()
                self.pos = None

            if self.drawingPos!=None:
                alpha = 0.5
                output = self.data.copy()
                self.data = cv2.circle(self.data, (self.drawingPos[0],self.drawingPos[1]), self.drawingPos[2], (255, 0, 0, 128), -1)
                self.data = cv2.addWeighted(self.data, alpha, output, 1 - alpha, 0, output)

                if self.timer != 0 and time.time() - self.timer > 0.5:
                    self.drawingPos = None


            self.data = cv2.resize(self.data, dsize=(800, 480), interpolation=cv2.INTER_AREA) #라즈베리파이 스크린 사이즈에 맞게 RESIZE
            self.image = QImage(self.data, self.data.shape[1], self.data.shape[0], self.data.shape[1] * 3,QImage.Format_RGB888) #create QIamge
            if self.frameUpdate != None:
                self.frameUpdate() #callback frameUpdate
        self.backcam_sock.close()

    def stop(self):
        self.frameUpdate = None

backcam = BackCam()
