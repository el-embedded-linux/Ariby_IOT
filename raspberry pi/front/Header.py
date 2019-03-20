from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from datetime import datetime


class Header(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setUi()

    def setUi(self):
        self.font = QFont()
        self._translate = QCoreApplication.translate
        self.titleWidget = QLabel()
        self.titleWidget.setFixedHeight(60)
        self.titleWidget.setStyleSheet("padding-top:10px;")

        self.horizontalLayout = QHBoxLayout(self.titleWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.titleSet()

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.addWidget(self.time, 1, 0)
        self.gridLayout.addWidget(self.weather, 1, 1)

        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.addWidget(self.aribyTitle)
        self.horizontalLayout.addLayout(self.gridLayout)

    def timeout(self):
        strTime = datetime.today().strftime("%Y.%m.%d. %H:%M ")
        self.time.setText(self._translate("Main", strTime))

    def titleSet(self):
        self.font.setFamily("Arial")
        self.font.setPointSize(24)
        self.font.setWeight(90)

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
        pix = QPixmap('Images/sunny.png')
        self.weather.setPixmap(pix)
        self.weather.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.weather.setFixedWidth(40)
        self.weather.setStyleSheet("padding-right:20px;")

