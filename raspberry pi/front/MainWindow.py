# PyQt ProGramming Version 3
# 1.일부 다이얼로그 라벨로 수정    2.헤더모듈화 완료    3.변수명 및 파일명 재명명    4.코드 병합, 정리
# 5.메인으로 back 구현 완료    6.주행 중 터치 시 버튼 팝업&영상처리 진행중


import sys
#import TurnSignal   #라파
import BackCam
#import FrontCam   #라파
import Header
#import BleClicked   #라파
import RidingClicked
import ChkRecordingClicked
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


#프로그레스바 설정
DEFAULTSTYLE = """
QProgressBar{
    border:0px;
    text-align:center;
    background-color:rgb(106, 230, 197);
    font-size:13px;
    padding: 1px 2px;
    margin: 0px 50%;
}

QProgressBar::chunk{
    background-color:rgb(255,255,255);
    border:0px;
    border-radius:5px;
    margin-right:30px;
    width:10px;
}
"""

#프로그레스바 쓰레드
class Thread(QThread):
    value = pyqtSignal(int)

    def __init__(self):
        QThread.__init__(self)
        self.mutex = QMutex()
        self.count = 0
        self._status = True
        self.pixmapOpacity = 1.0

    def run(self):
        while True:
            self.mutex.lock()
            if 100 == self.count:
                self.msleep(1000)
                loading.startButton.setVisible(True)
                loading.startButton.setStyleSheet("outline:0px;border:0px;color:white;padding:5px 10px 10px 10px;font-size:20px;font-family:Arial;")
                loading.progressBar.setVisible(False)
                self.mutex.unlock()
                break
            self.count += 1
            self.value.emit(self.count)
            self.msleep(10)
            self.mutex.unlock()


#스택위젯 클래스 생성
class StackedWidget(QStackedWidget):
    index = 0
    def __init__(self, parent=None):
        QStackedWidget.__init__(self, parent)

    def setCurrentIndex(self, index):
        self.fade = FadeWidget(self.currentWidget(), self.widget(index))
        QStackedWidget.setCurrentIndex(self, index)

    def setPage(self):
        if self.index == 0 :
            self.setCurrentIndex(1)
            self.index = 1
            window.setStyleSheet("background-color:rgb(41,41,41)")
            loading.th.terminate()


#페이드인, 아웃용
class FadeWidget(QWidget):
    def __init__(self, oldWidget, newWidget):
        QWidget.__init__(self, newWidget)

        self.oldPixmap = QPixmap(newWidget.size())
        oldWidget.render(self.oldPixmap)
        self.pixmapOpacity = 1.0

        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(333)
        self.timeline.start()

        self.resize(newWidget.size())
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmapOpacity)
        painter.drawPixmap(0, 0, self.oldPixmap)
        painter.end()

    def animate(self, value):
        self.pixmapOpacity = 1.0 - value
        self.repaint()


#스택위젯 1 로딩화면
class Loading(QWidget):
    def __init__(self, file):
        QWidget.__init__(self, flags=Qt.Widget)
        self.movie = QMovie(file, QByteArray(), self)
        self.progressBar = QProgressBar()
        self.progressBar.setStyleSheet(DEFAULTSTYLE)
        self.progressBar.setTextVisible(False)
        self.progressBar.setFixedHeight(16)
        self.startButton = QPushButton("START")
        self.th = Thread()
        self.setUi()
        self.th.start()

    def setUi(self):
        self.setWindowTitle("ARIBY")
        self.resize(800,480)
        self.th.value.connect(self.progressBar.setValue)

        self.movieScreen = QLabel()
        self.movieScreen.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.movieScreen.setAlignment(Qt.AlignCenter)
        self.movieScreen.setFixedHeight(250)

        self.startButton.clicked.connect(stack.setPage)
        self.startButton.setVisible(False)
        self.startButton.setStyleSheet("outline:0px;border:0px;color:rgb(106, 230, 197);padding:5px 10px 10px 10px; font-family:Arial;font-size:16px;font-weight:bold;")

        self.mainLayout = QVBoxLayout()
        self.mainLayout.addWidget(self.movieScreen)
        self.mainLayout.addWidget(self.progressBar)
        self.mainLayout.addWidget(self.startButton)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.mainLayout)

        self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(90)
        self.movieScreen.setMovie(self.movie)
        self.movie.start()


#스택위젯2 메인화면
class Main(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setUi()

    def setUi(self):
        self.font = QFont()
        self._translate = QCoreApplication.translate
        mainLayout = QVBoxLayout()
        self.setLayout(mainLayout)

        self.header = Header.Header()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.header.timeout)

        self.menuStack = QStackedWidget()

        self.menuWidget = QLabel()
        self.menuAreaSet()
        self.chkWidget = ChkRecordingClicked.ChkRecordingClicked(self)
        #self.blueWidget = BleClicked.BleClicked(self)   #라파

        self.menuStack.addWidget(self.menuWidget)
        self.menuStack.addWidget(self.chkWidget)
        #self.menuStack.addWidget(self.blueWidget)   #라파

        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.header.titleWidget)
        mainLayout.addWidget(self.menuStack)


    def menuAreaSet(self):
        self.gridLayout2 = QGridLayout(self.menuWidget)

        self.menuLabel = []
        self.menuButton = []
        self.font.setPointSize(11)
        row = 0; col = 0

        for i in range(0, 4, 1):
            self.menuLabel.append(QLabel(self.menuWidget))
            self.menuButton.append(QPushButton())
            self.menuLayout = QGridLayout()

            if i == 0:
                self.menuButton[i].setText("Riding")
                self.menuButton[i].mousePressEvent = self.ride
            elif i == 1:
                self.menuButton[i].setText("Check Recoding")
                self.menuButton[i].mousePressEvent = self.chkRec
            elif i == 2:
                self.menuButton[i].setText("Bluetooth")
                self.menuButton[i].mousePressEvent = self.blueCon
            else:
                self.menuButton[i].setText("Test")
                self.menuButton[i].mousePressEvent = self.test

            self.menuLabel[i].setStyleSheet("margin:5px;")
            self.menuButton[i].setStyleSheet("font:bold 25px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
            if (col == 2):
                row = 1; col = 0

            self.gridLayout2.addWidget(self.menuLabel[i], row, col)
            self.menuLabel[i].setLayout(self.menuLayout)
            self.menuLayout.addWidget(self.menuButton[i])
            col += 1

    #이벤트 설정
    def ride(self, event):
        lDig = RidingClicked.RidingClicked()
        lDig.exec_()
        BackCam.backCamera.stop()
        #FrontCam.frontCamera.stop()   #라파
        print("stop")


    def chkRec(self, event):
        self.menuStack.setCurrentIndex(1)


    def blueCon(self, event):
        #pass
        self.menuStack.setCurrentIndex(2)   #라파


    def test(self, event):
        pass
        # self.menuStack.setCurrentIndex(3)

    def changeStack(self):
        self.menuStack.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QLabel()
    window.resize(800, 480)
    window.setStyleSheet("background-color:rgb(106,230,197)")

    stack = StackedWidget()
    layout = QVBoxLayout(window)

    gif = "Images/start.gif"
    loading = Loading(gif)
    main = Main()

    stack.addWidget(loading)
    stack.addWidget(main)

    layout.addWidget(stack)
    layout.setContentsMargins(0, 0, 0, 0)

    window.showFullScreen()

    sys.exit(app.exec_())
