import sys

from PySide6.QtWidgets import QMainWindow, QStackedWidget, QApplication
# from PySide6.QtCore import *
from PySide6.QtGui import QGuiApplication

from components.main import MainPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1200, 800)
        self.center()
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

    def center(self):
        # 获取当前屏幕的尺寸和位置
        screen = QGuiApplication.screens()[0].availableGeometry()
        # 获取窗口的尺寸和位置
        size = self.geometry()
        # 计算窗口居中的位置
        print(screen.width())
        print(screen.height())
        print(size.width())
        print(size.height())
        x = (screen.width() - size.width()) / 2
        y = (screen.height() - size.height()) / 2
        # 移动窗口到居中位置
        self.move(x, y)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

