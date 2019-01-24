import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class RunDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle("Ariby Run")

        self.pushButton1= QPushButton("run", self)
        
class AppDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle("Ariby App")

        self.pushButton1= QPushButton("App", self)

        
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(0, 0, 800, 480)
        self.setWindowTitle("Ariby")
        self.setWindowIcon(QIcon('icon.png'))
        
        self.label = QLabel("main", self)
        self.label.resize(150,30)
        self.label.move(20, 20)
        self.runButton = QPushButton("Run", self)
        self.runButton.clicked.connect(self.runButtonClicked)
        self.runButton.move(20,60)
        self.appButton = QPushButton("App", self)
        self.appButton.clicked.connect(self.appButtonClicked)
        self.appButton.move(20,80)
        self.exitButton = QPushButton("Exit", self)
        self.exitButton.clicked.connect(quit)
        self.exitButton.move(20,100)
        

    def runButtonClicked(self):
        dlg = RunDialog()
        dlg.exec_()

    def appButtonClicked(self):
        dlg = AppDialog()
        dlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
