import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class AppWidget(QWidget):
    """程序界面设定控制类"""
    def __init__(self):
        # 调用弗雷德初始化方法
        super().__init__()
        # 调用界面初始化方法（一般会将UI界面的代码封装到另一个方法函数中，而不直接
        self.init_ui()
        # 加载文件中储存的所有人员信息
        self.load_all_infos()

    def init_ui(self):
        """设置UI界面"""
        self.setWindowTitle("人员管理系统")
        self.setFixedSize(1220, 771)

        # 创建字体对象，用来对要显示的文字进行设定
        font = QFont()
        font.setFamily("黑体")
        font.setPointSize(12)

        # 姓名
        label_name = QLabel(self)
        label_name.setGeometry(40, 30, 54, 16)
        label_name.setText("姓名：")
        label_name.setFont(font)
        self.line_edit_name = QLineEdit(self)
        self.line_edit_name.setGeometry(90, 30, 141, 20)

        # 性别
        label_gender = QLabel(self)
        label_gender.setGeometry(270, 30, 54, 16)
        label_gender.setText("性别：")
        label_gender.setFont(font)
        self.line_edit_gender = QComboBox(self)
        self.line_edit_gender.setGeometry(340, 30, 201, 20)
        self.line_edit_gender.addItems(["男", "女"])



    def change_search_type(self):
        pass

    def get_all_infos(self):
        pass

    def search_info_from_files(self):
        pass

    def save_change_info(self):
        pass

    def generate_menu(self, pos):
        pass

    def reload_all_infos(self):
        pass

    def add_new_statent_info(self):
        pass

    def load_all_infos(self):
        pass

if __name__ == "__main__":
    # 创建应用程序对象
    app = QApplication(sys.argv)

    # 设置窗口风格
    QApplication.setStyle(QStyleFactory.create("Fusion"))
    print(QStyleFactory.keys())

    # 创建一个要显示的窗口对象
    app_widget = AppWidget()
    app_widget.show()

    # 让应用程序一直运行，在这期间会显示UI界面，检测事件等操作
    sys.exit(app.exec())