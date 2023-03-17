import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Window")
        self.resize(300, 200)

    def resizeEvent(self, event):
        size = self.frameGeometry().size()
        print(f"Window size: {size.width()} x {size.height()}")

        # Call the base class resizeEvent method
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec())