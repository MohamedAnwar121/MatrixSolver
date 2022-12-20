import math
from cmath import e
from Precision import *


class LU:

    def __init__(self, a, n, b, precision, type):
        self.n = n
        self.a = a
        self.b = b
        self.sig = precision
        self.type = type
        self.l = []
        self.u = []
        self.x = [0 for x in range(self.n)]
        self.doolittlelower = [[0 for x in range(n)] for y in range(n)]
        self.doolittleupper = [[0 for x in range(n)] for y in range(n)]
        self.choleskylower = [[0 for x in range(self.n)] for y in range(self.n)]
        self.choleskyUpper = [[0 for x in range(self.n)] for y in range(self.n)]
        self.croutlower = [[0 for x in range(n)] for y in range(n)]
        self.croutupper = [[0 for x in range(n)] for y in range(n)]
        self.steps = {}

    def ManageLU(self):

        try:
            if self.type == "Downlittle Form":
                self.luDoolittleDecomposition()
            elif self.type == "Crout Form":
                self.crout()
            elif self.type == "Cholesky Form":
                self.luCholesky_Decomposition()
        except:
            self.x = "Invalid"

    def luDoolittleDecomposition(self):


        for i in range(self.n):

            # upper triangle
            for k in range(i, self.n):

                sum = 0
                for j in range(i):
                    sum += (self.doolittlelower[i][j] * self.doolittleupper[j][k])

                self.doolittleupper[i][k] = Precision.sigFigures(self.sig, self.a[i][k] - sum)
                print(self.doolittleupper)

            # upper triangle
            for k in range(i, self.n):
                if i == k:
                    self.doolittlelower[i][i] = 1
                else:
                    sum = 0
                    for j in range(i):
                        sum += (self.doolittlelower[k][j] * self.doolittleupper[j][i])

                    # evaluate
                    self.doolittlelower[k][i] = Precision.sigFigures(self.sig,
                                                                     (self.a[k][i] - sum) / self.doolittleupper[i][i])
                    print(self.doolittlelower)

            self.steps["L" + str(i)] = self.doolittlelower.copy()
            self.steps["U" + str(i)] = self.doolittleupper.copy()

        self.l = self.doolittlelower
        self.u = self.doolittleupper
        self.eliminate(self.doolittlelower, self.doolittleupper)

    def luCholesky_Decomposition(self):

        # Lower Triangular
        for i in range(self.n):
            for j in range(i + 1):
                sum1 = 0

                # summation for diagonals
                if j == i:
                    for k in range(j):
                        sum1 += pow(self.choleskylower[j][k], 2)
                    self.choleskylower[j][j] = Precision.sigFigures(self.sig, math.sqrt(self.a[j][j] - sum1))
                else:

                    # Evaluating
                    for k in range(j):
                        sum1 += (self.choleskylower[i][k] * self.choleskylower[j][k])
                    if self.choleskylower[j][j] > 0:
                        self.choleskylower[i][j] = Precision.sigFigures(self.sig,
                                                                        (self.a[i][j] - sum1) / self.choleskylower[j][
                                                                            j])
            self.steps["L" + str(i)] = self.choleskylower.copy()


        for i in range(self.n):
            for j in range(self.n):
                self.choleskyUpper[j][i] = self.choleskylower[i][j]

        self.l = self.choleskylower
        self.u = self.choleskyUpper
        self.eliminate(self.choleskylower, self.choleskyUpper)
        self.steps["U"] = self.choleskyUpper.copy()

    def crout(self):

        for j in range(self.n):
            self.croutupper[j][j] = 1
            for i in range(j, self.n):
                alpha = float(self.a[i][j])
                for k in range(j):
                    alpha -= self.croutlower[i][k] * self.croutupper[k][j]
                self.croutlower[i][j] = Precision.sigFigures(self.sig, alpha)
            for i in range(j + 1, self.n):
                tempU = float(self.a[j][i])
                for k in range(j):
                    tempU -= self.croutlower[j][k] * self.croutupper[k][i]
                if int(self.croutlower[j][j]) == 0:
                    self.croutlower[j][j] = e - 40
                self.croutupper[j][i] = Precision.sigFigures(self.sig, tempU / self.croutlower[j][j])

            self.steps["L" + str(i)] = self.croutlower.copy()
            self.steps["U" + str(i)] = self.croutupper.copy()

        self.l = self.croutlower
        self.u = self.croutupper
        self.eliminate(self.croutlower, self.croutupper)

    def eliminateL(self, l):

        y = [0 for x in range(self.n)]

        y[0] = Precision.sigFigures(self.sig, self.b[0] / l[0][0])

        for i in range(1, self.n):
            sum = 0
            for j in range(0, i):
                sum += l[i][j] * y[j]

            y[i] = Precision.sigFigures(self.sig, (self.b[i] - sum) / l[i][i])

        return y

    def eliminateU(self, u, y):

        self.x[self.n - 1] = Precision.sigFigures(self.sig, y[self.n - 1] / u[self.n - 1][self.n - 1])
        for i in range(self.n - 2, -1, -1):
            sum = 0
            for j in range(i + 1, self.n):
                sum += u[i][j] * self.x[j]

            self.x[i] = Precision.sigFigures(self.sig, (y[i] - sum) / u[i][i])

        return self.x

    def eliminate(self, l, u):

        y = self.eliminateL(l)
        z = self.eliminateU(u, y)
        self.x = z
