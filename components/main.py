import sys

from PySide6.QtWidgets import (QWidget, QHBoxLayout, QPushButton, QGridLayout, QLabel, QVBoxLayout, QSplitter,
                               QMainWindow, QApplication)
from PySide6.QtCore import Signal, QFile
from PySide6.QtGui import Qt, QPixmap

from ui.ui_main import Ui_MainWindow
from .subLineView import SubLineView
from components.subAreaView import SubAreaView

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def startClicked(self): # 点击“start”按钮  信号与槽函数
        print("你点击了start按钮")
    
    def stopClicked(self): # 点击“stop”按钮  信号与槽函数
        print("你点击了stop按钮")

    def setAreaClicked(self): # 点击“Set Area”按钮  信号与槽函数
        area_win = SubAreaView()
        area_win.area_signal.connect(self.setArea_text)
        area_win.exec()

    def setLinesClicked(self): # 点击“Set Lines”按钮  信号与槽函数
        line_win = SubLineView()
        line_win.line_signal.connect(self.setLine_text)
        line_win.exec()

    def loadVideoClicked(self): # 点击“Load Video”按钮  信号与槽函数
        print("你点击了Load Video按钮")

    def setLine_text(self, chosen_line): # 画线后点击确认，将坐标值显示出来
        self.ui.setLinesLineEdit.setText(chosen_line)

    def setArea_text(self, chose_area): # 画区域后点击确认，将坐标值显示出来
        self.ui.setAreaLlineEdit.setText(chose_area)