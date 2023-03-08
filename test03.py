import sys
from PySide6.QtWidgets import (QApplication,QPushButton,QVBoxLayout, QMainWindow,
       QHBoxLayout,QFileDialog,QWidget,QGraphicsView,QGraphicsScene)
from PySide6.QtCore import QUrl,Qt
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget,QGraphicsVideoItem

class MyWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("主窗口")
        self.resize(900, 700)
        self.setup_ui()

    def setup_ui(self):
        self.graphicsView = QGraphicsView() # 视图窗口
        # self.


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())