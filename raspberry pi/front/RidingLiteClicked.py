import threading
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class RidingLiteClicked(QLabel):
    def __init__(self, forBack):
        super().__init__()
        self.formSetting(forBack)

    def formSetting(self, forBack):
        self.speedLabel = QLabel("현재속도")
        self.speedLabel.setStyleSheet("font:bold 50px Arial; text-align:center; color:rgb(255,255,255);")
        self.speedPrintLabel = QLabel("10 km/h")
        self.speedPrintLabel.setStyleSheet("font:bold 30px Arial; text-align:center; color:rgb(255,255,255);")
        self.bpmLabel = QLabel("심박수")
        self.bpmLabel.setStyleSheet("font:bold 50px Arial; text-align:center; color:rgb(255,255,255);")
        self.bpmPrintLabel = QLabel("10 bpm")
        self.bpmPrintLabel.setStyleSheet("font:bold 30px Arial; text-align:center; color:rgb(255,255,255);")
        self.leftLayOut = QVBoxLayout()
        self.leftLayOut.addWidget(self.speedLabel, alignment=Qt.AlignHCenter)
        self.leftLayOut.addWidget(self.speedPrintLabel, alignment=Qt.AlignHCenter)
        self.leftLayOut.addWidget(self.bpmLabel, alignment=Qt.AlignHCenter)
        self.leftLayOut.addWidget(self.bpmPrintLabel, alignment=Qt.AlignHCenter)

        self.distanceDriveLabel = QLabel("주행거리")
        self.distanceDriveLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.distanceDrivePrintLabel = QLabel("10km")
        self.distanceDrivePrintLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.distanceTimeLabel = QLabel("주행시간")
        self.distanceTimeLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.distanceTimePrintLabel = QLabel("pm 1 : 05")
        self.distanceTimePrintLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.distanceTargetLabel = QLabel("목표거리")
        self.distanceTargetLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.distanceTargetPrintLabel = QLabel("5km")
        self.distanceTargetPrintLabel.setStyleSheet("font:bold 20px Arial; text-align:center; color:rgb(255,255,255);")
        self.disDriveLayOut = QVBoxLayout()
        self.disDriveLayOut.addWidget(self.distanceDriveLabel, alignment=Qt.AlignHCenter)
        self.disDriveLayOut.addWidget(self.distanceDrivePrintLabel, alignment=Qt.AlignHCenter)
        self.disTimeLayOut = QVBoxLayout()
        self.disTimeLayOut.addWidget(self.distanceTimeLabel, alignment=Qt.AlignHCenter)
        self.disTimeLayOut.addWidget(self.distanceTimePrintLabel, alignment=Qt.AlignHCenter)
        self.disTargetLayOut = QVBoxLayout()
        self.disTargetLayOut.addWidget(self.distanceTargetLabel, alignment=Qt.AlignHCenter)
        self.disTargetLayOut.addWidget(self.distanceTargetPrintLabel, alignment=Qt.AlignHCenter)
        self.rihgtLayOut = QHBoxLayout()
        self.rihgtLayOut.addLayout(self.disDriveLayOut)
        self.rihgtLayOut.addLayout(self.disTimeLayOut)
        self.rihgtLayOut.addLayout(self.disTargetLayOut)

        self.mainLayOut = QHBoxLayout()
        self.mainLayOut.addLayout(self.leftLayOut)
        self.mainLayOut.addLayout(self.rihgtLayOut)
        self.setLayout(self.mainLayOut)
