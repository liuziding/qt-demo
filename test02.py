import sys

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *

from components.mainNavWidget import MainNavWidget

class MyMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("主窗口")
        self.resize(1300, 800)
        self.setMinimumWidth(1300)
        self.setMinimumHeight(800)
        self.setStyleSheet("background-color: white;")
        self.setup_ui()

    def setup_ui(self):
        """展示布局界面"""
        # 加载样式表文件
        file = QFile("qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')

        # 总的控件个数
        self.widget_count = 4
        # 一行又多少列
        self.column_count = 2
        grid_layout = QGridLayout()
        grid_layout.setContentsMargins(0, 0, 0, 0)
        grid_layout.setSpacing(0)

        # 创建一个QWidget来显示导航栏按钮组
        top_widget = QWidget()
        top_widget.setFixedHeight(36)

        # 显示导航栏按钮组
        parameter_setting_button = QPushButton("参数设置")
        increase_video_button = QPushButton("加频")
        decrease_video_button = QPushButton("减频")
        refresh_video_button = QPushButton("刷新")

        # 设置属性
        parameter_setting_button.setObjectName("main_nav_btn")
        increase_video_button.setObjectName("main_nav_btn")
        decrease_video_button.setObjectName("main_nav_btn")
        refresh_video_button.setObjectName("main_nav_btn")

        # 设置样式
        parameter_setting_button.setStyleSheet(stylesheet)
        parameter_setting_button.setCursor(Qt.PointingHandCursor)
        increase_video_button.setStyleSheet(stylesheet)
        increase_video_button.setCursor(Qt.PointingHandCursor)
        decrease_video_button.setStyleSheet(stylesheet)
        decrease_video_button.setCursor(Qt.PointingHandCursor)
        refresh_video_button.setStyleSheet(stylesheet)
        refresh_video_button.setCursor(Qt.PointingHandCursor)

        # 将这些QPushButton添加到QHBoxLayout中
        top_layout = QHBoxLayout()
        top_layout.setContentsMargins(8, 0, 0, 0)
        top_layout.addWidget(parameter_setting_button)
        top_layout.addSpacing(-6)
        top_layout.addWidget(increase_video_button)
        top_layout.addSpacing(-6)
        top_layout.addWidget(decrease_video_button)
        top_layout.addSpacing(-6)
        top_layout.addWidget(refresh_video_button)
        top_layout.addStretch()

        # 创建一个QWidget来显示QGridLayout
        bottom_widget = QWidget()


        # 将QHBoxLayout设置为top_widget的布局
        top_widget.setLayout(top_layout)

        for i in range(0, self.widget_count):
            label = QLabel("Label", self)
            label.setStyleSheet("border: 2px solid #D7D7D7;")
            grid_layout.addWidget(label, i // self.column_count, i % self.column_count)

        # 将QGridLayout设置为bottom_widget的布局
        bottom_widget.setLayout(grid_layout)

        # 创建一个QVBoxLayout来放置top_widget和bottom_widget
        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(top_widget)
        main_layout.addWidget(bottom_widget)
        self.setLayout(main_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWidget()
    window.show()
    sys.exit(app.exec())