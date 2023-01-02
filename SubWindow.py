# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class SubWindow(QWidget):
    def __init__(self):
        super(SubWindow, self).__init__()
        self.resize(1200, 800)
