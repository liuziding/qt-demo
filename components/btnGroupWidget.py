from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
# from PySide6.QtGui import *
from PySide6.QtCore import QFile, Qt

from utils.commonhelper import CommonHelper

class BtnGroupWidget(QWidget):
    
    def __init__(self, window):
        super(BtnGroupWidget, self).__init__()

        self.setup_ui()

    def setup_ui(self):
        # 加载样式表文件
        file = QFile("./qss/app.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        stylesheet = file.readAll().data().decode('utf-8')
        layout = QHBoxLayout()

        # 显示按钮组
        param_setting_button = QPushButton("参数设置")
        import_Video_button = QPushButton("导入视频")
        start_identify_button = QPushButton("开始识别")
        export_end_button = QPushButton("导出结束")
        delete_video_button = QPushButton("删除视频")
        refresh_button = QPushButton("刷新")

        # 设置属性
        param_setting_button.setObjectName("top_btn_group")
        import_Video_button.setObjectName("top_btn_group")
        start_identify_button.setObjectName("top_btn_group")
        export_end_button.setObjectName("top_btn_group")
        delete_video_button.setObjectName("top_btn_group")
        refresh_button.setObjectName("top_btn_group")

        # 设置样式
        param_setting_button.setStyleSheet(stylesheet)
        param_setting_button.setCursor(Qt.PointingHandCursor)
        import_Video_button.setStyleSheet(stylesheet)
        import_Video_button.setCursor(Qt.PointingHandCursor)
        start_identify_button.setStyleSheet(stylesheet)
        start_identify_button.setCursor(Qt.PointingHandCursor)
        export_end_button.setStyleSheet(stylesheet)
        export_end_button.setCursor(Qt.PointingHandCursor)
        delete_video_button.setStyleSheet(stylesheet)
        delete_video_button.setCursor(Qt.PointingHandCursor)
        refresh_button.setStyleSheet(stylesheet)
        refresh_button.setCursor(Qt.PointingHandCursor)

        layout.addWidget(param_setting_button)
        layout.addSpacing(-10)
        layout.addWidget(import_Video_button)
        layout.addSpacing(-10)
        layout.addWidget(start_identify_button)
        layout.addSpacing(-10)
        layout.addWidget(export_end_button)
        layout.addSpacing(-10)
        layout.addWidget(delete_video_button)
        layout.addSpacing(-10)
        layout.addWidget(refresh_button)
        layout.addStretch()

        # 创建一个新控件，将水平布局设置为其主布局，并将其背景颜色设置为红色
        layout_widget = QWidget()
        layout_widget.setLayout(layout)
        layout_widget.move(0, 0)
        layout_widget.setFixedHeight(64)
        layout_widget.setStyleSheet("background-color: white;")

        # 将新空间添加到窗口中
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(layout_widget)

        # main_layout.setSpacing(12)
        # main_layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(main_layout)

