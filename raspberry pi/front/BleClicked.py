import blscan
import threading
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
        self.list.setFixedHeight(330)

        self.quitLabel = QLabel()
        self.quitLabel.setFixedHeight(60)
        self.quitLabel.setFixedWidth(760)

        self.quitBtn = QPushButton("QUIT")
        self.quitBtn.setFixedHeight(30)
        self.quitBtn.setFixedWidth(70)
        self.quitBtn.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.quitBtn.clicked.connect(forBack.changeStack)

        self.quitLayout = QGridLayout()
        self.quitLayout.setContentsMargins(0,0,0,0)
        self.quitLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.quitLayout.addWidget(self.quitBtn)

        self.quitLabel.setLayout(self.quitLayout)

        self.rightLayOut = QVBoxLayout()
        self.rightLayOut.addWidget(self.list)

        self.layout = QHBoxLayout()
        self.layout.addLayout(self.leftLayOut)
        self.layout.addLayout(self.rightLayOut)
        self.layout.addWidget(self.quitLabel)
        self.setLayout(self.layout)
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.setContentsMargins(0,0,0,0)
        self.setStyleSheet("background-color:rgb(41,41,41)")

    def showDvice(self, device):
        print(device)
        self.list.addItem('%s' % device)

    def checkBoxState(self):
            if self.checkBox1.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'ble')
            else:
                blscan.scan.stop()
            if self.checkBox2.isChecked() == True:
                devices = blscan.scan.start(self.showDvice,'classic')
            else:
                blscan.scan.stop()
