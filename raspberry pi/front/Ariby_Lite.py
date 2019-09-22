import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import FrontCam
#import pyqtgraph as pg

class Widget_1(QLabel):
    def __init__(self):
        super(Widget_1, self).__init__()
        # 스피드
        self.SpeedLabel = QLabel(" "+" 88") #100보다 작은 숫자일 땐 앞에 띄어쓰기 2칸 넣어야함, 큰 숫자일 땐 상관없음
        self.SpeedLabel.setStyleSheet("color:rgb(255,255,255); font-size:60px; font:bold")
        self.kmLabel = QLabel("\n\nKm/h")
        self.kmLabel.setFixedWidth(65)
        self.kmLabel.setStyleSheet("color:rgb(255,255,255); font-size:14px; font:bold")
        self.SpeedLayOut = QHBoxLayout()
        self.SpeedLayOut.addWidget(self.SpeedLabel)
        self.SpeedLayOut.addWidget(self.kmLabel)

        # 4칸(그리드레이아웃)
        self.FourInnerLayOut = QGridLayout()
        row = 0; col = 0;

        for i in range(0, 4, 1):
            if i == 0:
                text1 = "평균속도"
                value = " 10"
                text2 = "\nkm/h"
            elif i == 1:
                text1 = "이동거리"
                value = "110"
                text2 = "\nkm/h"
            elif i == 2:
                text1 = "심박수"
                value = " 80"
                text2 = "\nbpm"
            elif i == 3:
                text1 = "칼로리"
                value = "200"
                text2 = "\nKcal"

            self.avgSpeedLayout = QVBoxLayout()
            self.avgSpeedLayout.setContentsMargins(0,0,0,0)
            self.innerLayout = QHBoxLayout()
            self.innerLayout.setContentsMargins(0,0,0,0)
            self.outerLabel = QLabel()
            self.outerLabel.setLayout(self.avgSpeedLayout)
            self.textLabel1 = QLabel(text1)
            self.textLabel1.setAlignment(Qt.AlignCenter)
            self.textLabel1.setStyleSheet("color:white;font:bold;font-size:12px;")
            self.textLabel2 = QLabel()
            self.textLabel2.setLayout(self.innerLayout)
            self.avgSpeed = QLabel(value)
            self.avgSpeed.setStyleSheet("color:white;font:bold;font-size:26px;")
            self.km = QLabel(text2)
            self.km.setStyleSheet("color:white;font:bold;font-size:11px;")
            self.innerLayout.addWidget(self.avgSpeed)
            self.innerLayout.addWidget(self.km)
            self.avgSpeedLayout.addWidget(self.textLabel1)
            self.avgSpeedLayout.addWidget(self.textLabel2)

            if (col == 2):
                row = 1; col = 0

            self.FourInnerLayOut.addWidget(self.outerLabel, row, col)

            col += 1

        self.layout = QVBoxLayout()
        self.layout.addLayout(self.SpeedLayOut)
        self.layout.addLayout(self.FourInnerLayOut)
        self.setLayout(self.layout)


