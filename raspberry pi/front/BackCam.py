import cv2
import threading
from PyQt5.QtGui import *

class FrontCam(threading.Thread):
    isStoped = False

    #initializer
    def __init__(self, frameUpdate):
        threading.Thread.__init__(self)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(3,640)
        self.cap.set(4,360)
        self.frameUpdate = frameUpdate

    def run(self):
        while True:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.resize(frame, dsize=(800, 480), interpolation=cv2.INTER_AREA) #라즈베리파이 스크린 사이즈에 맞게 RESIZE
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3,QImage.Format_RGB888) #create QIamge
                pix = QPixmap(image) #create QPixmap
                self.frameUpdate(pix) #callback frameUpdate

            else:
                break

            if self.isStoped: #flag check
                break
        self.cap.release()

    def stop(self):
        self.isStoped = True
