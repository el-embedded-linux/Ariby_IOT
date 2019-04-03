import BackCam
#import FrontCam   #라파
import SpeedMeter
from PyQt5.QtWidgets import *

# 주행다이얼로그
class RidingClicked(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        self.resize(800, 480)
        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.cameraLabel = QLabel(self)
        self.speed = QLabel(self)
        self.backButton = QPushButton(self)

        BackCam.backCamera.setGetFrameFunc(self.back)

        self.cameraLabel.setGeometry(0,0,800,480)
        self.speed.setGeometry(510,10,300,100)
        self.backButton.setGeometry(712,428,70,30)

        self.speed.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 80px Arial;")
        self.backButton.setText("QUIT")
        self.backButton.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.backButton.clicked.connect(self.quit)

        SpeedMeter.speedmeter.callback = self.SpeedUpdate #콜백함수 등록
        SpeedMeter.speedmeter.start_b() #테스트용 쓰레드 시작

        #FrontCam.frontCamera.start()


    def SpeedUpdate(self, data): #속도 데이터 수신 콜백함수
        if int(data) < 10 :
            dataOutput = '0' + data
        else :
            dataOutput = data

        self.speed.setText(dataOutput+"km/h")

    def back(self, frame):
        self.cameraLabel.setPixmap(frame)

    def quit(self):
        SpeedMeter.speedmeter.stop()
        self.close()
