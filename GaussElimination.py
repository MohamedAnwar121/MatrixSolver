import numpy as np
from Precision import *


class GaussElimination:

    def __init__(self, a, b, scaling, precision, tol=1e-18):
        self.result = self.gaussElimination(a, b, scaling, precision, tol=1e-18)

    def gaussElimination(self, a, b, scaling, precision, tol=1e-18):
        n = a[0].size
        s = np.zeros(n)
        self.sigFig = precision
        self.getMaxInCol(a, s)
        x = np.zeros(n)

        self.steps = {
            "Initial Matrix": [a.copy(), b.copy()]
        }

        self.eliminate(a, b, x, s, tol, scaling)

        temp = self.substitute(a, b, x)
        if isinstance(temp, str):
            return temp

        string = "Final Matrix\n"
        self.steps[string] = [a.copy(), b.copy()]
        return x

    def getMaxInCol(self, a, s):
        for i in range(a[0].size):
            s[i] = abs(a[i][0])
            for j in range(1, a[0].size):
                if abs(a[i][j]) > s[i]:
                    s[i] = a[i][j]

    def eliminate(self, a, b, x, s, tol, scaling):
        n = a[0].size
        for k in range(0, n - 1):
            if scaling:
                self.pivotWithScaling(a, b, s, k)
            else:
                self.pivotWithoutScaling(a, b, k)

            if a[k][k] < tol:
                continue

            for i in range(k + 1, n):

                factor = Precision.sigFigures(self.sigFig, a[i][k] / a[k][k])

                for j in range(k, n):
                    a[i][j] -= Precision.sigFigures(self.sigFig, a[k][j] * factor)
                b[i] = Precision.sigFigures(self.sigFig, b[i] - factor * b[k])

                string = f"R{i + 1} = R{i + 1} - {factor} * R{k + 1}\n"
                self.steps[string] = [a.copy(), b.copy()]


    def substitute(self, a, b, x):
        n = a[0].size

        if a[n - 1][n - 1] == 0 and b[n - 1] == 0:
            return "Infinite"
        elif a[n - 1][n - 1] == 0:
            return "Invalid"

        x[n - 1] = Precision.sigFigures(self.sigFig, b[n - 1] / a[n - 1][n - 1])
        for i in range(n - 2, -1, -1):
            sm = 0
            for j in range(i + 1, n):
                sm += Precision.sigFigures(self.sigFig, a[i][j] * x[j])

            if a[i][i] == 0 and b[i] == 0:
                return "Infinite"
            elif a[i][i] == 0:
                return "Invalid"

            x[i] = Precision.sigFigures(self.sigFig, (b[i] - sm) / a[i][i])

    def pivotWithScaling(self, a, b, s, k):
        n = a[0].size
        p = k

        dummy = 0
        big = abs(a[k][k] / s[k])
        for i in range(k + 1, n):
            if s[i] != 0:
                dummy = abs(a[i][k] / s[i])
            else:
                continue
            if dummy > big:
                big = dummy
                p = i

        if p != k:
            for j in range(k, n):
                a[k][j], a[p][j] = a[p][j], a[k][j]

            b[p], b[k] = b[k], b[p]
            s[p], s[k] = s[k], s[p]

            string = f"R{k + 1} <-> R{p + 1}\n"
            self.steps[string] = [a.copy(), b.copy()]

    def pivotWithoutScaling(self, a, b, k):
        n = a[0].size
        p = k

        big = abs(a[k][k])
        for i in range(k + 1, n):
            dummy = abs(a[i][k])
            if dummy > big:
                big = dummy
                p = i

        if p != k:
            for j in range(k, n):
                a[k][j], a[p][j] = a[p][j], a[k][j]
            b[p], b[k] = b[k], b[p]

            self.steps[string] = [a.copy(), b.copy()]
