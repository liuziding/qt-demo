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

        # 将QHBoxLayout设置为top_widget的布局
        top_widget.setLayout(top_layout)

        # 创建一个QWidget来显示QGridLayout
        bottom_widget = QWidget()

        for i in range(0, self.widget_count):
            label = QLabel("", self)
            label.setStyleSheet("border: 2px solid #D7D7D7;")
            label.setObjectName("main_video_label")
            v_video_layout = QVBoxLayout()
            h_video_layout = QHBoxLayout()
            h_btn_label = QHBoxLayout()
            h_btn_label.setSpacing(6)
            stop_button = self.MyPushButton("Stop", "main_video_button")
            set_lines_button = self.MyPushButton("Set_Lines", "main_video_button")
            set_area_button = self.MyPushButton("Set_Area", "main_video_button")
            start_button = self.MyPushButton("Start", "main_video_button")
            export_button = self.MyPushButton("Export", "main_video_button")
            detail_button = self.MyPushButton("Detail", "main_video_button")

            stop_button.setStyleSheet(stylesheet)
            set_lines_button.setStyleSheet(stylesheet)
            set_area_button.setStyleSheet(stylesheet)
            start_button.setStyleSheet(stylesheet)
            export_button.setStyleSheet(stylesheet)
            detail_button.setStyleSheet(stylesheet)

            h_btn_label.addStretch()
            h_btn_label.addWidget(stop_button)
            h_btn_label.addWidget(set_lines_button)
            h_btn_label.addWidget(set_area_button)
            h_btn_label.addWidget(start_button)
            h_btn_label.addWidget(export_button)
            h_btn_label.addWidget(detail_button)
            h_btn_label.addStretch()

            image_label = QLabel()
            pixmap = QPixmap("icons/1.jpg")
            pixmap_w = pixmap.width()
            pixmap_h = pixmap.height()
            image_w = image_label.width()
            image_h = image_label.height()
            ratio_w = pixmap_w / image_w
            ratio_h = pixmap_h / image_h
            print((pixmap.width() / ratio_w - 20))
            print((pixmap.height() / ratio_w - 44))
            new_pixmap = None
            if ratio_w > ratio_h:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_w - 20), (pixmap.height() / ratio_w - 44))
            else:
                new_pixmap = pixmap.scaled((pixmap.width() / ratio_h - 20), (pixmap.height() / ratio_h - 20))
            
            print(image_label.width())
            print(image_label.height())
            image_label.setAlignment(Qt.AlignCenter)
            image_label.setPixmap(new_pixmap)
            # label.setStyleSheet("border: 1px solid red;")
            splitter_H = QSplitter(Qt.Horizontal)
            print(splitter_H.width())
            print(splitter_H.height())
            h_video_layout.addWidget(splitter_H)
            splitter_H.addWidget(image_label)

            # v_video_layout = QVBoxLayout()
            # btn_v = QPushButton("按钮")
            # v_video_layout.addWidget(h_video_layout)
            v_video_layout.addLayout(h_video_layout)
            # v_video_layout.addStretch(1)
            v_video_layout.addLayout(h_btn_label)


            # v_video_layout.addWidget(graphicsview)

            # video_show_label.setLayout(graphicsview)
            # rect_widget = QWidget()
            # rect_label = QLabel(self)
            # pixmap = QPixmap("icons/1.jpg")
            # new_pixmap = pixmap.scaled(pixmap.width() // 10, pixmap.height() // 10)
            # rect_label.setPixmap(new_pixmap)

            # # v_video_layout.addWidget(video_show_label)
            # # v_video_layout.addStretch(0)
            # v_video_layout.addWidget(rect_label)

            label.setLayout(v_video_layout)

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

    def MyPushButton(self, text, className):
            btn = QPushButton(text)
            btn.setObjectName(className)
            return btn

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWidget()
    window.show()
    sys.exit(app.exec())