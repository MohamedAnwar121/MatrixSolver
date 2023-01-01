import pyqtgraph as pg


class Plot:

    @staticmethod
    def plotBisection(f, xl, xu, newXr, newXl, newXu):
        graphWidget = pg.PlotWidget()
        boundry_scale = abs((f(xl) - f(xu)) / 5)
        print(boundry_scale)
        x = []
        y = []
        i = xl
        while i <= xu:
            x.append(i)
            i += 0.01
        for i in x:
            y.append(f(i))
        graphWidget.setBackground('w')
        pen = pg.mkPen(color=(0, 0, 0), width=5)
        graphWidget.plot(x, y, pen=pen)
        pen = pg.mkPen(color=(0, 0, 0), width=3)
        y = [f(newXl) - boundry_scale, f(newXu) + boundry_scale]
        x = [newXl, newXl]
        graphWidget.plot(x, y, pen=pen)
        y = [f(newXl) - boundry_scale, f(newXu) + boundry_scale]
        x = [newXu, newXu]
        graphWidget.plot(x, y, pen=pen)
        y = [f(newXl) - boundry_scale, f(newXu) + boundry_scale]
        x = [newXr, newXr]
        graphWidget.plot(x, y, pen=pen)
        return graphWidget