class Widget_2(QLabel):
    isRecording = False
    def __init__(self):
        super(Widget_2, self).__init__()
        ###그래프  #그래프 임시 제거
        """
        self.x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.y = [0, 34, 21, 40, 45, 30, 20, 25, 10]
        self.graphWd = pg.GraphicsWindow()
        self.graphWd.ci.layout.setContentsMargins(0,0,0,0)
        self.gp = self.graphWd.addPlot()
        self.gp.plot(self.x, self.y)

        self.gpLabel = QLabel()
        self.graphLayout = QVBoxLayout()
        self.graphLayout.setContentsMargins(0,0,0,0)
        self.graphLayout.addWidget(self.graphWd)
        self.gpLabel.setLayout(self.graphLayout)
        self.gpLabel.setFixedHeight(137)
        self.gpLabel.setFixedWidth(200)
        """

        self.camButton = QPushButton("녹화시작")
        self.camButton.setStyleSheet("color:white;font:bold;font-size:26px;background-color: rgba(0,0,0,0.4); border-style: outset; border-width: 2px; border-color: white;")
        self.camButton.setFixedHeight(137)
        self.camButton.setFixedWidth(218)
        self.camButton.clicked.connect(self.camButtonClicked)


        self.FourInnerLayOut = QGridLayout()
        row = 0; col = 0;
        for i in range(0, 4, 1): #띄어쓰기 없애지 말기...
            if i == 0:
                text1 = "최고속도"
                value = " "+"35" #값이 100 미만일 경우 / 100 이상 시 " " 제거 필요
                text2 = "\nkm/h"
                flag = 0
            elif i == 1:
                text1 = "주행시간"
                value = " "+"08:58"
                text2 = ""
                flag =1
            elif i == 2:
                text1 = "경사도"
                value = "  "+"0º"
                text2 = ""
                flag = 1
            elif i == 3:
                text1 = "온도"
                value = "  "+"25℃"
                text2 = ""
                flag = 1

            self.avgSpeedLayout = QVBoxLayout()
            self.avgSpeedLayout.setContentsMargins(0,0,0,0)
            self.innerLayout = QHBoxLayout()
            self.innerLayout.setContentsMargins(0,0,0,0)
            self.outerLabel = QLabel()
            self.outerLabel.setLayout(self.avgSpeedLayout)
            self.textLabel1 = QLabel(text1)
            self.textLabel1.setAlignment(Qt.AlignCenter)
            self.textLabel1.setStyleSheet("color:white;font:bold;font-size:12px;")
            self.textLabel2 = QLabel()
            self.textLabel2.setLayout(self.innerLayout)
            self.avgSpeed = QLabel(value)
            self.avgSpeed.setStyleSheet("color:white;font:bold;font-size:26px;")
            self.km = QLabel(text2)
            self.km.setStyleSheet("color:white;font:bold;font-size:11px;")
            self.innerLayout.addWidget(self.avgSpeed)
            if flag == 1:
                self.innerLayout.setAlignment(Qt.AlignCenter)
            self.innerLayout.addWidget(self.km)
            self.avgSpeedLayout.addWidget(self.textLabel1)
            self.avgSpeedLayout.addWidget(self.textLabel2)

            if (col == 2):
                row = 1; col = 0

            self.FourInnerLayOut.addWidget(self.outerLabel, row, col)

            col += 1

        self.FourLabel = QLabel()
        self.FourLabel.setLayout(self.FourInnerLayOut)

        self.layout2 = QVBoxLayout()
        self.layout2.setContentsMargins(0,0,0,0)
        #self.layout2.addWidget(self.gpLabel) #그래프 임시 제거
        self.layout2.addWidget(self.camButton)
        self.layout2.addWidget(self.FourLabel)
        self.setLayout(self.layout2)

    def camButtonClicked(self):
        if self.isRecording==False:
            self.frontCamObject=FrontCam.FrontCam()
            self.camButton.setText("녹화중")
            self.camButton.setStyleSheet("color:red;font:bold;font-size:26px;background-color: rgba(0,0,0,0.4); border-style: outset; border-width: 2px; border-color: white;")
            self.isRecording=True
        else:
            self.frontCamObject.stop()
            self.camButton.setText("녹화시작")
            self.camButton.setStyleSheet("color:white;font:bold;font-size:26px;background-color: rgba(0,0,0,0.4); border-style: outset; border-width: 2px; border-color: white;")
            self.isRecording=False




class Widget_3(QLabel):
    def __init__(self):
        super(Widget_3, self).__init__()
        self.textLabel = QLabel("주행 중입니다.")
        self.textLabel.setStyleSheet("font:bold;font-size:12px;color:white;")
        self.textLabel.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        self.textLabel.setFixedHeight(30)
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        img = QPixmap('Images/user0.png')
        self.label.setPixmap(img)
        self.label.setFixedHeight(250)
        self.backLabel = QLabel()

        self.layout3 = QVBoxLayout()
        self.layout3.setContentsMargins(0,0,0,0)
        self.layout3.addWidget(self.textLabel)
        self.layout3.addWidget(self.label)
        self.setLayout(self.layout3)

    def backWarning(self, data): #콜백 등록 필요
        self.textLabel.setText("후방에 주의하세요.")
        self.label.setPixmap(QPixmap('Images/user'+str(data)+'.png'))


class Form(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.stk_w = QStackedWidget(self)
        self.init_widget()
        self.checkIndex = 0

    def init_widget(self):
        self.setWindowTitle("Ariby Lite")
        widget_laytout = QBoxLayout(QBoxLayout.LeftToRight)

        self.stk_w.addWidget(Widget_1())
        self.stk_w.addWidget(Widget_2())
        self.stk_w.addWidget(Widget_3())

        widget_laytout.addWidget(self.stk_w)
        self.setLayout(widget_laytout)

    def mousePressEvent(self, e):
        if self.checkIndex == 1:
            self.stk_w.setCurrentIndex(2)
            self.checkIndex = 2
        elif self.checkIndex == 0:
            self.stk_w.setCurrentIndex(1)
            self.checkIndex = 1
        elif self.checkIndex == 2:
            self.stk_w.setCurrentIndex(0)
            self.checkIndex = 0


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.resize(240, 320)
    mywindow.setStyleSheet("background-color:rgb(0,0,0)")
    #mywindow.show()
    mywindow.showFullScreen()
    app.exec_()
