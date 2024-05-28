import sys
from PyQt5.QtWidgets import *
# 무조건 두 칸 띄우기

class Main(QMainWindow) :
    def __init__(self):
        super(Main, self).__init__()

        self.label = QLabel("안녕하세요", self)
# 무조건 두 칸 띄우기

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()

# PyQt위젯 기본 세팅
