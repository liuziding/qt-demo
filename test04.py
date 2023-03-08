import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1300,800)
        self.setup_ui()

    def setup_ui(self):
        # 总的控件个数
        self.widget_count = 4
        # 一行又多少列
        self.column_count = 2

        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        for i in range(0, self.widget_count):
            label = QLabel("Label", self)
            label.setStyleSheet("border: 2px solid #D7D7D7;")
            h_video_label = QHBoxLayout()
            stop_button = QPushButton("Stop")
            set_lines_button = QPushButton("Set_Lines")
            set_area_button = QPushButton("Set_Area")
            start_button = QPushButton("Start")
            export_button = QPushButton("Export")
            Detail_button = QPushButton("Detail")
            h_video_label.addStretch()
            h_video_label.addWidget(stop_button)
            h_video_label.addWidget(set_lines_button)
            h_video_label.addWidget(set_area_button)
            h_video_label.addWidget(start_button)
            h_video_label.addWidget(export_button)
            h_video_label.addWidget(Detail_button)
            h_video_label.addStretch()

            label.setLayout(h_video_label)


            grid_layout.addWidget(label, i // self.column_count, i % self.column_count)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())