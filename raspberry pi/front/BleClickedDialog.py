import BackCam
import SpeedMeter
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap, QMovie

#블루투스 다이얼로그
class BleClickedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        #좌표값
        x = 40
        y = 40
        w = 400
        h = 50

        #초기화
        self.bleBtn = {}
        self.bleBtnAddr = {}
        bleDeviceFindNum=0

        #디바이스를 선택하기 전 공백처리
        #tmpBle = []

        #디바이스를 5초간격으로 찾기
        devices = SpeedMeter.scanble(timeout=5)

        #뒷배경 삽입
        self.backimg = QLabel(self)
        pixmap = QPixmap('Images/ble.jpg')
        self.backimg.setPixmap(pixmap)
        self.backimg.setGeometry(0,0,800,480)

        #연결하시겠습니까? 버튼 생성
        self.connectLabel = QLabel("Connect", self)
        self.connectLabel.setGeometry(x+440, 420, 120, 50)
        self.connectLabel.setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding:15px 3px; outline:0px;")
        self.connectLabel.mousePressEvent = self.exitEvent
        self.connectLabel.setAlignment(Qt.AlignCenter)
        self.connectLabel.setVisible(False)

        #나가기 버튼
        self.closeLabel = QLabel("Exit", self)
        self.closeLabel.setGeometry(x+580, 420, 120, 50)
        self.closeLabel.setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding:15px 3px; outline:0px;")
        self.closeLabel.mousePressEvent = self.exitEvent
        self.closeLabel.setAlignment(Qt.AlignCenter)

        #선택된 디바이스 어드레스값 표출
        self.selectLabel = QLabel("블루투스 기기를 선택하세요",self)
        self.selectLabel.setGeometry(x+440, 40, 260, 100)
        self.selectLabel.setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding:15px 3px; outline:0px;")

        #gif 블루투스 애니메이션
        self.bleGif = QLabel(self)
        blebutton2 = QMovie('Images/blebutton.gif')
        self.bleGif.setMovie(blebutton2)
        blebutton2.start()
        self.bleGif.move(480, 150)
        self.bleGif.setVisible(False)

        #디바이스 찾기 이벤트
        for device in devices:
            self.bleBtn[bleDeviceFindNum] = QPushButton(device['name'] + '\n' + device['addr'], self)
            self.bleBtnAddr[bleDeviceFindNum] = device['addr']
            self.bleBtn[bleDeviceFindNum].clicked.connect(lambda state, button = self.bleBtn[bleDeviceFindNum], addr = self.bleBtnAddr[bleDeviceFindNum] : self.clickedEvent(state, button, addr))
            self.bleBtn[bleDeviceFindNum].setStyleSheet("background-color:rgb(106, 230, 197);")
            self.bleBtn[bleDeviceFindNum].setGeometry(x,y,w,h)
            bleDeviceFindNum += 1
            y += 70

        #디바이스 어드레스값 설정
        #SpeedMeter.speedmeter.setAddress()

        #디바이스가 설정되었는지 확인
        #SpeedMeter.speedmeter.isConnected

        self.showFullScreen()

    def exitEvent(self, event):
        self.close()

    def clickedEvent(self, state, button, addr):
        #button = 디바이스 모든 정보값 / addr = 디바이스 주소값
        self.selectLabel.setText(button.text() + '\n' + "가 선택되었습니다.")
        self.bleGif.setVisible(True)
        self.connectLabel.setVisible(True)
