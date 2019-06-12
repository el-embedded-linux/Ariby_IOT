import cv2
import BackCam
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 480)

        #이미지
        self.label = QLabel(self)
        self.label.resize(800,480)
        self.frontCamera = BackCam.BackCam(self.getFrameUpdate)
        self.frontCamera.start()

        self.show()

    def getFrameUpdate(self, frame):
        self.label.setPixmap(frame)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
