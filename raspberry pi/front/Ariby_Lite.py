import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #self.setGeometry(0, 0, 320, 240)
        a=40
        #스피드
        self.SpeedLabel = QLabel("Speed\n10Km/h")
        self.SpeedLabel.setStyleSheet("color:rgb(255,255,255); font-size:%dpx; font:bold" % a)
        self.SpeedLabel.setAlignment(Qt.AlignCenter)
        self.SpeedLayOut = QVBoxLayout()
        self.SpeedLayOut.addWidget(self.SpeedLabel)

        #4칸(그리드레이아웃)
        self.BPMLabel = QLabel("BPMLabel\n14.0")
        self.BPMLabel.setStyleSheet("color:rgb(255,255,255); font-size:20px; font:bold")
        self.BPMLabel.setAlignment(Qt.AlignCenter)
        self.CalLabel = QLabel("CalLabel\n6.37")
        self.CalLabel.setStyleSheet("color:rgb(255,255,255); font-size:20px; font:bold")
        self.CalLabel.setAlignment(Qt.AlignCenter)
        self.RTimeLabel = QLabel("RTimeLabel\n10:16")
        self.RTimeLabel.setStyleSheet("color:rgb(255,255,255); font-size:20px; font:bold")
        self.RTimeLabel.setAlignment(Qt.AlignCenter)
        self.DISTLabel = QLabel("DISTLabel\n12.54km")
        self.DISTLabel.setStyleSheet("color:rgb(255,255,255); font-size:20px; font:bold")
        self.DISTLabel.setAlignment(Qt.AlignCenter)

        self.FourInnerLayOut = QGridLayout()
        self.FourInnerLayOut.addWidget(self.BPMLabel, 0, 0)
        self.FourInnerLayOut.addWidget(self.CalLabel, 0, 1)
        self.FourInnerLayOut.addWidget(self.RTimeLabel, 1, 0)
        self.FourInnerLayOut.addWidget(self.DISTLabel, 1, 1)

        self.Verbtn1 = QPushButton("Ver1")
        self.Verbtn2 = QPushButton("Ver2")
        self.Verbtn3 = QPushButton("Ver3")

        self.VerLayOut = QHBoxLayout()
        self.VerLayOut.addWidget(self.Verbtn1)
        self.VerLayOut.addWidget(self.Verbtn2)
        self.VerLayOut.addWidget(self.Verbtn3)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SpeedLayOut)
        self.layout.addLayout(self.FourInnerLayOut)
        self.layout.addLayout(self.VerLayOut)

        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.resize(240, 320)
    mywindow.setStyleSheet("background-color:rgb(0,0,0)")
    mywindow.show()

    app.exec_()
