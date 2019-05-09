import blscan
import threading
import pexpect
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 블루투스 스택위젯
class BleClicked(QLabel):
    def __init__(self, forBack):
        super().__init__()
        self.formSetting(forBack)

    def formSetting(self, forBack):
        #그룹박스
        self.groupBox = QGroupBox("검색옵션")
        self.checkBox1 = QCheckBox('ble')
        self.checkBox1.stateChanged.connect(self.checkBoxState)
        self.checkBox2 = QCheckBox('classic')
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        #위젯추가
        self.leftInnerLayOut = QVBoxLayout()
        self.leftInnerLayOut.addWidget(self.checkBox1)
        self.leftInnerLayOut.addWidget(self.checkBox2)
        self.groupBox.setLayout(self.leftInnerLayOut)
        self.leftLayOut = QVBoxLayout()
        self.leftLayOut.addWidget(self.groupBox)
        self.groupBox.setStyleSheet("color:white;font-size:20px;border:0px;")

        self.list = QListWidget(self)
        self.list.setStyleSheet("color:white;font-size:20px;border:0px;QListWidget::item{border:1px solid red;};")
        self.list.setFixedWidth(550)
        self.list.setFixedHeight(280) #550, 330

        self.quitBtn = QPushButton("Quit")
        self.quitBtn.setFixedHeight(30)
        self.quitBtn.setFixedWidth(70)
        self.quitBtn.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.quitBtn.clicked.connect(forBack.changeStack)

        self.ConnBtn = QPushButton("Connect")
        self.ConnBtn.setFixedHeight(30)
        self.ConnBtn.setFixedWidth(70)
        self.ConnBtn.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.ConnBtn.clicked.connect(self.connClicked)

        self.quitLayout = QHBoxLayout()
        self.quitLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.quitLayout.addWidget(self.ConnBtn)
        self.quitLayout.addWidget(self.quitBtn)

        self.rightLayOut = QVBoxLayout()
        self.rightLayOut.addWidget(self.list)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayOut)
        self.layout.addLayout(self.rightLayOut)
        self.backlayout = QVBoxLayout()
        self.backlayout.addLayout(self.layout)
        self.backlayout.addLayout(self.quitLayout)
        self.setLayout(self.backlayout)
        #self.layout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        #self.layout.setContentsMargins(0,0,0,0)
        #self.setStyleSheet("background-color:rgb(41,41,41)")

    def showDvice(self, device): #리스트위젯에 아이템을 추가
        print(device)
        self.list.addItem('addr : ' + '%s' % device['addr'] + ' name : ' + '%s' % device['name'] )

    def connClicked(self):
        self.pairDevice(self.itemSelect())
        print("디바이스가 연결되었습니다.")

    def checkBoxState(self): #ble, classic 선택여부 판단
            if self.checkBox1.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'ble')
            else:
                blscan.scan.stop()
            if self.checkBox2.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'classic')
            else:
                blscan.scan.stop()

    def itemSelect(self): #리스트위젯에 선택된 아이템을 MacAdress만 추출하여 str로 리턴
        selectItem = [device.text() for device in self.list.selectedItems()]
        tmpStr = selectItem[0]
        print(tmpStr[7:24])
        selectDevice = tmpStr[7:24]
        return selectDevice

    def pairDevice(self, MacAdress): #bluetoothctl을 이용한 페어링
        conn = pexpect.spawn("bluetoothctl", echo = False)
        time.sleep(0.2)
        conn.send("scan on" + "\n")
        time.sleep(0.2)
        conn.send("discoverable on" + "\n")
        time.sleep(0.2)
        conn.send("pair %s" % MacAdress + "\n")
        time.sleep(0.2)
        conn.expect("Pairing successful")
