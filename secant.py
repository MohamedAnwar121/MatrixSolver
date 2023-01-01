from math import *
import copy
from matplotlib import pyplot as plt
import numpy as np
from Precision import *


class secantmethod:
    def __init__(self, exp, initial_guess1,initial_guess2, noOfSig, tolerance=1e-5, iter=50):
        self.steps = {}
        self.x0 = initial_guess1
        self.x1 = initial_guess2
        self.sigfig = noOfSig
        self.e = tolerance
        self.N = iter
        self.exp = "secantmethod.f = lambda self,x : " + exp
        exec(self.exp)
        self.steps["initial guess 1"] = initial_guess1
        self.steps["initial guess 2"] = initial_guess2

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
                if self.func(x0) - self.func(x1) < 1e-18:
                    print('Divide by zero error!')
                    break

                x2 = Precision.sigFigures(self.sigfig, (x0 - (x1 - x0) * self.func(x0) / (self.func(x1) - self.func(x0))))
                print(f'Iteration-{step}, x2 = {x2} and f(x2) = {self.func(x2)} , EPS = {(x2 - x1) / x2}')
                x0 = x1
                x1 = x2
                step = step + 1

                if step > self.N:
                    print('Not Convergent!')
                    break

                condition = abs((x1 - x0) / x1) > e
            print(f'\n Required root is: {x2}')

        except:
            return "can't find root"
