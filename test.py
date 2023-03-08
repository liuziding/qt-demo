import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MyMainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(900, 700)
        self.setup_ui()

    def setup_ui(self):
        """展示布局界面"""
        # 总的控件个数
        self.widget_count = 3
        # 一行又多少列
        self.column_count = 1
        if self.widget_count > 1:
            self.column_count = 2
        print(self.width())
        # 计算一个控件的宽度
        widget_width = self.width() / self.column_count
        # 总共又多少行（编号 // 一行多少列 + 1）
        row_count = (self.widget_count - 1) // self.column_count + 1
        widget_height = self.height() / row_count

        for i in range(0, self.widget_count):
            w = QWidget(self)
            w.resize(widget_width, widget_height)
            widget_x = i % self.column_count * widget_width
            widget_y = i // self.column_count * widget_height
            w.move(widget_x, widget_y)
            w.setStyleSheet("background-color: red; border: 2px solid #333;")
            w.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWidget()
    window.show()
    sys.exit(app.exec())