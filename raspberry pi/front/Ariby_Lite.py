'''
1. 버그 수정필요 // 그래프 띄울시 백그라운드로 pyqt위젯이 하나 더 생김
2. Q스택위젯, 마우스클릭이벤트로 인덱스 번호 찾기
3. pyqtgraph 백그라운드 표출되는 버그 수정바람
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pyqtgraph as pg

class StWidgetForm(QGroupBox):
    """
    위젯 베이스 클래스
    """
    def __init__(self):
        QGroupBox.__init__(self)
        self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.y = [0, 34, 21, 40, 45, 50, 30, 20, 25, 10]
        self.SpeedPlot = pg.plot(self.x, self.y)
        self.SpeedPlot.setXRange(1, 10)
        self.SpeedPlot.setYRange(1, 60)

class Widget_1(StWidgetForm):
    """
    버튼 그룹
    """
    def __init__(self):
        super(Widget_1, self).__init__()
        # self.setGeometry(0, 0, 320, 240)
        # 스피드
        self.SpeedLabel = QLabel("Speed\n10Km/h")
        self.SpeedLabel.setStyleSheet("color:rgb(255,255,255); font-size:40px; font:bold")
        self.SpeedLabel.setAlignment(Qt.AlignCenter)
        self.SpeedLayOut = QVBoxLayout()
        self.SpeedLayOut.addWidget(self.SpeedLabel)

        # 4칸(그리드레이아웃)
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

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SpeedLayOut)
        self.layout.addLayout(self.FourInnerLayOut)
        self.setLayout(self.layout)

class Widget_2(StWidgetForm):
    def __init__(self):
        super(Widget_2, self).__init__()
        # 스피드
        self.SpeedLabel = QLabel("Speed\n10Km/h")
        self.SpeedLabel.setStyleSheet("color:rgb(255,255,255); font-size:35px; font:bold")
        self.SpeedLabel.setAlignment(Qt.AlignCenter)
        self.SpeedLayOut = QVBoxLayout()
        self.SpeedLayOut.addWidget(self.SpeedPlot)
        self.SpeedLayOut.addWidget(self.SpeedLabel)

        # 그리드레이아웃
        self.MaxLabel = QLabel("MaxLabel\n80 km/h")
        self.MaxLabel.setStyleSheet("color:rgb(255,255,255); font-size:18px; font:bold")
        self.MaxLabel.setAlignment(Qt.AlignCenter)
        self.AvgLabel = QLabel("AvgLabel\n55 km/h")
        self.AvgLabel.setStyleSheet("color:rgb(255,255,255); font-size:18px; font:bold")
        self.AvgLabel.setAlignment(Qt.AlignCenter)

        self.FourInnerLayOut = QGridLayout()
        self.FourInnerLayOut.addWidget(self.MaxLabel, 0, 0)
        self.FourInnerLayOut.addWidget(self.AvgLabel, 0, 1)

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SpeedLayOut)
        self.layout.addLayout(self.FourInnerLayOut)
        self.setLayout(self.layout)

class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.init_widget()
        self.checkIndex = True

    def init_widget(self):
        self.setWindowTitle("Ariby Lite")
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        self.stk_w.addWidget(Widget_1())
        self.stk_w.addWidget(Widget_2())

        widget_laytout.addWidget(self.stk_w)
        self.setLayout(widget_laytout)

    def mousePressEvent(self, e):
        if self.checkIndex == False:
            self.stk_w.setCurrentIndex(0)
            self.checkIndex = True
        elif self.checkIndex == True:
            self.stk_w.setCurrentIndex(1)
            self.checkIndex = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.resize(240, 320)
    mywindow.setStyleSheet("background-color:rgb(0,0,0)")
    mywindow.show()
    app.exec_()
