import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from ui.ui_main02 import Ui_MainWindow
from .subLineView import SubLineView
from components.subAreaView import SubAreaView

image_w = 200
image_h = 120

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.l_imageArea.setAlignment(Qt.AlignCenter)
        self.pixmap = QPixmap("images/inside.jpg")
        self.pixmap_w = self.pixmap.width()
        self.pixmap_h = self.pixmap.height()
        label_w = self.ui.l_imageArea.width() - 10
        label_h = self.ui.l_imageArea.height() - 10
        print("1234234")
        print(label_w)
        print(label_h)
        ratio_w = self.pixmap_w / label_w
        ratio_h = self.pixmap_h / label_h
        if ratio_w > ratio_h:
            new_pixmap = self.pixmap.scaled((self.pixmap_w / ratio_w), (self.pixmap_h / ratio_w))
        else:
            new_pixmap = self.pixmap.scaled((self.pixmap_w / ratio_h), (self.pixmap_h / ratio_h))
            
        self.ui.l_imageArea.setPixmap(new_pixmap)


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

    def resizeEvent(self, evt):
        
        if self.ui.l_imageArea:

            print(self.ui.l_imageArea.size())
            label_w = self.ui.l_imageArea.width() - 10
            label_h = self.ui.l_imageArea.height() - 10
            print("456457456")
            print(label_w)
            print(label_h)
            ratio_w = self.pixmap_w / label_w
            ratio_h = self.pixmap_h / label_h
            if ratio_w > ratio_h:
                new_pixmap = self.pixmap.scaled((self.pixmap_w / ratio_w), (self.pixmap_h / ratio_w))
            else:
                new_pixmap = self.pixmap.scaled((self.pixmap_w / ratio_h), (self.pixmap_h / ratio_h))
                
            self.ui.l_imageArea.setPixmap(new_pixmap)

        super().resizeEvent(evt)
    