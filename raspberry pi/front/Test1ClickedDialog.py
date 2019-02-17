import BackCam
import SpeedMeter
from PyQt5.QtWidgets import *

#다이얼로그1
class Test1ClickedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        self.resize(200, 200)
        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.label = QLabel(self)
        self.test = QLabel(self)
        self.frontCamera = BackCam.BackCam(self.back)
        self.frontCamera.start()
        self.label.setGeometry(0,0,800,480)
        self.test.setGeometry(0,0,200,200)
        self.test.setStyleSheet("background-color:rgba(255,255,255,0)")

        speedmeter = SpeedMeter.SpeedMeter('F0:45:DA:10:B9:C1',self.SpeedUpdate)
        speedmeter.start_b()

        self.showFullScreen()


    def SpeedUpdate(self, data):
        self.test.setText("test"+data)
        print(data)


    def back(self, frame):
        self.label.setPixmap(frame)

