import sys
from PyQt5.QtWidgets import *
# 무조건 두 칸 띄우기

class Main(QMainWindow) :
    def __init__(self):
        super(Main, self).__init__()
        self.setGeometry(100, 100, 500, 300)
        self.setWindowTitle("워밍업 프로그램")

        # 시세조회
        self.getPriceLabel = QLabel("현재가격", self)
        self.getPriceLabel.move(55, 10)
        self.getPriceTextEdit = QTextEdit(self)
        self.getPriceTextEdit.move(30, 40)
        self.getPriceButton = QPushButton("조회", self)
        self.getPriceButton.move(150, 40)

        # 매수
        self.buyLabel = QLabel("매수금액", self)
        self.buyLabel.move(55, 90)
        self.buyTextEdit = QTextEdit(self)
        self.buyTextEdit.move(30, 120)
        self.buyButton = QPushButton("조회", self)
        self.buyButton.move(150, 120)

        # 매도
        self.sellLabel = QLabel("현재가격", self)
        self.sellLabel.move(55, 190)
        self.sellTextEdit = QTextEdit(self)
        self.sellTextEdit.move(30, 220)
        self.sellButton = QPushButton("조회", self)
        self.sellButton.move(150, 220)
# 무조건 두 칸 띄우기

app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()


# PyQt위젯 기본 세팅
