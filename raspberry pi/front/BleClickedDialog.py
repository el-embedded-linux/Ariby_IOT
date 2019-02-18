import BackCam
import SpeedMeter
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap

#다이얼로그1
class BleClickedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        self.resize(200, 200)
        self.setStyleSheet("background-color:rgb(41,41,41)")
        
        self.label = QLabel(self)
        pixmap = QPixmap('Images/ble.png')
        self.label.setPixmap(pixmap)
        self.label.setGeometry(0,0,800,480)
        self.showFullScreen()
