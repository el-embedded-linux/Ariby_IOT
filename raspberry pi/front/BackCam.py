import cv2
import threading
from PyQt5.QtGui import *

class BackCam():
    isStoped = True

    #initializer
    def __init__(self, frameUpdate):
        self.frameUpdate = frameUpdate

    #thread start
    def start(self):
        if self.isStoped:
            t = threading.Thread(target=self.run, args=())
            t.start()
        else:
            print("BackCam 쓰레드는 한개만 생성 할 수 있습니다.")

    def run(self):
        self.isStoped = False
        cap = cv2.VideoCapture(-1) # -1 or 0
        cap.set(3,640)
        cap.set(4,360)
        while True:
            ret, frame = cap.read()
            if ret:
                frame = cv2.resize(frame, dsize=(800, 480), interpolation=cv2.INTER_AREA) #라즈베리파이 스크린 사이즈에 맞게 RESIZE
                image = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1] * 3,QImage.Format_RGB888) #create QIamge
                pix = QPixmap(image) #create QPixmap
                self.frameUpdate(pix) #callback frameUpdate

            else:
                break

            if self.isStoped: #flag check
                break
        cap.release()

    def stop(self):
        self.isStoped = True
