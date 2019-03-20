import os
import cv2
import Header
from PyQt5.QtWidgets import *


class ChkRecordingDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.formSetting()

    def recordTest(self, item):
        self.recordPlay = PlayRecording(item.text())

    def formSetting(self):
        self.resize(800, 480)
        self.setStyleSheet("background-color:rgb(41,41,41)")

        self.headerTest = Header.Header()

        self.list = QListWidget(self)
        fileNames = os.listdir("Movie/")

        for fileName in fileNames:
            self.list.addItem('%s' % fileName)

        self.list.itemClicked.connect(self.recordTest)
        self.list.setStyleSheet("color:white;font-size:20px;border:0px;")
        self.headerTest.setGeometry(0,0,800,60)
        self.list.setGeometry(0,80,800,420)

        self.show()


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


