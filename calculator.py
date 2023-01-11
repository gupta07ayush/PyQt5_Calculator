# importing libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python Calculator")

        # set window geometry
        self.setGeometry(100, 100, 360, 350)

        # calling method
        self.UiComponents()

        # show all widgets
        self.show()

    # Method for widgets
    def UiComponents(self):

        # creating a label
        self.label = QLabel(self)

        # setting geometry to the label
        self.label.setGeometry(5, 5, 350, 70)

        # creating label multi line
        self.label.setWordWrap(True)

        # setting style sheet to the label
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border:4px sold black;"
                                 'background:white;'
                                 '}')

        # setting alignment to the label
        self.label.setAlignment(Qt.Alignment)

        # setting font
        self.label.setFont(QFont('Arial', 15))

        # adding number button to the screen creating a push button
        push1 = QPushButton('1', self)

        # setting geometry
        push1.setGeometry(5, 150, 80, 40)

        # creating push button 2
        push2 = QPushButton("2", self)
        push2.setGeometry(95, 150, 80, 40)

        # creating push button 3
        push3 = QPushButton('3', self)
        push3.setGeometry(185, 150, 80, 40)

        # creating push button 4
        push4 = QPushButton('4', self)
        push4.setGeometry(5, 200, 80, 40)
