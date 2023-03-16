import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from components.main import MainPage
from ui.ui_main import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):

        # 创建QWidget对象
        self.widget = QStackedWidget()

        # 创建主页
        self.mainPage = MainPage()

        self.mainPage.setParent(self)

        # # 将窗口添加到QWidget
        self.widget.addWidget(self.mainPage)

        # 将QStackedWidget添加到窗口中
        self.setCentralWidget(self.widget)
        
        
        # def startClicked(self): # 点击“start”按钮  信号与槽函数
        #     print("你点击了start按钮")


        # self.startButton.clicked.connect(MainWindow.startClicked)
        # self.stopButton.clicked.connect(MainWindow.stopClicked)
        # self.setAreaButton.clicked.connect(MainWindow.setAreaClicked)
        # self.setLinesButton.clicked.connect(MainWindow.setLinesClicked)
        # self.loadVideoButton.clicked.connect(MainWindow.loadVideoClicked)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(1200, 800)
    window.move(0, 0)
    window.show()
    sys.exit(app.exec())
