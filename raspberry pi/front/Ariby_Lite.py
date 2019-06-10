#버그 수정필요 // 그래프 띄울시 백그라운드로 pyqt위젯이 하나 더 생김
#             // 버튼 클릭시 화면 전환기능 구현해야함

import sys
import random
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg
import threading
import time

class MyWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.x = [0, 1, 2, 3, 4, 5, 6, 7 ,8 ,9]
        self.y = [0, 34, 21, 40, 45, 50, 30, 20 ,25 ,10]
        self.SpeedPlot = pg.plot(self.x, self.y)
        self.SpeedPlot.setXRange(1, 10)
        self.SpeedPlot.setYRange(1, 60)
        self.setupUI()

    def setupUI(self):
        #self.setGeometry(0, 0, 320, 240)
        #스피드
        self.SpeedLabel = QLabel("Speed\n10Km/h")
        self.SpeedLabel.setStyleSheet("color:rgb(255,255,255); font-size:40px; font:bold")
        self.SpeedLabel.setAlignment(Qt.AlignCenter)
        self.SpeedLayOut = QVBoxLayout()
        self.SpeedLayOut.addWidget(self.SpeedLabel)
        self.SpeedLayOut.addWidget(self.SpeedPlot)

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

        self.Verbtn1 = QPushButton("변경하기")
        self.Verbtn1.setStyleSheet("color:rgb(255,255,255); font-size:20px; font:bold")

        self.VerLayOut = QHBoxLayout()
        self.VerLayOut.addWidget(self.Verbtn1)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SpeedLayOut)
        self.layout.addLayout(self.FourInnerLayOut)
        self.layout.addLayout(self.VerLayOut)
        self.setLayout(self.layout)

    #def update_plot(self):
    #    time.strftime("%S", time.localtime())
    #    self.plottimer(random.randint(1, 60))
    #    self.SpeedPlot.setXRange(1, len(self.x)+1)

    #def plottimer(self, randomint):
    #    self.y.append(randomint)
    #    print(self.y,len(self.y))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mywindow = MyWindow()
    mywindow.resize(240, 320)
    mywindow.setStyleSheet("background-color:rgb(0,0,0)")

    #def get_data():
    #    mywindow.update_plot()

    #mytimer = QTimer()
    #mytimer.start(1000)  # 1초마다 갱신 위함...
    #mytimer.timeout.connect(get_data)

    mywindow.show()

    app.exec_()
