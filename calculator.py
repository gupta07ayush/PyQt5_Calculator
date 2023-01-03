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
