import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
import numpy as np
from GaussElimination import *
from GaussJordan import *
from LUDecomposition import *
from IterativeMethods import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Precision import *
import sys


class GUI(QMainWindow):

    def __init__(self):
        super(GUI, self).__init__()
        self.SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
        self.setupUi()
        self.show()

    def setupUi(self):
        self.setObjectName("Matrix Solver")
        self.setFixedSize(1200, 800)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.setFont(font)

        self.centralwidget = QtWidgets.QWidget(self)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # mainframe
        self.MainFrame = QtWidgets.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.MainFrame.setStyleSheet("background-color: rgb(46, 52, 54);\n""color: \"white\";")
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")

        self.titlelabel = QtWidgets.QLabel(self.MainFrame)
        self.titlelabel.setGeometry(QtCore.QRect(420, 40, 371, 81))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.titlelabel.setFont(font)
        self.titlelabel.setStyleSheet("color: \"white\";")
        self.titlelabel.setScaledContents(False)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")

        self.eqnlabel = QtWidgets.QLabel(self.MainFrame)
        self.eqnlabel.setGeometry(QtCore.QRect(180, 180, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eqnlabel.setFont(font)
        self.eqnlabel.setObjectName("eqnlabel")

        self.precision = QtWidgets.QLabel(self.MainFrame)
        self.precision.setGeometry(QtCore.QRect(180, 310, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.precision.setFont(font)
        self.precision.setObjectName("precision")

        self.operationbox = QtWidgets.QComboBox(self.MainFrame)
        self.operationbox.setGeometry(QtCore.QRect(720, 450, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.operationbox.setFont(font)
        self.operationbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.operationbox.setObjectName("operationbox")
        self.operationbox.addItem("")
        self.operationbox.addItem("")
        self.operationbox.addItem("")
        self.operationbox.addItem("")
        self.operationbox.addItem("")
        self.operation = QtWidgets.QLabel(self.MainFrame)
        self.operation.setGeometry(QtCore.QRect(180, 440, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operation.setFont(font)
        self.operation.setObjectName("operation")

        self.eqnbox = QtWidgets.QComboBox(self.MainFrame)
        self.eqnbox.setGeometry(QtCore.QRect(800, 190, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eqnbox.setFont(font)
        self.eqnbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(0, 0, 0);")
        self.eqnbox.setMaxVisibleItems(10)
        self.eqnbox.setObjectName("eqnbox")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")
        self.eqnbox.addItem("")

        self.precisionbox = QtWidgets.QComboBox(self.MainFrame)
        self.precisionbox.setGeometry(QtCore.QRect(800, 320, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.precisionbox.setFont(font)
        self.precisionbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.precisionbox.setObjectName("precisionbox")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")
        self.precisionbox.addItem("")

        self.proceedbtn = QtWidgets.QPushButton(self.MainFrame)
        self.proceedbtn.setGeometry(QtCore.QRect(950, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedbtn.setFont(font)
        self.proceedbtn.setObjectName("proceedbtn")
        self.proceedbtn.clicked.connect(self.proceedbtnChangeFrame)

        self.scalingbtn = QtWidgets.QPushButton(self.MainFrame)
        self.scalingbtn.setGeometry(QtCore.QRect(490, 570, 261, 81))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.scalingbtn.setFont(font)
        self.scalingbtn.setObjectName("scalingbtn")
        self.scalingState = False
        self.scalingbtn.setStyleSheet("QPushButton""{""background-color : red;""}")

        self.scalingbtn.clicked.connect(self.btnToggle)

        self.titlelabel.raise_()
        self.eqnlabel.raise_()
        self.precision.raise_()
        self.operationbox.raise_()
        self.eqnbox.raise_()
        self.precisionbox.raise_()
        self.proceedbtn.raise_()
        self.scalingbtn.raise_()
        self.operation.raise_()
        ##################################################

        self.equations = QtWidgets.QFrame(self.centralwidget)
        self.equations.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.equations.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                     "color: \"white\";")
        self.equations.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.equations.setFrameShadow(QtWidgets.QFrame.Raised)
        self.equations.setObjectName("equations")

        self.proceedeqnbtn = QtWidgets.QPushButton(self.equations)
        self.proceedeqnbtn.setGeometry(QtCore.QRect(960, 680, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedeqnbtn.setFont(font)
        self.proceedeqnbtn.setObjectName("proceedeqnbtn")
        self.proceedeqnbtn.clicked.connect(self.proceedbtnEqn)

        self.backButtone = QtWidgets.QPushButton(self.equations)
        self.backButtone.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtone.setFont(font)
        self.backButtone.setObjectName("backButton")
        self.backButtone.clicked.connect(self.backButtonShowMenu)
        #############################################################################

        # main
        self.main = QtWidgets.QFrame(self.centralwidget)
        self.main.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.main.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                "color: \"white\";")
        self.main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main.setObjectName("main")
        self.lineareqnsbtn = QtWidgets.QPushButton(self.main)
        self.lineareqnsbtn.setGeometry(QtCore.QRect(310, 200, 561, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineareqnsbtn.setFont(font)
        self.lineareqnsbtn.setObjectName("lineareqnsbtn")
        self.lineareqnsbtn.clicked.connect(self.gotomain)
        self.rootbtn = QtWidgets.QPushButton(self.main)
        self.rootbtn.setGeometry(QtCore.QRect(310, 460, 561, 151))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rootbtn.setFont(font)
        self.rootbtn.setObjectName("rootbtn")
        self.rootbtn.clicked.connect(self.gotoroot)
        self.operationlabel = QtWidgets.QLabel(self.main)
        self.operationlabel.setGeometry(QtCore.QRect(380, 40, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.operationlabel.setFont(font)
        self.operationlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.operationlabel.setObjectName("operationlabel")
        #############################################################################

        # rootscreen
        self.rootscreen = QtWidgets.QFrame(self.centralwidget)
        self.rootscreen.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.rootscreen.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                      "color: \"white\";")
        self.rootscreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.rootscreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.rootscreen.setObjectName("rootscreen")
        self.eqnlabel_2 = QtWidgets.QLabel(self.rootscreen)
        self.eqnlabel_2.setGeometry(QtCore.QRect(110, 110, 441, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.eqnlabel_2.setFont(font)
        self.eqnlabel_2.setObjectName("eqnlabel_2")
        self.precision_2 = QtWidgets.QLabel(self.rootscreen)
        self.precision_2.setGeometry(QtCore.QRect(110, 210, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.precision_2.setFont(font)
        self.precision_2.setObjectName("precision_2")
        self.operation_2 = QtWidgets.QLabel(self.rootscreen)
        self.operation_2.setGeometry(QtCore.QRect(110, 320, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operation_2.setFont(font)
        self.operation_2.setObjectName("operation_2")
        self.precisionbox_2 = QtWidgets.QComboBox(self.rootscreen)
        self.precisionbox_2.setGeometry(QtCore.QRect(760, 220, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.precisionbox_2.setFont(font)
        self.precisionbox_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.precisionbox_2.setObjectName("precisionbox_2")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.precisionbox_2.addItem("")
        self.proceedrootbtn = QtWidgets.QPushButton(self.rootscreen)
        self.proceedrootbtn.setGeometry(QtCore.QRect(950, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedrootbtn.setFont(font)
        self.proceedrootbtn.setObjectName("proceedrootbtn")
        # self.proceedrootbtn.clicked.connect()
        self.eqnin = QtWidgets.QLineEdit(self.rootscreen)
        self.eqnin.setGeometry(QtCore.QRect(480, 110, 681, 61))
        self.eqnin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(0, 0, 0);")
        self.eqnin.setText("")
        self.eqnin.setObjectName("eqnin")
        self.rootopbox = QtWidgets.QComboBox(self.rootscreen)
        self.rootopbox.setGeometry(QtCore.QRect(720, 330, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.rootopbox.setFont(font)
        self.rootopbox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                     "color: rgb(0, 0, 0);")
        self.rootopbox.setObjectName("rootopbox")
        self.rootopbox.addItem("")
        self.rootopbox.addItem("")
        self.rootopbox.addItem("")
        self.rootopbox.addItem("")
        self.rootopbox.addItem("")
        self.label_5 = QtWidgets.QLabel(self.rootscreen)
        self.label_5.setGeometry(QtCore.QRect(110, 420, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.iterationsin = QtWidgets.QLineEdit(self.rootscreen)
        self.iterationsin.setGeometry(QtCore.QRect(780, 440, 113, 29))
        self.iterationsin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.iterationsin.setText("")
        self.iterationsin.setObjectName("iterationsin")
        self.label_6 = QtWidgets.QLabel(self.rootscreen)
        self.label_6.setGeometry(QtCore.QRect(110, 520, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.epsin = QtWidgets.QLineEdit(self.rootscreen)
        self.epsin.setGeometry(QtCore.QRect(780, 540, 113, 29))
        self.epsin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                 "color: rgb(0, 0, 0);")
        self.epsin.setObjectName("epsin")
        self.backButtonroot = QtWidgets.QPushButton(self.rootscreen)
        self.backButtonroot.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtonroot.setFont(font)
        self.backButtonroot.setObjectName("backButton")
        self.backButtonroot.clicked.connect(self.backButtonShowMenu)
        #############################################################################

        # bisectionfalsi
        self.bisectionfalsi = QtWidgets.QFrame(self.centralwidget)
        self.bisectionfalsi.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.bisectionfalsi.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                          "color: \"white\";")
        self.bisectionfalsi.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bisectionfalsi.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bisectionfalsi.setObjectName("bisectionfalsi")
        self.label_2 = QtWidgets.QLabel(self.bisectionfalsi)
        self.label_2.setGeometry(QtCore.QRect(80, 150, 411, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.xlin = QtWidgets.QLineEdit(self.bisectionfalsi)
        self.xlin.setGeometry(QtCore.QRect(560, 170, 113, 29))
        self.xlin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 0, 0);")
        self.xlin.setObjectName("xlin")
        self.label_3 = QtWidgets.QLabel(self.bisectionfalsi)
        self.label_3.setGeometry(QtCore.QRect(80, 400, 421, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.xuin = QtWidgets.QLineEdit(self.bisectionfalsi)
        self.xuin.setGeometry(QtCore.QRect(560, 420, 113, 29))
        self.xuin.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 0, 0);")
        self.xuin.setObjectName("xuin")
        self.proceedfalsibtn = QtWidgets.QPushButton(self.bisectionfalsi)
        self.proceedfalsibtn.setGeometry(QtCore.QRect(950, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedfalsibtn.setFont(font)
        self.proceedfalsibtn.setObjectName("proceedfalsibtn")
        self.backButtonfalsi = QtWidgets.QPushButton(self.bisectionfalsi)
        self.backButtonfalsi.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtonfalsi.setFont(font)
        self.backButtonfalsi.setObjectName("backButton")
        self.backButtonfalsi.clicked.connect(self.backButtonShowMenu)
        ###########################################################

        # secant
        self.secant = QtWidgets.QFrame(self.centralwidget)
        self.secant.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.secant.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                  "color: \"white\";")
        self.secant.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.secant.setFrameShadow(QtWidgets.QFrame.Raised)
        self.secant.setObjectName("secant")
        self.label_4 = QtWidgets.QLabel(self.secant)
        self.label_4.setGeometry(QtCore.QRect(80, 150, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.x0in = QtWidgets.QLineEdit(self.secant)
        self.x0in.setGeometry(QtCore.QRect(750, 170, 113, 29))
        self.x0in.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 0, 0);")
        self.x0in.setObjectName("x0in")
        self.label_7 = QtWidgets.QLabel(self.secant)
        self.label_7.setGeometry(QtCore.QRect(80, 400, 531, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.x1in = QtWidgets.QLineEdit(self.secant)
        self.x1in.setGeometry(QtCore.QRect(750, 420, 113, 29))
        self.x1in.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(0, 0, 0);")
        self.x1in.setObjectName("x1in")
        self.proceedsecantbtn = QtWidgets.QPushButton(self.secant)
        self.proceedsecantbtn.setGeometry(QtCore.QRect(950, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedsecantbtn.setFont(font)
        self.proceedsecantbtn.setObjectName("proceedsecantbtn")
        self.backButtonsecant = QtWidgets.QPushButton(self.secant)
        self.backButtonsecant.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtonsecant.setFont(font)
        self.backButtonsecant.setObjectName("backButton")
        self.backButtonsecant.clicked.connect(self.backButtonShowMenu)
        ###########################################################

        # fixedpointnewton
        self.fixedpointnewton = QtWidgets.QFrame(self.centralwidget)
        self.fixedpointnewton.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.fixedpointnewton.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                            "color: \"white\";")
        self.fixedpointnewton.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fixedpointnewton.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fixedpointnewton.setObjectName("fixedpointnewton")
        self.label_8 = QtWidgets.QLabel(self.fixedpointnewton)
        self.label_8.setGeometry(QtCore.QRect(120, 300, 461, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.x0in_2 = QtWidgets.QLineEdit(self.fixedpointnewton)
        self.x0in_2.setGeometry(QtCore.QRect(760, 320, 113, 29))
        self.x0in_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                  "color: rgb(0, 0, 0);")
        self.x0in_2.setObjectName("x0in_2")
        self.proceedfixedbtn = QtWidgets.QPushButton(self.fixedpointnewton)
        self.proceedfixedbtn.setGeometry(QtCore.QRect(950, 660, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedfixedbtn.setFont(font)
        self.proceedfixedbtn.setObjectName("proceedfixedbtn")
        self.backButtonfixed = QtWidgets.QPushButton(self.fixedpointnewton)
        self.backButtonfixed.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtonfixed.setFont(font)
        self.backButtonfixed.setObjectName("backButton")
        self.backButtonfixed.clicked.connect(self.backButtonShowMenu)
        #########################################################

        # steps
        self.steps = QtWidgets.QFrame(self.centralwidget)
        self.steps.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.steps.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                 "color: \"white\";")
        self.steps.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.steps.setFrameShadow(QtWidgets.QFrame.Raised)
        self.steps.setObjectName("steps")

        self.scrollArea = QtWidgets.QScrollArea(self.steps)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(0, 600))
        self.scrollArea.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1198, 798))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #############################################################################

        # results
        self.Results = QtWidgets.QFrame(self.centralwidget)
        self.Results = QtWidgets.QFrame(self.centralwidget)
        self.Results.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.Results.setStyleSheet("background-color: rgb(46, 52, 54);\n"
                                   "color: \"white\";")
        self.Results.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Results.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Results.setObjectName("Results")

        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Results)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(200, 130, 791, 511))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.ResultsLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.ResultsLayout.setContentsMargins(0, 0, 0, 0)
        self.ResultsLayout.setObjectName("verticalLayout_5")

        self.stepsbtn = QtWidgets.QPushButton(self.Results)
        self.stepsbtn.setGeometry(QtCore.QRect(920, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.stepsbtn.setFont(font)
        self.stepsbtn.setObjectName("stepsbtn")
        self.stepsbtn.clicked.connect(self.showSteps)

        self.resultslabel = QtWidgets.QLabel(self.Results)
        self.resultslabel.setGeometry(QtCore.QRect(480, 40, 221, 91))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.resultslabel.setFont(font)
        self.resultslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.resultslabel.setObjectName("resultslabel")

        self.backButton = QtWidgets.QPushButton(self.Results)
        self.backButton.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonShowMenu)
        #############################################################################

        # Lu select frame
        self.LuSelectFrame = QtWidgets.QFrame(self.centralwidget)
        self.LuSelectFrame.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.LuSelectFrame.setStyleSheet("background-color: rgb(46, 52, 54);\n""color: \"white\";")
        self.LuSelectFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LuSelectFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LuSelectFrame.setObjectName("frame")

        self.operationbox_LU = QtWidgets.QComboBox(self.LuSelectFrame)
        self.operationbox_LU.setGeometry(QtCore.QRect(450, 340, 331, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.operationbox_LU.setFont(font)
        self.operationbox_LU.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                           "color: rgb(0, 0, 0);")
        self.operationbox_LU.setObjectName("operationbox_LU")
        self.operationbox_LU.addItem("")
        self.operationbox_LU.addItem("")
        self.operationbox_LU.addItem("")

        self.chooseLulabel = QtWidgets.QLabel(self.LuSelectFrame)
        self.chooseLulabel.setGeometry(QtCore.QRect(150, 90, 941, 101))
        font = QtGui.QFont()
        font.setPointSize(35)
        self.chooseLulabel.setFont(font)
        self.chooseLulabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chooseLulabel.setObjectName("chooseLulabel")

        self.proceedbtn_2 = QtWidgets.QPushButton(self.LuSelectFrame)
        self.proceedbtn_2.setGeometry(QtCore.QRect(900, 670, 261, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedbtn_2.setFont(font)
        self.proceedbtn_2.setObjectName("proceedbtn_2")
        self.proceedbtn_2.clicked.connect(self.showResults)

        self.backButtonlu = QtWidgets.QPushButton(self.LuSelectFrame)
        self.backButtonlu.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtonlu.setFont(font)
        self.backButtonlu.setObjectName("backButton")
        self.backButtonlu.clicked.connect(self.backButtonShowMenu)

        self.iterativeParameters = QtWidgets.QFrame(self.centralwidget)
        self.iterativeParameters.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.iterativeParameters.setStyleSheet("background-color: rgb(46, 52, 54);\n""color: \"white\";")
        self.iterativeParameters.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.iterativeParameters.setFrameShadow(QtWidgets.QFrame.Raised)
        self.iterativeParameters.setObjectName("frame_2")

        self.numOfIteraions = QtWidgets.QLabel(self.iterativeParameters)
        self.numOfIteraions.setGeometry(QtCore.QRect(90, 40, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.numOfIteraions.setFont(font)
        self.numOfIteraions.setObjectName("numOfIteraions")

        self.numOfIteraionsLineEdit = QtWidgets.QLineEdit(self.iterativeParameters)
        self.numOfIteraionsLineEdit.setGeometry(QtCore.QRect(560, 60, 113, 29))
        self.numOfIteraionsLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                                  "color: rgb(0, 0, 0);")
        self.numOfIteraionsLineEdit.setObjectName("numOfIteraionsLineEdit")
        self.numOfIteraionsLineEdit.setValidator(QDoubleValidator(-0.9, 0.9, 50))

        self.relativeErrolabel = QtWidgets.QLabel(self.iterativeParameters)
        self.relativeErrolabel.setGeometry(QtCore.QRect(90, 220, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.relativeErrolabel.setFont(font)
        self.relativeErrolabel.setObjectName("relativeErrolabel")

        self.relativeErrorLineEdit = QtWidgets.QLineEdit(self.iterativeParameters)
        self.relativeErrorLineEdit.setGeometry(QtCore.QRect(560, 241, 113, 29))
        self.relativeErrorLineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
        self.relativeErrorLineEdit.setObjectName("relativeErrorLineEdit")
        self.relativeErrorLineEdit.setValidator(QDoubleValidator(-0.9, 0.9, 50))

        self.initialGuesslabel = QtWidgets.QLabel(self.iterativeParameters)
        self.initialGuesslabel.setGeometry(QtCore.QRect(90, 380, 381, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.initialGuesslabel.setFont(font)
        self.initialGuesslabel.setObjectName("initialGuesslabel")

        self.proceedbtn_3 = QtWidgets.QPushButton(self.iterativeParameters)
        self.proceedbtn_3.setGeometry(QtCore.QRect(990, 690, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.proceedbtn_3.setFont(font)
        self.proceedbtn_3.setObjectName("proceedbtn_3")
        self.proceedbtn_3.clicked.connect(self.showResults)

        self.backButtoni = QtWidgets.QPushButton(self.iterativeParameters)
        self.backButtoni.setGeometry(QtCore.QRect(50, 670, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButtoni.setFont(font)
        self.backButtoni.setObjectName("backButton")
        self.backButtoni.clicked.connect(self.backButtonShowMenu)

        self.gridLayoutWidget = QtWidgets.QWidget(self.iterativeParameters)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(90, 480, 1051, 101))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.initialGuessgrid = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.initialGuessgrid.setContentsMargins(0, 0, 0, 0)
        self.initialGuessgrid.setObjectName("initialGuessgrid")

        # self.MainFrame.raise_()
        self.main.raise_()

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titlelabel.setText(_translate("MainWindow", "Matrix Solver"))
        self.eqnlabel.setText(_translate("MainWindow", "Enter number of equations:"))
        self.precision.setText(_translate("MainWindow", "Enter the precision:"))
        self.operationbox.setItemText(0, _translate("MainWindow", "Gauss Elimination"))
        self.operationbox.setItemText(1, _translate("MainWindow", "Gauss Jordan"))
        self.operationbox.setItemText(2, _translate("MainWindow", "LU Decomposition"))
        self.operationbox.setItemText(3, _translate("MainWindow", "Jacobi"))
        self.operationbox.setItemText(4, _translate("MainWindow", "Gauss Seidel"))
        self.operation.setText(_translate("MainWindow", "Choose the operation:"))
        self.eqnbox.setCurrentText(_translate("MainWindow", "2"))
        self.eqnbox.setItemText(0, _translate("MainWindow", "2"))
        self.eqnbox.setItemText(1, _translate("MainWindow", "3"))
        self.eqnbox.setItemText(2, _translate("MainWindow", "4"))
        self.eqnbox.setItemText(3, _translate("MainWindow", "5"))
        self.eqnbox.setItemText(4, _translate("MainWindow", "6"))
        self.eqnbox.setItemText(5, _translate("MainWindow", "7"))
        self.eqnbox.setItemText(6, _translate("MainWindow", "8"))
        self.eqnbox.setItemText(7, _translate("MainWindow", "9"))
        self.precisionbox.setCurrentText(_translate("MainWindow", "3"))
        self.precisionbox.setItemText(0, _translate("MainWindow", "3"))
        self.precisionbox.setItemText(1, _translate("MainWindow", "4"))
        self.precisionbox.setItemText(2, _translate("MainWindow", "5"))
        self.precisionbox.setItemText(3, _translate("MainWindow", "6"))
        self.precisionbox.setItemText(4, _translate("MainWindow", "7"))
        self.precisionbox.setItemText(5, _translate("MainWindow", "8"))
        self.precisionbox.setItemText(6, _translate("MainWindow", "9"))
        self.precisionbox.setItemText(7, _translate("MainWindow", "10"))
        self.precisionbox.setItemText(8, _translate("MainWindow", "11"))
        self.precisionbox.setItemText(9, _translate("MainWindow", "12"))
        self.precisionbox.setItemText(10, _translate("MainWindow", "13"))
        self.precisionbox.setItemText(11, _translate("MainWindow", "14"))
        self.precisionbox.setItemText(12, _translate("MainWindow", "15"))
        self.precisionbox.setItemText(13, _translate("MainWindow", "16"))
        self.precisionbox.setItemText(14, _translate("MainWindow", "17"))
        self.precisionbox.setItemText(15, _translate("MainWindow", "18"))
        self.precisionbox.setItemText(16, _translate("MainWindow", "19"))
        self.precisionbox.setItemText(17, _translate("MainWindow", "20"))
        self.proceedbtn.setText(_translate("MainWindow", "Proceed"))
        self.scalingbtn.setText(_translate("MainWindow", "Scaling"))
        self.proceedeqnbtn.setText(_translate("MainWindow", "Proceed"))
        self.stepsbtn.setText(_translate("MainWindow", "show steps"))
        self.resultslabel.setText(_translate("MainWindow", "Results"))

        self.operationbox_LU.setItemText(0, _translate("MainWindow", "Downlittle Form"))
        self.operationbox_LU.setItemText(1, _translate("MainWindow", "Crout Form"))
        self.operationbox_LU.setItemText(2, _translate("MainWindow", "Cholesky Form"))
        self.chooseLulabel.setText(_translate("MainWindow", "Choose LU decompisition format"))
        self.proceedbtn_2.setText(_translate("MainWindow", "Proceed"))
        self.numOfIteraions.setText(_translate("MainWindow", "Number of iterations:"))
        self.relativeErrolabel.setText(_translate("MainWindow", "Absolute relative error:"))
        self.initialGuesslabel.setText(_translate("MainWindow", "Initial guess:"))
        self.proceedbtn_3.setText(_translate("MainWindow", "Proceed"))
        self.backButton.setText(_translate("MainWindow", "Back to menu"))
        self.backButtonlu.setText(_translate("MainWindow", "Back to menu"))
        self.backButtoni.setText(_translate("MainWindow", "Back to menu"))
        self.backButtone.setText(_translate("MainWindow", "Back to menu"))
        self.lineareqnsbtn.setText(_translate("MainWindow", "Solve System of linear equations"))
        self.rootbtn.setText(_translate("MainWindow", "Root Finding"))
        self.operationlabel.setText(_translate("MainWindow", "Choose operation"))
        self.eqnlabel_2.setText(_translate("MainWindow", "Enter the equation:"))
        self.precision_2.setText(_translate("MainWindow", "Enter the precision:"))
        self.operation_2.setText(_translate("MainWindow", "Choose the operation:"))
        self.precisionbox_2.setCurrentText(_translate("MainWindow", "3"))
        self.precisionbox_2.setItemText(0, _translate("MainWindow", "3"))
        self.precisionbox_2.setItemText(1, _translate("MainWindow", "4"))
        self.precisionbox_2.setItemText(2, _translate("MainWindow", "5"))
        self.precisionbox_2.setItemText(3, _translate("MainWindow", "6"))
        self.precisionbox_2.setItemText(4, _translate("MainWindow", "7"))
        self.precisionbox_2.setItemText(5, _translate("MainWindow", "8"))
        self.precisionbox_2.setItemText(6, _translate("MainWindow", "9"))
        self.precisionbox_2.setItemText(7, _translate("MainWindow", "10"))
        self.precisionbox_2.setItemText(8, _translate("MainWindow", "11"))
        self.precisionbox_2.setItemText(9, _translate("MainWindow", "12"))
        self.precisionbox_2.setItemText(10, _translate("MainWindow", "13"))
        self.precisionbox_2.setItemText(11, _translate("MainWindow", "14"))
        self.precisionbox_2.setItemText(12, _translate("MainWindow", "15"))
        self.precisionbox_2.setItemText(13, _translate("MainWindow", "16"))
        self.precisionbox_2.setItemText(14, _translate("MainWindow", "17"))
        self.precisionbox_2.setItemText(15, _translate("MainWindow", "18"))
        self.precisionbox_2.setItemText(16, _translate("MainWindow", "19"))
        self.precisionbox_2.setItemText(17, _translate("MainWindow", "20"))
        self.proceedrootbtn.setText(_translate("MainWindow", "Proceed"))
        self.rootopbox.setItemText(0, _translate("MainWindow", "Bisection"))
        self.rootopbox.setItemText(1, _translate("MainWindow", "False position (Regular-falsi)"))
        self.rootopbox.setItemText(2, _translate("MainWindow", "Fixed point iteration"))
        self.rootopbox.setItemText(3, _translate("MainWindow", "Newton Raphson"))
        self.rootopbox.setItemText(4, _translate("MainWindow", "Secant"))
        self.label_5.setText(_translate("MainWindow", "Number of iterations:"))
        self.label_6.setText(_translate("MainWindow", "Absolute relative error:"))
        self.label_2.setText(_translate("MainWindow", "Enter the lower bound (xl):"))
        self.label_3.setText(_translate("MainWindow", "Enter the upper bound (xu):"))
        self.proceedfalsibtn.setText(_translate("MainWindow", "Proceed"))
        self.label_4.setText(_translate("MainWindow", "Enter the first initial guess (x₀):"))
        self.label_7.setText(_translate("MainWindow", "Enter the second initial guess (x₁):"))
        self.proceedsecantbtn.setText(_translate("MainWindow", "Proceed"))
        self.label_8.setText(_translate("MainWindow", "Enter the initial guess (x₀):"))
        self.proceedfixedbtn.setText(_translate("MainWindow", "Proceed"))
        self.backButtonroot.setText(_translate("MainWindow", "Back to menu"))
        self.backButtonsecant.setText(_translate("MainWindow", "Back to menu"))
        self.backButtonfalsi.setText(_translate("MainWindow", "Back to menu"))
        self.backButtonfixed.setText(_translate("MainWindow", "Back to menu"))

    def backButtonShowMenu(self):
        self.setupUi()

    def gotomain(self):
        self.MainFrame.raise_()

    def gotoroot(self):
        self.rootscreen.raise_()

    def btnToggle(self):
        self.scalingState = not self.scalingState
        if self.scalingState:
            self.scalingbtn.setStyleSheet("QPushButton""{""background-color : green;""}")
        else:
            self.scalingbtn.setStyleSheet("QPushButton""{""background-color : red;""}")

    def proceedbtnChangeFrame(self):
        numOfEqn = int(self.eqnbox.currentText())
        self.drawEqns(numOfEqn)
        self.equations.raise_()

    def proceedbtnEqn(self):
        operation = self.operationbox.currentText()
        numOfEqn = int(self.eqnbox.currentText())
        if operation == "Gauss Elimination" or operation == "Gauss Jordan":
            self.showResults()
        elif operation == "LU Decomposition":
            self.LuSelectFrame.raise_()
        elif operation == "Jacobi" or operation == "Gauss Seidel":

            for j in range(0, 2 * numOfEqn):
                temp = j
                if j % 2 == 0:
                    label = QLabel("X" + str(j // 2 + 1).translate(self.SUB) + " =")

                    if j == 2 * numOfEqn - 1:
                        label.setText("X" + str(j // 2 + 1).translate(self.SUB))

                    font = label.font()
                    font.setPointSize(20)
                    label.setFont(font)
                    self.initialGuessgrid.addWidget(label, 0, j)
                else:
                    lineEdit = QLineEdit()
                    lineEdit.setValidator(QDoubleValidator(-0.9, 0.9, 50))
                    lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
                    self.initialGuessgrid.addWidget(lineEdit, 0, j)

            self.iterativeParameters.raise_()

    def showSteps(self):
        precision = int(self.precisionbox.currentText())
        operation = self.operationbox.currentText()

        if operation == "Jacobi" or operation == "Gauss Seidel":
            c = 0
            for i in self.stepsDic:
                self.newLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.newLabel.setFont(QFont("Tahoma", 35))
                self.newLabel.setScaledContents(False)
                self.newLabel.setAlignment(QtCore.Qt.AlignCenter)

                newX = np.array(self.stepsDic[i], dtype='f8')
                result = f"X{str(c).translate(self.SUB)} = " + str(newX) + "\n"
                self.newLabel.setText(result)
                self.verticalLayout.addWidget(self.newLabel)
                c += 1


        elif operation == "Gauss Elimination" or operation == "Gauss Jordan":
            for i in self.stepsDic:
                self.newLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.newLabel.setFont(QFont("Tahoma", 35))
                self.newLabel.setScaledContents(False)
                self.newLabel.setAlignment(QtCore.Qt.AlignCenter)

                a_b = self.stepsDic[i]

                newA = np.array(a_b[0], dtype='f8')
                newB = np.array(a_b[1], dtype='f8')
                result = ""

                for k in range(newA[0].size):
                    result += "|  "
                    for j in range(newA[0].size):
                        newA[k][j] = Precision.sigFigures(precision, newA[k][j])
                        result += str(newA[k][j]) + "   "
                    result += "|  "
                    newB[k] = Precision.sigFigures(precision, newB[k])
                    result += str(newB[k]) + "  "
                    result += "|\n"

                result += i + "\n"
                self.newLabel.setText(result)

                self.verticalLayout.addWidget(self.newLabel)
        elif operation == "LU Decomposition":
            for i in self.stepsDic:

                self.newLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
                self.newLabel.setFont(QFont("Tahoma", 35))
                self.newLabel.setScaledContents(False)
                self.newLabel.setAlignment(QtCore.Qt.AlignCenter)
                result = ""

                print(np.array(self.stepsDic[i]).ndim)

                if np.array(self.stepsDic[i]).ndim == 1:
                    result = i + " = " + str(self.stepsDic[i]) + "\n"
                    self.newLabel.setText(result)
                    self.verticalLayout.addWidget(self.newLabel)
                    continue

                l_u = np.array(self.stepsDic[i], dtype='f8')
                result += i + " = "

                for k in range(l_u[0].size):
                    for j in range(l_u[0].size):
                        l_u[k][j] = Precision.sigFigures(precision, l_u[k][j])

                for k in l_u:
                    result += str(k) + "\n"
                    result += "        "

                self.newLabel.setText(result)
                self.verticalLayout.addWidget(self.newLabel)

        self.backButton2 = QtWidgets.QPushButton()
        font = QtGui.QFont()
        font.setPointSize(20)
        self.backButton2.setFont(font)
        self.backButton2.setObjectName("backButton")
        self.backButton2.setText("Back to menu")
        self.backButton2.clicked.connect(self.backButtonShowMenu)
        self.verticalLayout.addWidget(self.backButton2)
        self.steps.raise_()

    def showResults(self):
        global x
        precision = int(self.precisionbox.currentText())
        operation = self.operationbox.currentText()
        n = int(self.eqnbox.currentText())

        a = np.array([[0 for x in range(n)] for y in range(n)], dtype='f8')
        b = np.array([0 for x in range(n)], dtype='f8')

        for i in range(n):
            for j in range(0, 2 * n, 2):
                if self.grid.itemAtPosition(i, j).widget().text() != '':
                    a[i][j // 2] = float(self.grid.itemAtPosition(i, j).widget().text())

        for i in range(n):
            if self.grid.itemAtPosition(i, 2 * n + 1).widget().text() != '':
                b[i] = float(self.grid.itemAtPosition(i, 2 * n + 1).widget().text())

        start = time.time()  # start runtime of the functions

        if operation == "Gauss Elimination" or operation == "Gauss Jordan":
            # self.equations.hide()
            x = None
            if operation == "Gauss Elimination":
                gaussElimination = GaussElimination(a, b, self.scalingState, precision)
                x = gaussElimination.result
                self.stepsDic = gaussElimination.steps
            else:
                gaussJordan = GaussJordan()
                x = gaussJordan.gaussjordan(a, b, self.scalingState, precision)
                self.stepsDic = gaussJordan.steps


        elif operation == "LU Decomposition":
            # self.LuSelectFrame.hide()

            luOperation = self.operationbox_LU.currentText()
            lu = LU(a, n, b, precision, luOperation)
            lu.ManageLU()
            matrixL = lu.l
            matrixU = lu.u
            x = lu.x
            self.stepsDic = lu.steps

        elif operation == "Jacobi" or operation == "Gauss Seidel":
            # self.iterativeParameters.hide()

            error = None
            strError = self.relativeErrorLineEdit.text()
            if strError == '':
                error = 0
                strError = "0"
            elif strError[0] == 'e':
                strError = "1" + strError
                error = float(strError)
            else:
                error = float(strError)

            numOfItr = int(self.numOfIteraionsLineEdit.text() if self.numOfIteraionsLineEdit.text() != '' else 0)
            initialGuess = np.array([0 for x in range(n)], dtype='f8')
            for i in range(n):
                if self.initialGuessgrid.itemAtPosition(0, i).widget().text() != '' and i % 2 == 1:
                    initialGuess[i] = float(self.initialGuessgrid.itemAtPosition(0, i).widget().text())

            iterative = IterativeMethods(n, a, b, precision, initialGuess, error, numOfItr)

            if operation == "Jacobi":
                iterative.ManageJacobi()
            else:
                iterative.ManageSeidel()

            x = iterative.x
            self.stepsDic = iterative.steps

        if isinstance(x, str):
            label = QLabel()
            font = label.font()
            font.setPointSize(20)
            label.setFont(font)
            label.setScaledContents(False)
            label.setAlignment(QtCore.Qt.AlignCenter)
            if x == "Invalid":
                label.setText("System has no solution \n(Inconsistent)")
            elif x == "Infinite":
                label.setText("System has Infinite number of solutions \n(Inconsistent)")
            elif x == "Singular":
                label.setText("System has no unique solution \n(Singular)")

            self.ResultsLayout.addWidget(label)
            self.Results.raise_()
            return

        for j in range(0, n):
            label = QLabel("X" + str(j + 1).translate(self.SUB) + " = " + str(x[j]))
            font = label.font()
            font.setPointSize(30)
            label.setFont(font)
            label.setScaledContents(False)
            label.setAlignment(QtCore.Qt.AlignCenter)
            self.ResultsLayout.addWidget(label)

        end = time.time()
        label = QLabel("Runtime = " + str(float(round((end - start) * (10 ** 3), 7))) + " ms")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        label.setScaledContents(False)
        label.setAlignment(QtCore.Qt.AlignCenter)
        self.ResultsLayout.addWidget(label)

        self.Results.raise_()

    def proceedbtnLU(self):
        self.showResults()

    def drawEqns(self, numOfEqn):
        temp = 0
        self.grid = QtWidgets.QGridLayout()
        self.grid.setContentsMargins(20, 0, 20, 150)

        for i in range(0, numOfEqn):
            for j in range(0, 2 * numOfEqn):
                temp = j
                if j % 2 == 1:
                    label = QLabel("X" + str(j // 2 + 1).translate(self.SUB) + " +")

                    if j == 2 * numOfEqn - 1:
                        label.setText("X" + str(j // 2 + 1).translate(self.SUB))

                    font = label.font()
                    font.setPointSize(20)
                    label.setFont(font)
                    self.grid.addWidget(label, i, j)
                else:
                    lineEdit = QLineEdit()
                    lineEdit.setValidator(QDoubleValidator(-0.9, 0.9, 50))
                    lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
                    lineEdit.setPlaceholderText("a" + str(i * numOfEqn + j // 2 + 1).translate(self.SUB))
                    self.grid.addWidget(lineEdit, i, j)

            label = QLabel("= ")
            font = label.font()
            font.setPointSize(20)
            label.setFont(font)
            lineEdit = QLineEdit()
            lineEdit.setValidator(QDoubleValidator(-0.9, 0.9, 50))
            lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n""color: rgb(0, 0, 0);")
            lineEdit.setPlaceholderText("b" + str(i + 1).translate(self.SUB))
            self.grid.addWidget(label, i, temp + 1)
            self.grid.addWidget(lineEdit, i, temp + 2)

        self.equations.setLayout(self.grid)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = GUI()
    sys.exit(app.exec_())
