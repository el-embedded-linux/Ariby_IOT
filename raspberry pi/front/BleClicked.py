import blscan
import threading
import pexpect
import time
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

# 블루투스 스택위젯
class BleClicked(QLabel):
    def __init__(self, forBack, setting):
        super().__init__()
        self.setting = setting
        self.formSetting(forBack)

    def formSetting(self, forBack):
        #그룹박스
        self.groupBoxOption = QGroupBox("검색옵션")
        self.checkBoxBle = QCheckBox('Ble')
        self.checkBoxBle.stateChanged.connect(self.checkBoxState)
        self.checkBoxClassic = QCheckBox('Classic')
        self.checkBoxClassic.stateChanged.connect(self.checkBoxState)

        self.groupBoxConn = QGroupBox("연결된디바이스")
        self.checkBoxConnDev = QCheckBox('ConnectDevice')
        #self.checkBox1.stateChanged.connect(self.checkBoxState)

        #위젯추가
        self.leftInnerLayOut1 = QVBoxLayout()
        self.leftInnerLayOut1.addWidget(self.checkBoxBle)
        self.leftInnerLayOut1.addWidget(self.checkBoxClassic)
        self.leftInnerLayOut2 = QVBoxLayout()
        self.leftInnerLayOut2.addWidget(self.checkBoxConnDev)
        self.groupBoxOption.setLayout(self.leftInnerLayOut1)
        self.groupBoxConn.setLayout(self.leftInnerLayOut2)
        self.leftLayOut = QVBoxLayout()
        self.leftLayOut.addWidget(self.groupBoxOption)
        self.leftLayOut.addWidget(self.groupBoxConn)

        self.list = QListWidget(self)
        self.list.setFixedWidth(550)
        self.list.setFixedHeight(280) #550, 330

        self.quitBtn = QPushButton("Quit")
        self.quitBtn.setFixedHeight(30)
        self.quitBtn.setFixedWidth(70)
        self.quitBtn.setStyleSheet("font:bold "+self.setting.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.quitBtn.clicked.connect(forBack.changeStack)

        self.ConnBtn = QPushButton("Connect")
        self.ConnBtn.setFixedHeight(30)
        self.ConnBtn.setFixedWidth(90)
        self.ConnBtn.setStyleSheet("font:bold "+self.setting.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.ConnBtn.clicked.connect(self.connClicked)

        self.statusLabel = QLabel("Bluetooth Connect")
        self.quitLayout = QHBoxLayout()
        self.quitLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.quitLayout.addWidget(self.statusLabel)
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

        if (self.setting.thema == 'D'):
            self.setStyleSheet("background-color:rgb(41,41,41)")
            if (self.setting.fontSize2=='S'):
                self.groupBoxOption.setStyleSheet("color:white;font:bold 12px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:white;font:bold 12px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:white;font:bold 12px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 12px Arial; color:rgb(255,255,255);margin-left:20px;")

            elif (self.setting.fontSize2=='M'):
                self.groupBoxOption.setStyleSheet("color:white;font:bold 14px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:white;font:bold 14px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:white;font:bold 14px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 14px Arial; color:rgb(255,255,255);margin-left:20px;")

            else :
                self.groupBoxOption.setStyleSheet("color:white;font:bold 16px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:white;font:bold 16px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:white;font:bold 16px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 16px Arial; color:rgb(255,255,255);margin-left:20px;")
        #self.layout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        #self.layout.setContentsMargins(0,0,0,0)
        else :
            self.setStyleSheet("background-color:white")
            if (self.setting.fontSize2=='S'):
                self.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 12px Arial; color:rgb(41,41,41);margin-left:20px;")

            elif (self.setting.fontSize2=='M'):
                self.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41);margin-left:20px;")

            else :
                self.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;margin-left:20px;")
                self.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;margin-left:20px;")
                self.list.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                self.statusLabel.setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41);margin-left:20px;")

    def showDvice(self, device): #리스트위젯에 아이템을 추가
        print(device)
        self.list.addItem('addr : ' + '%s' % device['addr'] + ' name : ' + '%s' % device['name'] )

    def connClicked(self):
        self.pairDevice(self.itemSelect())

    def checkBoxState(self): #ble, classic 선택여부 판단
            if self.checkBoxBle.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'ble')
                self.list.clear()
            else:
                blscan.scan.stop()
            if self.checkBoxClassic.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'classic')
                self.list.clear()
            else:
                blscan.scan.stop()

    def itemSelect(self): #리스트위젯에 선택된 아이템을 MacAdress만 추출하여 str로 리턴
        selectItem = [device.text() for device in self.list.selectedItems()]
        tmpStr = selectItem[0]
        print(tmpStr[7:24])
        selectDevice = tmpStr[7:24]
        return selectDevice

    def pairDevice(self, MacAdress): #bluetoothctl을 이용한 페어링
        ctl = pexpect.spawn("bluetoothctl", echo = False)
        time.sleep(0.2)
        ctl.send("scan on" + "\n")
        print("5초간 기다리세요")
        time.sleep(5)
        #conn.send("discoverable on" + "\n")
        #time.sleep(0.2)
        ctl.send("pair %s" % MacAdress + "\n")
        time.sleep(0.2)
        res = ctl.expect(["Failed to pair", "Pairing successful"])
        status = True if res == 1 else False

        if status == False:
            print("다시 시도해주세요.")
            self.statusLabel.setText("다시 시도해주세요.")
