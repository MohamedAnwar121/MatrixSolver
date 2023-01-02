from math import *
import copy
from matplotlib import pyplot as plt
import numpy as np
from Precision import *


class secantmethod:
    def __init__(self, exp, initial_guess1, initial_guess2, noOfSig, tolerance=1e-5, iter=50):
        self.steps = {}
        self.x0 = initial_guess1
        self.x1 = initial_guess2
        self.sigfig = noOfSig
        self.e = tolerance
        self.N = iter
        self.ea = 0
        self.status = "converge"
        self.exp = "secantmethod.f = lambda self,x : " + exp
        exec(self.exp)

    def func(self, x):
        res = self.f(x)
        if res == inf:
            raise Exception
        return Precision.sigFigures(self.sigfig, res)

    def secant(self):
        try:
            x0 = Precision.sigFigures(self.sigfig, self.x0)
            x1 = Precision.sigFigures(self.sigfig, self.x1)
            x2 = x1
            print('\n\n*** SECANT METHOD IMPLEMENTATION ***')
            step = 1
            condition = True
            while condition:
                if self.func(x0) == self.func(x1):
                    print('Divide by zero error!')
                    return "can't find root"

                x2 = Precision.sigFigures(self.sigfig,
                                          (x0 - (x1 - x0) * self.func(x0) / (self.func(x1) - self.func(x0))))
                if x2 != 0:
                    self.ea = abs((x2 - x1) / x2)
                print(f'Iteration-{step}, x2 = {x2} and f(x2) = {self.func(x2)} , EPS = {self.ea}')
                self.steps[f'iteration {step}'] = [x0, x1, x2, float(round(self.ea, 7))]
                x0 = x1
                x1 = x2
                step = step + 1

                if step > self.N:
                    self.status = "diverge"
                    print('Not Convergent!')
                    return x2

                condition = abs(self.ea) > self.e
            print(f'\n Required root is: {x2}')
            return x2

        except:
            return "can't find root"

# x0 = float(0.5)
# x1 = float(1)
# e = float(5 / 100)
# # N = int()
# s=secantmethod("x**2-2",x0,x1,5,e)
# # Starting Secant Method
# print(s.secant())
