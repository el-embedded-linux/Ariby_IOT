import sys
import FrontCam
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 480)

        self.frontCamera = FrontCam.FrontCam() #FrontCam 클라스 생성

        self.start = QPushButton("START", self)
        self.start.clicked.connect(self.frontCamera.start) #FrontCam 의 메소드 start()
        self.start.move(100,100)

        self.stop = QPushButton("STOP", self)
        self.stop.clicked.connect(self.frontCamera.stop) #FrontCam 의 메소드 stop()
        self.stop.move(200,100)
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
