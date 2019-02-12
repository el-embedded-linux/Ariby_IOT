import cv2
import cam
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 10
        self.top = 10
        self.width = 800
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)

        #이미지
        self.label = QLabel(self)
        self.label.resize(800,480)
        self.frontCamera = cam.frontCamera(self.getFrameStart)
        self.frontCamera.start()

        self.show()

    def getFrameStart(self, frame):
        self.label.setPixmap(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
