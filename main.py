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
    a = np.array([[1, 2],
                  [7, 8]], dtype='d')
    b = np.array([3, 9], dtype='d')



    print(a)
    gauss = NumericalMethods(a, b, True, 4)
    x = gauss.result

    # UiMainWindow()
    print(x)


if __name__ == '__main__':
    main()
    # gui()
