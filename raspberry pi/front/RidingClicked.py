import platform
from BackCam import *
if platform.system()=='Linux':
    #import FrontCam
    import SpeedMeter
    from AndroidBluetooth import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# 주행다이얼로그
class RidingClicked(QDialog):
    def __init__(self):
        super().__init__()
        self.test = 1
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.receiveSpeedCount = 0
        self.wheelDiameter = 10
        self.formSetting()
        self.timerStart()

    def formSetting(self):

        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.cameraLabel = QLabel(self)
        self.heartRateImage = QMovie("Images/heart.gif", QByteArray(), self)
        self.heartRateScreen = QLabel(self)
        self.heartRate = QLabel(self)
        self.distance = QLabel(self)
        self.direction = QLabel(self)
        self.speed = QLabel(self)
        self.kmh = QLabel(self)
        self.ridingTime = QLabel(self)
        self.ridingDistance = QLabel(self)
        self.backButton = QPushButton(self)

        self.cameraLabel.setGeometry(0,0,800,480)
        self.heartRateScreen.setGeometry(15,20,80,80)
        self.heartRate.setGeometry(100,10,150,100)
        self.distance.setGeometry(490, 32, 60, 20)
        self.direction.setGeometry(490, 55, 60, 40)
        self.speed.setGeometry(550,10,180,100)
        self.kmh.setGeometry(690,20,100,80)
        self.ridingTime.setGeometry(205,428,180,30)
        self.ridingDistance.setGeometry(405,428,220,30)
        self.backButton.setGeometry(712,428,70,30)

        self.heartRateScreen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.heartRateScreen.setAlignment(Qt.AlignCenter)
        self.distance.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.direction.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)

        self.cameraLabel.setStyleSheet("background-color:rgba(255,255,255,0)")
        self.heartRate.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 80px Arial;")
        self.heartRateScreen.setStyleSheet("background-color:rgba(255,255,255,0)")
        self.distance.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 16px Arial;")
        self.direction.setStyleSheet("background-color:rgba(255,255,255,0);")
        self.speed.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 80px Arial;")
        self.kmh.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 40px Arial;")
        self.ridingTime.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 16px Arial;")
        self.ridingDistance.setStyleSheet("background-color:rgba(255,255,255,0);color:white;font:bold 16px Arial;")
        self.backButton.setText("Quit")
        self.backButton.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.backButton.clicked.connect(self.quit)

        if platform.system() == 'Linux':
            SpeedMeter.speedmeter.callback = self.speedUpdate #콜백함수 등록
            SpeedMeter.speedmeter.start() #테스트용 쓰레드 시작
            androidBluetooth.setCallback(self.BluetoothRead) #블루투스 Read 함수 전달
            #self.frontCamera = FrontCam.FrontCam() #카메라 객체 생성 & 녹화 시작

        backcam.frameUpdate = self.frameUpdate #영상 라벨 전달

        self.heartRateImage.setCacheMode(QMovie.CacheAll)
        self.heartRateImage.setSpeed(120)
        self.heartRateScreen.setMovie(self.heartRateImage)
        self.heartRateImage.start()

        self.kmh.setText("km/h")

        self.fontEffect(self.speed)
        self.fontEffect(self.kmh)
        self.fontEffect(self.distance)
        self.fontEffect(self.heartRate)
        self.fontEffect(self.ridingDistance)
        self.fontEffect(self.ridingTime)
        self.show()

    def timerStart(self):
        global timer
        timer = threading.Timer(1, self.timerStart)
        self.ridingTime.setText('Riding Time : %02d:%02d:%02d' % (self.hours, self.minutes, self.seconds))
        self.seconds+=1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
        timer.start()

    def timerStop(self):
        timer.cancel()

    def fontEffect(self, item):
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(8)
        effect.setColor(QColor("black"))
        effect.setOffset(1,1)
        item.setGraphicsEffect(effect)

    def heartRateUpdate(self, data):
        if int(data) < 10:
            dataOutput = ' ' + data
        else:
            dataOutput = data

        self.heartRate.setText(dataOutput)   #심박수 완료 후 변경

    def navUpdate(self, distance, direction):  # 네비 테스트 완료 후 변경
        if direction == 'right':
            img = QPixmap('Images/right.png')
        elif direction == 'left':
            img = QPixmap('Images/left.png')
        else:
            img = QPixmap('Images/straight.png')
        self.distance.setText(str(distance) + 'm')
        self.direction.setPixmap(img)

    def speedUpdate(self, data):  # 속도 데이터 수신 콜백함수
        self.receiveSpeedCount += 1
        data = str(int(float(data[:-2])))
        dataOutput = data

        if int(data) < 10:
            dataOutput = '    ' + data
        elif int(data) < 100:
            dataOutput = '  ' + data
        self.heartRateUpdate(data)  # 심박수 완료 후 변경
        self.speed.setText(dataOutput)
        self.ridingDistance.setText("Riding Distance : "+str(self.receiveSpeedCount*self.wheelDiameter)+"km/h")

    def frameUpdate(self):
        self.cameraLabel.clear() # Label을 clear하여 paintEvent가 실행되도록 함

    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        if backcam.image != None:
            painter.drawImage(0,0,backcam.image) # 카메라객체에 가장 최근 프레임을 그림

    def BluetoothRead(self, text):
        print(text)
        self.textList = text.split("/")
        self.navUpdate(self.textList[0], self.textList[1])
        #TODO text에 따라 다른 네비게이션이 표시되도록 수정


    def quit(self):
        self.heartRateImage.stop()
        self.timerStop()
        if platform.system()=='Linux':
            SpeedMeter.speedmeter.stop()
            #self.frontCamera.stop()
            androidBluetooth.stop()
        backcam.stop()
        self.close()
