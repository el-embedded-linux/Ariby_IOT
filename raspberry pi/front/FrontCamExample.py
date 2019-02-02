import sys
import FrontCam
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 480)

        self.label = QLabel(self)
        self.label.resize(800,480) #QLabel 생성 사이즈 변경

        self.frontCamera = FrontCam.FrontCam(self.frameUpdate) #FrontCam 클라스 생성
        self.frontCamera.start() #쓰레드 시작

        self.show()

    def frameUpdate(self, frame):
        self.label.setPixmap(frame) #label의 Pixmap 변경

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
