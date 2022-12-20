from abc import ABC, abstractmethod
from Precision import *


class IterativeMethods:

    def __init__(self, n, a, b, noOfSig, initialGuess, tol=1e-5, iterations=50):
        self.numberOfVariables = n
        self.sig = noOfSig
        self.steps = {}
        self.a = a
        self.b = b
        self.errorTolerance = tol
        self.nIteration = iterations
        self.x = initialGuess
        self.steps["initial guess"] = self.x.copy()

    def isDDM(self):

        for i in range(0, self.numberOfVariables):
            sum = 0
            for j in range(0, self.numberOfVariables):
                sum = sum + abs(self.a[i][j])
            sum = sum - abs(self.a[i][i])
            if abs(self.a[i][i]) < sum:
                return False
        return True

    # get the max error in x
    @abstractmethod
    def calc_error(x_new, x):
        e = -1
        for i in range(0, len(x)):
            if x_new[i] == 0:
                return -1
            e = max(abs((x_new[i] - x[i]) / x_new[i]), e)
        return e

    def jacobi(self):

        x_new = self.x.copy()
        for j in range(0, self.numberOfVariables):
            d = self.b[j]
            for i in range(0, self.numberOfVariables):
                if (j != i):
                    d -= self.a[j][i] * self.x[i]
            x_new[j] = Precision.sigFigures(self.sig, d / self.a[j][j])
        return x_new

    def seidel(self):

        for j in range(0, self.numberOfVariables):
            d = self.b[j]
            for i in range(0, self.numberOfVariables):
                if (j != i):
                    d -= self.a[j][i] * self.x[i]
            self.x[j] = Precision.sigFigures(self.sig, d / self.a[j][j])
        return self.x

    # loop run for nIteration times and break if the given errorTolerance is achieved
    def ManageJacobi(self):

         try:
            for i in range(0, self.nIteration):
                x_new = self.jacobi()
                error = IterativeMethods.calc_error(x_new, self.x)
                self.x = x_new
                self.steps["iteration " + str(i)] = self.x
                if error < self.errorTolerance or error == -1:
                    break
         except:
            self.x = "Invalid"

    # loop run for nIteration times and break if the given errorTolerance is achieved
    def ManageSeidel(self):

         try:
            for i in range(0, self.nIteration):
                x_prev = self.x.copy()
                x_new = self.seidel()
                error = IterativeMethods.calc_error(x_new, x_prev)
                self.x = x_new
                self.steps["iteration " + str(i)] = self.x.copy()
                if error < self.errorTolerance or error == -1:
                    break
         except:
            self.x = "Invalid"

