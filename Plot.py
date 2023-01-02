import pyqtgraph as pg
from math import *

class Plot:

    def __init__(self,exp):
        self.exp = "Plot.f = lambda self,x : " + exp
        exec(self.exp)


    def func(self, x):
        return self.f(x)

    def plotBisection(self, xl, xu, newXr, newXl, newXu):
        graphWidget = pg.PlotWidget()
        boundry_scale = abs((self.func(xl) - self.func(xu)) / 5)
        print(boundry_scale)
        x = []
        y = []
        i = xl
        while i <= xu:
            x.append(i)
            i += 0.01
        for i in x:
            y.append(self.func(i))
        graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.plot(x, y, pen=pen)
        pen = pg.mkPen(color=(0, 0, 0), width=3)
        y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        x = [newXl, newXl]
        graphWidget.plot(x, y, pen=pen)
        y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        x = [newXu, newXu]
        graphWidget.plot(x, y, pen=pen)
        y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        x = [newXr, newXr]
        graphWidget.plot(x, y, pen=pen)
        return graphWidget

    def plotFixed(self,z):
        graphWidget = pg.PlotWidget()
        x = []
        y = []
        boundry_scale = abs((self.func(0) - self.func(100)) / 3)

        for i in range(100):
            x.append(i)
            y.append(self.func(i))

        graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.plot(x,pen=pen)
        graphWidget.plot(y,pen=pen)
        pen = pg.mkPen(color=(0, 0, 0), width=3)
        b = [min(y), max(y)]
        print(z)
        a = [z, z]
        graphWidget.plot(a, b, pen=pen)
        # y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        # x = [newXu, newXu]
        # graphWidget.plot(x, y, pen=pen)
        return graphWidget


# if __name__ == '__main__':
#     ob = Plot("x+5");
#     print(ob.func(5))

