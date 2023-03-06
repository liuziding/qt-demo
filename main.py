import sys

from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QLabel, QMenu,
                      QHBoxLayout,QFileDialog,QWidget,QSlider, QScrollArea, QTextEdit,
                      QListWidget, QListWidgetItem, QMainWindow, QMenuBar, QTableWidget)
from PySide6.QtCore import QUrl, Qt, QSize
from PySide6.QtGui import QAction, QColor, QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget

from components.btnGroupWidget import BtnGroupWidget
from components.contentWidget import ContentWidget

class MyMainWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)

        # 窗口上部分按钮组
        self.btn_group_widget = BtnGroupWidget(self)

        # 窗口下半部分控件
        self.content_widget = ContentWidget()

        self.setup_ui()

        self.show()

    def setup_ui(self):

        # 中心控件
        centre_widget = QWidget()

        # 中心控件布局 分为上下两部分
        centre_layout = QVBoxLayout()
        centre_layout.setContentsMargins(0, 0, 0, 0)
        centre_layout.setSpacing(0)

        # 绑定信号
        centre_layout.addWidget(self.btn_group_widget)

        # 设置中心控件布局
        centre_widget.setLayout(centre_layout)

        # 设置中心控件
        self.setCentralWidget(centre_widget)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWidget()
    window.setWindowTitle("主窗口")
    window.setWindowIcon(QIcon("./icons/1.jpg"))
    window.setFixedSize(1500, 760)
    sys.exit(app.exec())


