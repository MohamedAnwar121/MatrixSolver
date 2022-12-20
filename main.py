import numpy as np
from GaussElimination import NumericalMethods

from GUI import *
from PyQt5.QtWidgets import *
import sys


def gui():
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()



def main():
    a = np.array([[1, 1, 2],
                  [1, 6, 22],
                  [2, 4, 3]], dtype='d')
    b = np.array([11, 6, 5], dtype='d')



    print(a)
    x = NumericalMethods.GaussElimination(a, b, True)

    # UiMainWindow()
    print(x)


if __name__ == '__main__':
    # main()
    gui()
