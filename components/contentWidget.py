import sys

from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QLabel, QMenu,
                      QHBoxLayout,QFileDialog,QWidget,QSlider, QScrollArea, QTextEdit,
                      QListWidget, QListWidgetItem, QMainWindow, QMenuBar, QTableWidget)
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QAction, QColor, QPixmap
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

class ContentWidget(QMainWindow):
    def __init__(self):
        super(ContentWidget, self).__init__()
        self.setup_ui()

    def setup_ui(self):
        # 创建左、中、右三个部件
        self.left_widget = QListWidget()
        conter_widget = QTableWidget()
        right_widget = QTableWidget()

        # 设置左部件列表
        for i in range(5):
            text = f"{i+1}. video video video video video video video video"
            item = QListWidgetItem(text)
            item.setToolTip(text)
            item.setSizeHint(QSize(0, 40))
            self.left_widget.addItem(item)
        
        self.left_widget.setMaximumWidth(200)
        self.left_widget.setMaximumHeight(736)
        self
