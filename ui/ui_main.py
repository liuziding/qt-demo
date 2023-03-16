# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1142, 944)
        MainWindow.setStyleSheet(u"QWidget#MainWindow {\n"
"	background: #fff;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 28))
        self.lineEdit.setMaximumSize(QSize(16777215, 28))
        self.lineEdit.setStyleSheet(u"QWidget#lineEdit {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.verticalLayout.addWidget(self.lineEdit)

        self.videoFrame = QFrame(self.centralwidget)
        self.videoFrame.setObjectName(u"videoFrame")
        self.videoFrame.setMinimumSize(QSize(600, 400))
        self.videoFrame.setFrameShape(QFrame.StyledPanel)
        self.videoFrame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.videoFrame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 180))
        self.frame_2.setMaximumSize(QSize(167777, 180))
        self.frame_2.setStyleSheet(u"QWidget#frame_2 {\n"
"	border: 0;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.loadVideoLineEdit = QLineEdit(self.frame_2)
        self.loadVideoLineEdit.setObjectName(u"loadVideoLineEdit")
        self.loadVideoLineEdit.setMinimumSize(QSize(0, 28))
        self.loadVideoLineEdit.setMaximumSize(QSize(16777215, 28))
        self.loadVideoLineEdit.setStyleSheet(u"QWidget#loadVideoLineEdit {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout.addWidget(self.loadVideoLineEdit)

        self.loadVideoButton = QPushButton(self.frame_2)
        self.loadVideoButton.setObjectName(u"loadVideoButton")
        self.loadVideoButton.setMinimumSize(QSize(110, 28))
        self.loadVideoButton.setMaximumSize(QSize(110, 28))
        self.loadVideoButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.loadVideoButton.setStyleSheet(u"QWidget#loadVideoButton {\n"
"	background: #fff;\n"
"	border-radius: 6px;\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout.addWidget(self.loadVideoButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.setLinesLineEdit = QLineEdit(self.frame_2)
        self.setLinesLineEdit.setObjectName(u"setLinesLineEdit")
        self.setLinesLineEdit.setMinimumSize(QSize(0, 28))
        self.setLinesLineEdit.setMaximumSize(QSize(16777215, 28))
        self.setLinesLineEdit.setStyleSheet(u"QWidget#setLinesLineEdit {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_3.addWidget(self.setLinesLineEdit)

        self.setLinesButton = QPushButton(self.frame_2)
        self.setLinesButton.setObjectName(u"setLinesButton")
        self.setLinesButton.setMinimumSize(QSize(110, 28))
        self.setLinesButton.setMaximumSize(QSize(110, 28))
        self.setLinesButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.setLinesButton.setStyleSheet(u"QWidget#setLinesButton {\n"
"	background: #fff;\n"
"	border-radius: 6px;\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_3.addWidget(self.setLinesButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.setAreaLlineEdit = QLineEdit(self.frame_2)
        self.setAreaLlineEdit.setObjectName(u"setAreaLlineEdit")
        self.setAreaLlineEdit.setMinimumSize(QSize(0, 28))
        self.setAreaLlineEdit.setMaximumSize(QSize(16777215, 28))
        self.setAreaLlineEdit.setStyleSheet(u"QWidget#setAreaLlineEdit {\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_2.addWidget(self.setAreaLlineEdit)

        self.setAreaButton = QPushButton(self.frame_2)
        self.setAreaButton.setObjectName(u"setAreaButton")
        self.setAreaButton.setMinimumSize(QSize(110, 32))
        self.setAreaButton.setMaximumSize(QSize(110, 32))
        self.setAreaButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.setAreaButton.setStyleSheet(u"QWidget#setAreaButton {\n"
"	background: #fff;\n"
"	border-radius: 6px;\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_2.addWidget(self.setAreaButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 32))
        self.frame_3.setMaximumSize(QSize(16777215, 32))
        self.frame_3.setStyleSheet(u"QWidget#frame_3 {\n"
"	border: 0;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.startButton = QPushButton(self.frame_3)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(80, 32))
        self.startButton.setMaximumSize(QSize(16777215, 32))
        self.startButton.setStyleSheet(u"QWidget#startButton {\n"
"	background: #fff;\n"
"	border-radius: 6px;\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_4.addWidget(self.startButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.stopButton = QPushButton(self.frame_3)
        self.stopButton.setObjectName(u"stopButton")
        self.stopButton.setMinimumSize(QSize(80, 32))
        self.stopButton.setMaximumSize(QSize(80, 32))
        self.stopButton.setStyleSheet(u"QWidget#stopButton {\n"
"	background: #fff;\n"
"	border-radius: 6px;\n"
"	border: 1px solid #BEBEBE;\n"
"}")

        self.horizontalLayout_4.addWidget(self.stopButton)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame_2)


        self.horizontalLayout_5.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1142, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.startButton.clicked.connect(MainWindow.startClicked)
        self.stopButton.clicked.connect(MainWindow.stopClicked)
        self.setAreaButton.clicked.connect(MainWindow.setAreaClicked)
        self.setLinesButton.clicked.connect(MainWindow.setLinesClicked)
        self.loadVideoButton.clicked.connect(MainWindow.loadVideoClicked)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u7a97\u53e3", None))
        self.loadVideoButton.setText(QCoreApplication.translate("MainWindow", u"Load Video", None))
        self.setLinesButton.setText(QCoreApplication.translate("MainWindow", u"Set Lines", None))
        self.setAreaButton.setText(QCoreApplication.translate("MainWindow", u"Set Area", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.stopButton.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
    # retranslateUi

