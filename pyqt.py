import sys
from PyQt5.QtWidgets import *


class Main(QMainWindow) :
    def __init__(self):
        super(Main, self).__init__()

        self.label = QLabel("안녕하세요", self)


app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()