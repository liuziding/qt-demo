from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
# from PySide6.QtGui import *
from PySide6.QtCore import QFile, Qt

from utils.commonhelper import CommonHelper

class MainNavWidget(QWidget):
    
    def __init__(self, window):
        super(MainNavWidget, self).__init__()

        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        file = QFile("./qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')
        layout = QHBoxLayout()

        # 显示按钮组
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

        layout.addWidget(parameter_setting_button)
        layout.addSpacing(-10)
        layout.addWidget(increase_video_button)
        layout.addSpacing(-10)
        layout.addWidget(decrease_video_button)
        layout.addSpacing(-10)
        layout.addWidget(refresh_video_button)
        layout.addSpacing(-10)
        layout.addStretch()

        # 创建一个新控件，将水平布局设置为其主布局，并将其背景颜色设置为红色
        layout_widget = QWidget()
        layout_widget.setLayout(layout)
        layout_widget.move(0, 0)
        layout_widget.setFixedHeight(48)
        layout_widget.setStyleSheet("background-color: white;")

        # 将新空间添加到窗口中
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(layout_widget)

        # main_layout.setSpacing(12)
        # main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)

