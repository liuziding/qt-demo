import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

class MyWindow(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.resize(1300,800)
        self.setStyleSheet("background-color: #fff;")
        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        file = QFile("qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')
        
        self.setStyleSheet("background-color: #fff;")

        


        # 总的控件个数
        self.widget_count = 4
        # 一行又多少列
        self.column_count = 2

        grid_layout = QGridLayout(self)
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        for i in range(0, self.widget_count):
            label = QLabel("", self)
            label.setObjectName("video_label")
            h_video_label = QHBoxLayout()
            h_video_label.setSpacing(6)
            stop_button = self.MyPushButton("Stop", "main_view_button")
            set_lines_button = self.MyPushButton("Set_Lines", "main_view_button")
            set_area_button = self.MyPushButton("Set_Area", "main_view_button")
            start_button = self.MyPushButton("Start", "main_view_button")
            export_button = self.MyPushButton("Export", "main_view_button")
            detail_button = self.MyPushButton("Detail", "main_view_button")

            label.setObjectName("main_video_label")
            stop_button.setObjectName("main_view_button")


            h_video_label.addStretch()
            h_video_label.addWidget(stop_button)
            h_video_label.addWidget(set_lines_button)
            h_video_label.addWidget(set_area_button)
            h_video_label.addWidget(start_button)
            h_video_label.addWidget(export_button)
            h_video_label.addWidget(detail_button)
            h_video_label.addStretch()

            label.setLayout(h_video_label)


            grid_layout.addWidget(label, i // self.column_count, i % self.column_count)
        
        self.setStyleSheet(stylesheet)

    def MyPushButton(self, text, className):
            btn = QPushButton(text)
            btn.setObjectName(className)
            return btn

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())