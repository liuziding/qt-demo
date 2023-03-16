# import sys
# from PySide6.QtWidgets import *
# from PySide6.QtGui import *

# class ImageWidget(QWidget):
#     def __init__(self, image_path):
#         super().__init__()
#         self.label = QLabel(self)
#         pixmap = QPixmap(image_path)
#         self.label.setPixmap(pixmap)
#         self.label.setAlignment(Qt.AlignCenter)

#         # Resize the widget to match the image size
#         self.resize(pixmap.width(), pixmap.height())

#     def resizeEvent(self, event):
#         # Scale the pixmap to fit the resized widget
#         pixmap = self.label.pixmap().scaled(
#             self.label.size(), 
#             Qt.KeepAspectRatio, 
#             Qt.SmoothTransformation
#         )
#         self.label.setPixmap(pixmap)
#         self.label.move(self.width() / 2 - pixmap.width() / 2, self.height() / 2 - pixmap.height() / 2)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     widget = ImageWidget('images/inside.jpg')
#     widget.show()
#     sys.exit(app.exec())



import sys
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # 创建标签并设置图片
        label = QLabel()
        pixmap = QPixmap('images/inside.jpg')
        label.setPixmap(pixmap)

        # 将标签放在一个布局中
        layout = QVBoxLayout()
        layout.addWidget(label)

        # 设置布局以及窗口的边框
        self.setLayout(layout)
        self.setFixedSize(400, 400)
        self.setStyleSheet("border: 2px solid black;")

        # 让图片在标签中居中
        label.setAlignment(Qt.AlignCenter)
        label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
