import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class TestFont(QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setGeometry(200, 200, 800, 600)
        self.createFont()
        self.createLabel()
        self.getLabelFont()

    def createFont(self):
        self.fonts = list()
        fontName = ('宋体','仿宋','黑体','楷体','隶书','幼圆','华文中宋','方正舒体', '华文黑体', 'Times New Roman')
        for i in range(0, len(fontName)):
            f = QFont()
            f.setPointSizeF(25.5)
            f.setFamily(fontName[i])
            self.fonts.append(f)
        self.fonts[0].setBold(True)
        self.fonts[1].setItalic(True)
        self.fonts[2].setStrikeOut(True)
        self.fonts[3].setOverline(True)
        self.fonts[4].setUnderline(True)
        self.fonts[5].setCapitalization(QFont.AllUppercase)
        self.fonts[6].setWeight(QFont.Thin)
        self.fonts[7].setWordSpacing(50)
        self.fonts[8].setStretch(70)
        self.fonts[9].setPixelSize(50)

    def createLabel(self):
        self.labels = list()
        string = "liu zi ding, 社会我定哥，人狠话不多！"
        for i in range(1):
            label = QLabel(self)
            label.setGeometry(0, 50 * i, 800, 70)
            label.setText(str(i) + ": " + string)
            label.setFont(self.fonts[i])
            self.labels.append(label)

    def getLabelFont(self):
        print("字体信息：")
        template = "Label {}, family:{}, Bold:{}, Italic:{}, StrikeOut:{}, OverLine:{}, UnderLine:{}, " \
            "Capitalization:{}, Weight:{}, WordSpacing:{}, Stretch:{}, PixelSize:{}, PointSize:{}"
        j = 0
        for i in self.labels:
            f = i.font()  #获取标签的字体
            print(template.format(j,f.family(),f.bold(),f.italic(),f.strikeOut(),f.overline(),f.underline(),
            f.capitalization(),f.weight(),f.wordSpacing(),f.stretch(),f.pixelSize(),f.pointSize()))
            j = j+1

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = app.font()
    font.setFamily("Helvetica [Cronyx]")
    app.setFont(font)
    window = TestFont()
    window.show()
    sys.exit(app.exec())
