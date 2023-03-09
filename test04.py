import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和固定大小
        self.setWindowTitle("图片自适应固定大小的窗口")
        self.setFixedSize(1000, 300)

        # 加载图片
        self.image = QPixmap("icons/inside.jpg")

        # 创建标签并设置图片
        self.label = QLabel(self)
        self.label.setPixmap(self.image)

        # 设置标签在窗口中的位置和大小，并使其自适应窗口大小并保持纵横比
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setScaledContents(True)
        self.label.resize(self.width(), self.height())

        # 将标签添加到窗口中
        self.setCentralWidget(self.label)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
