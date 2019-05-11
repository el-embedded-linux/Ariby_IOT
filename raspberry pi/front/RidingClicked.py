import platform
import BackCam
if platform.system()=='Linux':
    import FrontCam
    import SpeedMeter
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 주행다이얼로그
class RidingClicked(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.cameraLabel = QLabel(self)
        self.heartRateImage = QMovie("Images/heart.gif", QByteArray(), self)
        self.heartRateScreen = QLabel(self)
        self.heartRateScreen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.heartRateScreen.setAlignment(Qt.AlignCenter)
        self.heartRate = QLabel(self)
        self.speed = QLabel(self)
        self.backButton = QPushButton(self)

        self.cameraLabel.setGeometry(0,0,800,480)
        self.heartRateScreen.setGeometry(15,20,80,80)
        self.heartRate.setGeometry(100,10,150,100)
        self.speed.setGeometry(510,10,280,100)
        self.backButton.setGeometry(712,428,70,30)

        self.cameraLabel.setStyleSheet("background-color:rgba(255,0,0,0)")
        self.heartRate.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 80px Arial;")
        self.heartRateScreen.setStyleSheet("background-color:rgba(255,255,255,0)")
        self.speed.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 80px Arial;")
        self.backButton.setText("QUIT")
        self.backButton.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.backButton.clicked.connect(self.quit)

        SpeedMeter.speedmeter.callback = self.speedUpdate #콜백함수 등록
        SpeedMeter.speedmeter.start_b() #테스트용 쓰레드 시작

        self.backCamera = BackCam.BackCam(self.frameUpdate) #카메라 객체 생성
        if platform.system()=='Linux':
            self.frontCamera = FrontCam.FrontCam() #카메라 객체 생성 & 녹화 시작

        self.heartRateImage.setCacheMode(QMovie.CacheAll)
        self.heartRateImage.setSpeed(120)
        self.heartRateScreen.setMovie(self.heartRateImage)
        self.heartRateImage.start()

        self.show()

    def heartRateUpdate(self, data):
        if int(data) < 10:
            dataOutput = '0' + data
        else:
            dataOutput = data

        self.heartRate.setText(dataOutput)

    def speedUpdate(self, data): #속도 데이터 수신 콜백함수
        if int(data) < 10 :
            dataOutput = '0' + data
        else :
            dataOutput = data
        self.heartRateUpdate(data)      #심박수 완료 후 변경
        self.speed.setText(dataOutput+"km/h")

    def frameUpdate(self):
        self.cameraLabel.clear() # Label을 clear하여 paintEvent가 실행되도록 함

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawImage(0,0,self.backCamera.image) # 카메라객체에 가장 최근 프레임을 그림


    def quit(self):
        self.heartRateImage.stop()
        SpeedMeter.speedmeter.stop()
        if platform.system()=='Linux':
            self.frontCamera.stop()
        self.backCamera.stop()
        self.close()
