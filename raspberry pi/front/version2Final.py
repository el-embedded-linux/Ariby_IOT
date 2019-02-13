# PyQt ProGramming Version 2
# 1.프로그레스바(쓰레드) 2.gif이미지 movie 위젯 적용 3.스택위젯으로 화면 재구성(+추후 추가 예정) 4.페이드인, 페이드아웃
# 5.날씨 아이콘 추가(크롤링 진행했었으나 블루투스 통신으로 이용할 지 상의 후 추가 예정) 6.라즈베리파이 마우스 커서 숨김

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime

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


#다이얼로그1
class Test1ClickedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def formSetting(self):
        self.resize(200, 200)
        self.setStyleSheet("background-color:rgb(41,41,41)")

        label = QLabel("Testing")
        label.setAlignment(Qt.AlignCenter)
        label.setStyleSheet("color:white; font-family:Arial")

        closeBtn = QPushButton("Exit")
        closeBtn.clicked.connect(self.closeDialog)
        closeBtn.setStyleSheet("font:bold 16px Arial; border:1px; border-radius:5px; background-color:rgb(106,230,197); color:rgb(41,41,41); padding:3px;")

        layout = QGridLayout()
        layout.addWidget(label,0, 0)
        layout.addWidget(closeBtn,1, 0)

        self.setLayout(layout)
        self.showFullScreen()

    def closeDialog(self):
        self.close()


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

        self.titleWidget = QLabel()
        self.titleWidget.setFixedHeight(60)
        self.titleWidget.setStyleSheet("padding-top:10px;")

        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.titleSet()

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addWidget(self.time, 1, 0)
        self.gridLayout.addWidget(self.weather, 1, 1)

        self.menuWidget = QLabel()
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.addWidget(self.aribyTitle)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.testAreaSet()

        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.titleWidget)
        mainLayout.addWidget(self.menuWidget)

    def timeout(self):
        strTime = datetime.today().strftime("%Y.%m.%d. %H:%M ")
        self.time.setText(self._translate("Main", strTime))

    def titleSet(self):
        self.font.setFamily("Arial")
        self.font.setPointSize(24)
        self.font.setWeight(50)

        self.setWindowTitle(self._translate("Main", "ARIBY"))

        self.aribyTitle = QLabel(self.titleWidget)
        self.aribyTitle.setFont(self.font)
        self.aribyTitle.setStyleSheet("color: rgb(106, 230, 197);")
        self.aribyTitle.setText(self._translate("Main", "  ARIBY"))

        self.font.setFamily("Bahnschrift Light")
        self.font.setPointSize(13)

        self.time = QLabel(self.titleWidget)
        self.time.setFont(self.font)
        self.time.setStyleSheet("color:white")
        self.time.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.time.setFixedWidth(180)

        self.weather = QLabel(self.titleWidget)
        pix = QPixmap('sunny.png')
        self.weather.setPixmap(pix)
        self.weather.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.weather.setFixedWidth(40)
        self.weather.setStyleSheet("padding-right:20px;")

    def testAreaSet(self):
        self.gridLayout2 = QGridLayout(self.menuWidget)

        self.menuLabel = []
        self.menuButton = []
        self.font.setPointSize(11)
        row = 0; col = 0

        for i in range(0, 6, 1):
            self.menuLabel.append(QLabel(self.menuWidget))
            self.menuButton.append(QPushButton("test"))
            self.menuLayout = QGridLayout()

            if i == 0:
                self.menuButton[i].setText("Bluetooth")
                self.menuButton[i].mousePressEvent = self.test1Clicked
            elif i == 1:
                self.menuButton[i].setText("Riding")
                self.menuButton[i].mousePressEvent = self.test2Clicked
            elif i == 2:
                self.menuButton[i].setText("Check Recoding")
                self.menuButton[i].mousePressEvent = self.test3Clicked
            elif i == 3:
                self.menuButton[i].setText("Settnigs")
                self.menuButton[i].mousePressEvent = self.test4Clicked
            elif i == 4:
                self.menuButton[i].setText("Help")
                self.menuButton[i].mousePressEvent = self.test5Clicked
            else :
                self.menuButton[i].setText("Exit")
                self.menuButton[i].mousePressEvent = self.test6Clicked

            self.menuLabel[i].setStyleSheet("margin:5px;")
            self.menuButton[i].setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding:15px 3px; outline:0px;")
            if (col == 3):
                row = 1; col = 0

            self.gridLayout2.addWidget(self.menuLabel[i], row, col)
            self.menuLabel[i].setLayout(self.menuLayout)
            self.menuLayout.addWidget(self.menuButton[i])
            col += 1

    #이벤트 설정
    def test1Clicked(self, event):
        lDig = Test1ClickedDialog()
        lDig.exec_()

    def test2Clicked(self, event):
        lDig = Test1ClickedDialog()
        lDig.exec_()

    def test3Clicked(self, event):
        lDig = Test1ClickedDialog()
        lDig.exec_()

    def test4Clicked(self, event):
        lDig = Test1ClickedDialog()
        lDig.exec_()

    def test5Clicked(self, event):
        lDig = Test1ClickedDialog()
        lDig.exec_()

    def test6Clicked(self, event):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QLabel()
    window.resize(800, 480)
    window.setStyleSheet("background-color:rgb(106,230,197)")

    stack = StackedWidget()
    layout = QVBoxLayout(window)

    gif = "start.gif"
    loading = Loading(gif)
    main = Main()

    stack.addWidget(loading)
    stack.addWidget(main)

    layout.addWidget(stack)
    layout.setContentsMargins(0, 0, 0, 0)

    window.showFullScreen()

    sys.exit(app.exec_())
