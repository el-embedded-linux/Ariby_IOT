import cv2
import threading
from PyQt5.QtGui import *
import socket
import struct
import pickle

class BackCam():
    isStoped = True

    #initializer
    def __init__(self):
        self.frameUpdate = None

    def setGetFrameFunc(self,frameUpdate):
        self.frameUpdate = frameUpdate

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=())
            t.start()
        else:
            print("BackCam 쓰레드는 한개만 생성 할 수 있습니다.")

        self.isStoped = False
        self.backcam_sock = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
        self.backcam_sock.bind( ('',8080) )

    def run(self):
        while True:
            #print('do')
            data , addr = self.backcam_sock.recvfrom(65535)
            if self.frameUpdate != None:
                frame = pickle.loads(data, fix_imports=True, encoding="bytes")
                frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
                frame = cv2.resize(frame, dsize=(800, 480), interpolation=cv2.INTER_AREA) #라즈베리파이 스크린 사이즈에 맞게 RESIZE
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3,QImage.Format_RGB888) #create QIamge
                pix = QPixmap(image) #create QPixmap
                self.frameUpdate(pix) #callback frameUpdate
        self.backcam_sock.close()

    def stop(self):
        self.frameUpdate = None

backCamera = BackCam()
