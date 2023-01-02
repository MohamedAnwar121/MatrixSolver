import pyqtgraph as pg
from math import *
import copy
from sympy import *
from Precision import *


class Plot:
    def fx(self, xn, expression):
        x = Symbol('x')
        mainExpr = sympify(expression)
        mainExpr = lambdify(x, mainExpr)
        return mainExpr(xn)

    # Defining derivative of function
    def gx(self, expression, xn):
        x = Symbol('x')
        mainExpr = sympify(expression)
        diffExpr = mainExpr.diff(x)
        diffExpr = lambdify(x, diffExpr)
        print(diffExpr(xn))
        return diffExpr(xn)

    def plotBisection(self, xl, xu, newXr, newXl, newXu, expression):
        graphWidget = pg.PlotWidget()
        boundry_scale = abs((self.fx(xl, expression) - self.fx(xu, expression)) / 5)
        print(boundry_scale)
        x = []
        y = []
        i = xl
        while i <= xu:
            x.append(i)
            i += 0.01
        for i in x:
            y.append(self.fx(i, expression))
        graphWidget.setBackground('w')
        graphWidget.showGrid(x=True, y=True)
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.plot(x, y, pen=pen)
        pen = pg.mkPen(color=(0, 0, 0), width=3)
        y = [self.fx(newXl, expression) - boundry_scale, self.fx(newXu, expression) + boundry_scale]
        x = [newXl, newXl]
        graphWidget.plot(x, y, pen=pen)
        y = [self.fx(newXl, expression) - boundry_scale, self.fx(newXu, expression) + boundry_scale]
        x = [newXu, newXu]
        graphWidget.plot(x, y, pen=pen)
        y = [self.fx(newXl, expression) - boundry_scale, self.fx(newXu, expression) + boundry_scale]
        x = [newXr, newXr]
        graphWidget.plot(x, y, pen=pen)
        return graphWidget

    def plotFixed(self, z, expression):
        graphWidget = pg.PlotWidget()
        x = []
        y = []
        boundry_scale = abs((self.fx(0, expression) - self.fx(100, expression)) / 3)

        for i in range(100):
            x.append(i)
            y.append(self.fx(i, expression))

        graphWidget.setBackground('w')
        graphWidget.showGrid(x=True, y=True)
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.plot(x, pen=pen)
        graphWidget.plot(x, y, pen=pen)
        pen = pg.mkPen(color=(0, 0, 0), width=3)
        b = [min(y), max(y)]
        print(z)
        a = [z, z]
        graphWidget.plot(a, b, pen=pen)
        # y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        # x = [newXu, newXu]
        # graphWidget.plot(x, y, pen=pen)
        return graphWidget

    def plotNewtonSecant(self, expression):
        graphWidget = pg.PlotWidget()
        x = []
        y = []
        boundry_scale = abs((self.gx(expression, 0) - self.gx(expression, 100)) / 3)

        for i in range(-50, 50, 1):
            print(expression)
            print(self.gx(expression, i))
            x.append(i)
            y.append(self.gx(expression, i))

        graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.showGrid(x=True, y=True)
        graphWidget.setXRange(min(x), max(x))
        graphWidget.setYRange(min(y), max(y))
        graphWidget.plot(x, y, pen=pen)
        # y = [self.func(newXl) - boundry_scale, self.func(newXu) + boundry_scale]
        # x = [newXu, newXu]
        # graphWidget.plot(x, y, pen=pen)
        print(x, y)
        return graphWidget

# if __name__ == '__main__':
#     ob = Plot("x+5");
#     print(ob.func(5))
