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

        # creating push button 5
        push5 = QPushButton('5', self)
        push5.setGeometry(95, 200, 80, 40)

        # creating push button 6
        push6 = QPushButton('6', self)
        push6.setGeometry(185, 200, 80, 40)

        # creating push button 7
        push7 = QPushButton('7', self)
        push7.setGeometry(5, 250, 80, 40)

        # creating push button 8
        push8 = QPushButton('8', self)
        push8.setGeometry(95, 250, 80, 40)

        # creating push button 9
        push9 = QPushButton('9', self)
        push9.setGeometry(185, 250, 80, 40)

        # creating push button 0
        push0 = QPushButton('4', self)
        push0.setGeometry(5, 300, 80, 40)

        # equal button
        push_equal = QPushButton("=", self)
        push_equal.setGeometry(275, 300, 80, 40)

        # adding equal button a color effect
        c_effect = QGraphicsColorizeEffect()
        c_effect.setColor(Qt.blue)
        push_equal.setGraphicsEffect(c_effect)

        # creating push button +
        push_plus = QPushButton("+", self)
        push_plus.setGeometry(275, 250, 80, 40)

        # creating push button -
        push_minus = QPushButton("-", self)
        push_minus.setGeometry(275, 200, 80, 40)

        # creating push button *
        push_mul = QPushButton("*", self)
        push_mul.setGeometry(275, 150, 80, 40)

        # creating push button /
        push_div = QPushButton("/", self)
        push_div.setGeometry(185, 300, 80, 40)

        # creating push button .
        push_point = QPushButton(".", self)
        push_point.setGeometry(95, 300, 80, 40)

        # creating push button clear
        push_clear = QPushButton("Clear", self)
        push_clear.setGeometry(5, 100, 200, 40)

        # creating push button Del
        push_del = QPushButton("Del", self)
        push_del.setGeometry(210, 100, 140, 40)

        # adding action to each of the button
        push_minus.clicked.connect(self.action_minus)
        push_equal.clicked.connect(self.action_equal)
        push_div.clicked.connect(self.action_div)
        push_mul.clicked.connect(self.action_mul)
        push_plus.clicked.connect(self.action_plus)
        push_point.clicked.connect(self.action_point)
        push_clear.clicked.connect(self.action_clear)
        push_del.clicked.connect(self.action_del)

        # adding action to each of the number button
        push1.clicked.connect(self.action1)
        push2.clicked.connect(self.action2)
        push3.clicked.connect(self.action3)
        push4.clicked.connect(self.action4)
        push5.clicked.connect(self.action5)
        push6.clicked.connect(self.action6)
        push7.clicked.connect(self.action7)
        push8.clicked.connect(self.action8)
        push9.clicked.connect(self.action9)

    def action_equal(self):
        # get the label text
        equation = self.label.text()

        try:
            # getting the answer
            ans = eval(equation)

            # setting text to the label
            self.label.setText(str(ans))

        except:
            # setting text to the label
            self.label.setText("Wrong Input")

        def action_plus(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "+")

        def action_minus(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + " - ")

        def action_mul(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + " * ")

        def action_div(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + " / ")

        def action_point(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + ".")

        def action0(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "0")

        def action1(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "1")

        def action2(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "2")

        def action3(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "3")

        def action4(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "4")

        def action5(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "5")

        def action6(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "6")

        def action7(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "7")

        def action8(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "8")

        def action9(self):
            # appending label text
            text = self.label.text()
            self.label.setText(text + "9")
