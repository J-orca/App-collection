import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon


def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(1100, 300, 800, 500)
    win.setWindowTitle("TBA")
    win.setWindowIcon(QIcon("R.jpg"))
    win.show()
    sys.exit(app.exec_())


window()
