import sys
from PyQt5.QtWidgets import (QWidget, QApplication, QLabel, QLineEdit, QPushButton, QGridLayout, QGroupBox, QHBoxLayout, QVBoxLayout, QTextEdit)
from PyQt5.QtGui import QIcon

class Click(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.x = 300  # or left
        self.y = 300  # or top
        self.width = 400
        self.height = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x, self.y, self.width, self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        self.createGridLayout()
        self.setLayout(self.layout)
        self.show()

    def createGridLayout(self):
        self.layout = QGridLayout()
        self.button = QPushButton("Click to Change Color", self)
        self.button.clicked.connect(self.changeColor)
        self.layout.addWidget(self.button, 2, 2)

    def changeColor(self):
        self.button.setStyleSheet("background-color: yellow")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Click()
    sys.exit(app.exec_())
