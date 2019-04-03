import os
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 버튼 팝업 진행중

# 녹화 확인 스택위젯
class ChkRecordingClicked(QLabel):
    def __init__(self, forBack):
        super().__init__()
        self.formSetting(forBack)

    def recordTest(self, item):
        self.recordPlay = PlayRecording(item.text())

    def formSetting(self, forBack):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.list = QListWidget(self)
        fileNames = os.listdir("Movie/")

        for fileName in fileNames:
            self.list.addItem('%s' % fileName)

        self.list.itemClicked.connect(self.recordTest)
        self.list.setStyleSheet("color:white;font-size:20px;border:0px;QListWidget::item{border:1px solid red;};")
        self.list.setFixedWidth(760)
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

        self.layout.addWidget(self.list)
        self.layout.addWidget(self.quitLabel)


class PlayRecording():
    def __init__(self, fileName):
        super().__init__()
        self.formSetting(fileName)

    def formSetting(self, fileName):
        file = 'Movie/'+fileName
        cap = cv2.VideoCapture(file)

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                cv2.imshow('frame', frame)
                if cv2.waitKey(40) & 0xFF == ord('q'):
                    break
            else:
                break
        cap.release()
        #cv2.destroyAllWindows()


