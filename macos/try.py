from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QMainWindow
import sys


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.initUI()


def clicked():
    print("clicked")


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Instant Kill Mode")

    label = QtWidgets.QLabel(win)
    label.setText("Instant Kill")
    label.move(100, 100)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Kill")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())


window()
