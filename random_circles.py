import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from random import randint
from UI import Ui_Form


print()
class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = True
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.flag = False
            self.qp.end()

    def drawf(self):
        self.flag = True
        self.update()

    def draw(self):
        self.qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        self.qp.setPen(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        raz = randint(10, 50)
        x = randint(50, 200)
        y = randint(50, 100)
        self.qp.drawEllipse(x, y, raz, raz)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
