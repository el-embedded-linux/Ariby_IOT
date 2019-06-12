import platform
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 녹화 확인 스택위젯
class SettingsClicked(QLabel):
    def __init__(self, forBack, window):
        super().__init__()
        self.window = window
        self.formSetting(forBack)

    def formSetting(self, forBack):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.layout.setContentsMargins(0,0,0,0)

        self.file = open(r'/home/pi/EL_IOT/raspberry pi/front/setting.txt', 'r')
        line = self.file.readlines()
        self.file.close()

        self.timeSetup = line[0][0:2]
        self.fontSize =line[1][0:2]
        self.fontSize2 = line[2][0:1]
        self.thema = line[3][0:1]
        print(self.thema+"1")

        self.setLayout(self.layout)

        self.selectLabel = QLabel()
        self.selectLabel.setFixedHeight(50)

        self.displayBtn = QPushButton("DISPLAY")
        self.displayBtn.setFixedWidth(130)
        self.displayBtn.setFixedHeight(25)
        self.displayBtn.setStyleSheet("margin-left:30px;font:bold "+self.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.displayBtn.clicked.connect(self.dis)

        if (self.fontSize2) == 'S':
            self.setFontSet = ' 12px '
        elif (self.fontSize2) =='M':
            self.setFontSet = ' 13px '
        else :
            self.setFontSet = ' 14px '

        #self.ridingBtn = QPushButton("RIDING")
        #self.ridingBtn.setFixedWidth(105)
        #self.ridingBtn.setFixedHeight(25)
        #self.ridingBtn.setStyleSheet("font:bold "+self.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        #self.ridingBtn.clicked.connect(self.rid)

        self.selectLayout = QHBoxLayout()
        self.selectLayout.setContentsMargins(0, 0, 0, 0)
        self.selectLayout.setAlignment(Qt.AlignVCenter)
        self.selectLayout.addWidget(self.displayBtn)
        #self.selectLayout.addWidget(self.ridingBtn)

        self.selectLabel.setLayout(self.selectLayout)

        self.setStack = QStackedWidget()
        self.setStack.setLayout(QVBoxLayout())

        self.displayAllLayout = QVBoxLayout()
        self.displayAllLayout.setContentsMargins(0,0,0,0)

        self.displayWidget = QLabel()
        self.displayWidget.setLayout(self.displayAllLayout)
        self.displayWidget.setFixedWidth(800)
        self.displayWidget.setFixedHeight(250)

        self.timeLayout = QHBoxLayout()
        self.timeLayout.setContentsMargins(0,0,0,0)
        self.timeLabel = QLabel()
        self.timeLabel.setFixedWidth(590)
        self.timeLabel.setFixedHeight(30)
        self.timeLabel.setLayout(self.timeLayout)
        self.timeText = QLabel("Time Setup : " + self.timeSetup +"H")
        self.timeText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:208px;")
        self.timeRadio12 = QRadioButton("12H")
        self.timeRadio12.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:76px;")
        self.timeRadio24 = QRadioButton("24H")
        self.timeRadio24.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:70px")
        if (self.timeSetup == '12'):
            self.timeRadio12.setChecked(True)
        else:
            self.timeRadio24.setChecked(True)
        self.timeLayout.addWidget(self.timeText)
        self.timeLayout.addWidget(self.timeRadio12)
        self.timeLayout.addWidget(self.timeRadio24)

        self.fontLayout = QHBoxLayout()
        self.fontLayout.setContentsMargins(0, 0, 0, 0)
        self.fontLabel = QLabel()
        self.fontLabel.setFixedWidth(590)
        self.fontLabel.setFixedHeight(30)
        self.fontLabel.setLayout(self.fontLayout)
        self.fontText = QLabel("Button Font Size : " + self.fontSize)
        self.fontText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
        self.fontCb = QComboBox()
        self.fontCb.setFixedWidth(80)
        self.fontCb.addItems(['14','15','16','17','18','19','20'])
        self.fontCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
        self.fontLayout.addWidget(self.fontText)
        self.fontLayout.addWidget(self.fontCb)

        self.fontLayout2 = QHBoxLayout()
        self.fontLayout2.setContentsMargins(0,0,0,0)
        self.fontLabel2 = QLabel()
        self.fontLabel2.setFixedWidth(590)
        self.fontLabel2.setFixedHeight(30)
        self.fontLabel2.setLayout(self.fontLayout2)
        if (self.fontSize2 == 'S') :
            self.fontSize2Set = '작게'
        elif (self.fontSize2 == 'M') :
            self.fontSize2Set = '중간'
        else :
            self.fontSize2Set = '크게'
        self.fontText2 = QLabel("Font Size : " + self.fontSize2Set)
        self.fontText2.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
        self.fontRadioS = QRadioButton("작게")
        self.fontRadioS.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px;")
        self.fontRadioM = QRadioButton("중간")
        self.fontRadioM.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px")
        self.fontRadioL = QRadioButton("크게")
        self.fontRadioL.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:28px")
        if (self.fontSize2 == 'S'):
            self.fontRadioS.setChecked(True)
        elif (self.fontSize2 == 'M'):
            self.fontRadioM.setChecked(True)
        else:
            self.fontRadioL.setChecked(True)
        self.fontLayout2.addWidget(self.fontText2)
        self.fontLayout2.addWidget(self.fontRadioS)
        self.fontLayout2.addWidget(self.fontRadioM)
        self.fontLayout2.addWidget(self.fontRadioL)

        self.themaLayout = QHBoxLayout()
        self.themaLayout.setContentsMargins(0, 0, 0, 0)
        self.themaLabel = QLabel()
        self.themaLabel.setFixedWidth(590)
        self.themaLabel.setFixedHeight(30)
        self.themaLabel.setLayout(self.themaLayout)
        if (self.thema == 'D'):
            self.themaTextSet = '기본'
        else :
            self.themaTextSet = '하얀색'
        self.themaText = QLabel("Thema : " + self.themaTextSet)
        self.themaText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
        self.themaCb = QComboBox()
        self.themaCb.setFixedWidth(80)
        self.themaCb.addItems(['기본', '하얀색'])
        self.themaCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
        self.themaLayout.addWidget(self.themaText)
        self.themaLayout.addWidget(self.themaCb)

        self.displayAllLayout.addWidget(self.timeLabel)
        self.displayAllLayout.addWidget(self.fontLabel)
        self.displayAllLayout.addWidget(self.fontLabel2)
        self.displayAllLayout.addWidget(self.themaLabel)

        #self.ridingAllLayout = QVBoxLayout()
        #self.ridingAllLayout.setContentsMargins(0,0,0,0)

        #self.ridingWidget = QLabel()
        #self.ridingWidget.setLayout(self.ridingAllLayout)
        #self.ridingWidget.setFixedWidth(800)
        #self.ridingWidget.setFixedHeight(335)

        self.setStack.addWidget(self.displayWidget)
        #self.setStack.addWidget(self.ridingWidget)

        self.quitLabel = QLabel()
        self.quitLabel.setFixedHeight(50)
        self.quitLabel.setFixedWidth(780)

        self.saveBtn = QPushButton("Save")
        self.saveBtn.setFixedHeight(30)
        self.saveBtn.setFixedWidth(70)
        self.saveBtn.setStyleSheet("font:bold "+self.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.saveBtn.clicked.connect(self.save)

        self.quitBtn = QPushButton("Quit")
        self.quitBtn.setFixedHeight(30)
        self.quitBtn.setFixedWidth(70)
        self.quitBtn.setStyleSheet("font:bold "+self.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.quitBtn.clicked.connect(forBack.changeStack)

        self.quitLayout = QHBoxLayout()
        self.quitLayout.setContentsMargins(0,0,0,0)
        self.quitLayout.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.quitLayout.addWidget(self.saveBtn)
        self.quitLayout.addWidget(self.quitBtn)

        self.quitLabel.setLayout(self.quitLayout)

        self.layout.addWidget(self.selectLabel)
        self.layout.addWidget(self.setStack)
        self.layout.addWidget(self.quitLabel)

        if (self.thema == 'D'):
            self.setStyleSheet("background-color:rgb(41,41,41);")
            self.timeText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:208px;")
            self.timeRadio12.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:76px;")
            self.timeRadio24.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:70px")
            self.fontText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.fontCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.fontText2.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.fontRadioS.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px;")
            self.fontRadioM.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px")
            self.fontRadioL.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:28px")
            self.themaText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.themaCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
        else :
            self.setStyleSheet("background-color:white;")
            self.timeText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:208px;")
            self.timeRadio12.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:76px;")
            self.timeRadio24.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:70px")
            self.fontText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.fontCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.fontText2.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.fontRadioS.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:32px;")
            self.fontRadioM.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:32px")
            self.fontRadioL.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:28px")
            self.themaText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.themaCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")

    def dis(self):
        self.setStack.setCurrentIndex(0)

    #def rid(self):
    #    self.setStack.setCurrentIndex(1)

    def btnSizeSet(self, main, chkClicked):
        if (self.fontSize2=='S'):
            for i in range(0, 4, 1):
                main.menuButton[i].setStyleSheet("font:bold 20px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
            chkClicked.list.setStyleSheet("color:white;font-size:18px;border:0px;QListWidget::item{border:1px solid red;};")
        elif (self.fontSize2=='M'):
            for i in range(0, 4, 1):
                main.menuButton[i].setStyleSheet("font:bold 23px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
            chkClicked.list.setStyleSheet("color:white;font-size:20px;border:0px;QListWidget::item{border:1px solid red;};")
        else :
            for i in range(0, 4, 1):
                main.menuButton[i].setStyleSheet("font:bold 25px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
            chkClicked.list.setStyleSheet("color:white;font-size:22px;border:0px;QListWidget::item{border:1px solid red;};")

        chkClicked.quitBtn.setStyleSheet("font:bold " + self.fontSize + "px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")

    def btnSizeSet1(self, main, chkClicked, bleClicked):
        if (self.thema == 'D'):
            bleClicked.setStyleSheet("background-color:rgb(41,41,41)")
            if (self.fontSize2=='S'):
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 20px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:white;font-size:18px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:white;font:bold 12px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:white;font:bold 12px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:white;font:bold 12px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 12px Arial; color:rgb(255,255,255);margin-left:20px;")

            elif (self.fontSize2=='M'):
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 23px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:white;font-size:20px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:white;font:bold 14px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:white;font:bold 14px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:white;font:bold 14px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 14px Arial; color:rgb(255,255,255);margin-left:20px;")

            else :
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 25px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:white;font-size:22px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:white;font:bold 16px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:white;font:bold 16px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:white;font:bold 16px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 16px Arial; color:rgb(255,255,255);margin-left:20px;")

        else :
            bleClicked.setStyleSheet("background-color:white")
            if (self.fontSize2=='S'):
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 20px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:rgb(41,41,41);font-size:18px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:rgb(41,41,41);font:bold 12px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 12px Arial; color:rgb(41,41,41);margin-left:20px;")

            elif (self.fontSize2=='M'):
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 23px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:rgb(41,41,41);font-size:20px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:rgb(41,41,41);font:bold 14px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 14px Arial; color:rgb(41,41,41);margin-left:20px;")

            else :
                for i in range(0, 4, 1):
                    main.menuButton[i].setStyleSheet("font:bold 25px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); padding-top:30px; padding-bottom:30px; outline:0px;")
                chkClicked.list.setStyleSheet("color:rgb(41,41,41);font-size:22px;border:0px;QListWidget::item{border:1px solid red;};")
                bleClicked.groupBoxOption.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;margin-left:20px;")
                bleClicked.groupBoxConn.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;margin-left:20px;")
                bleClicked.list.setStyleSheet("color:rgb(41,41,41);font:bold 16px Arial;border:0px;QListWidget::item{border:1px solid red;};margin-left:20px;")
                bleClicked.statusLabel.setStyleSheet("font:bold 16px Arial; color:rgb(41,41,41);margin-left:20px;")

        chkClicked.quitBtn.setStyleSheet("font:bold " + self.fontSize + "px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        bleClicked.ConnBtn.setStyleSheet("font:bold "+self.fontSize+"px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        bleClicked.quitBtn.setStyleSheet("font:bold " + self.fontSize + "px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")

    def funcSet(self, main, chk):
        self.main = main
        self.chk = chk

    def funcSet1(self, main, chk, ble):
        self.main = main
        self.chk = chk
        self.ble = ble

    def getHeader(self, header):
        self.header = header

    def save(self):
        if (self.timeRadio12.isChecked()):
            self.timeSetup = '12'
        else :
            self.timeSetup = '24'
        self.timeText.setText("Time Setup : " + self.timeSetup +"H")

        self.fontSize = self.fontCb.currentText()
        self.fontText.setText("Button Font Size : " + self.fontSize)

        if (self.fontRadioS.isChecked()):
            self.fontSize2 = 'S'
            self.fontText2Set = '작게'
            self.setFontSet = ' 12px '

        elif (self.fontRadioM.isChecked()):
            self.fontSize2 = 'M'
            self.fontText2Set = '중간'
            self.setFontSet = ' 13px '

        else :
            self.fontSize2 = 'L'
            self.fontText2Set = '크게'
            self.setFontSet = ' 14px '

        self.fontText2.setText("Font size : " + self.fontText2Set)

        self.themaItem = self.themaCb.currentText()
        if (self.themaItem == '기본') :
            self.thema = 'D'
            self.themaTextSet = '기본'
            self.window.setStyleSheet("background-color:rgb(41,41,41)")
            self.setStyleSheet("background-color:rgb(41,41,41)")
            self.header.time.setStyleSheet("color:white")
            self.timeText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:208px;")
            self.timeRadio12.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:76px;")
            self.timeRadio24.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:70px")
            self.fontText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.fontCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.fontText2.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.fontRadioS.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px;")
            self.fontRadioM.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:32px")
            self.fontRadioL.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:28px")
            self.themaText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:white; margin-left:210px;")
            self.themaCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.chk.setStyleSheet("background-color:rgb(41,41,41)")

        else :
            self.thema = 'W'
            self.themaTextSet = '하얀색'
            self.window.setStyleSheet("background-color:white")
            self.setStyleSheet("background-color:white")
            self.header.time.setStyleSheet("color:rgb(41,41,41)")
            self.timeText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:208px;")
            self.timeRadio12.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:76px;")
            self.timeRadio24.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:70px")
            self.fontText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.fontCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.fontText2.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.fontRadioS.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:32px;")
            self.fontRadioM.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:32px")
            self.fontRadioL.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:28px")
            self.themaText.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); margin-left:210px;")
            self.themaCb.setStyleSheet("font:bold"+self.setFontSet+"Arial; color:rgb(41,41,41); background-color:white;")
            self.chk.setStyleSheet("background-color:white")

        self.themaText.setText("Thema : " + self.themaTextSet)

        self.saveBtn.setStyleSheet("font:bold " + self.fontSize + "px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")
        self.quitBtn.setStyleSheet("font:bold " + self.fontSize + "px Arial; color:rgb(41,41,41); border:0px; border-radius:5px; background-color:rgb(106,230,197); outline:0px;")

        if platform.system() == 'Linux':
            self.btnSizeSet1(self.main, self.chk, self.ble)
        else :
            self.btnSizeSet(self.main, self.chk)

        self.file = open(r'/home/pi/EL_IOT/raspberry pi/front/setting.txt','w')
        self.file.writelines(self.timeSetup+'\n'+self.fontSize+'\n'+self.fontSize2+'\n'+self.thema)
        self.file.close()
