from math import *
import copy
from matplotlib import pyplot as plt
import numpy as np
from Precision import *


class fixedPoint:

    def __init__(self, exp, initial_guess, noOfSig, tolerance=1e-5, iter=50):
        self.steps = {}
        self.x = initial_guess
        self.sig = noOfSig
        self.errorTolerance = tolerance
        self.nIteration = iter
        self.exp = "fixedPoint.f = lambda self,x : " + exp
        exec(self.exp)
        self.steps["initial guess"] = initial_guess

    def func(self, x):
        res = self.f(x)
        if res == inf:
            raise Exception
        return Precision.sigFigures(self.sig, res)

    def fixedPt(self):

        try:
            xr = copy.copy(self.x)
            xr_old = 0;

            for i in range(self.nIteration):
                xr_old = copy.copy(xr)
                xr = self.func(xr_old)
                print(xr)
                self.steps["iteration " + str(i)] = copy.copy(xr)

                if xr != 0:
                    ea = abs((xr - xr_old) / xr)

                    if ea <= self.errorTolerance:
                        self.steps["root: "] = copy.copy(xr)
                        return;

            self.steps["root: "] = copy.copy(xr)

        except:
            return "can't find root"

# if name == "__main__":

#     ob = fixedPoint("1 / sqrt(1+x)",1,6)
#     ob.fixedPt()
#     print(ob.steps)


# x = np.linspace(-5,5,100)
# z1 =[]
# z2 =[]
# for i in range(50):
#     z1.append(i)
#     z2.append(ob.func(i))
# plt.plot(z1)
# plt.plot(z2)
# plt.show()


# PLOT
# x = np.linspace(-5,5,100)

# # the function, which is y = x^2 here
# y = x
# y2 = x ** 2 - 2
# # setting the axes at the centre
# fig = plt.figure()
# ax = fig.add_subplot(1, 1, 1)
# ax.spines['left'].set_position('center')
# ax.spines['bottom'].set_position('zero')
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# ax.xaxis.set_ticks_position('bottom')
# ax.yaxis.set_ticks_position('left')

# # plot the function
# plt.plot(x,y, 'r')
# plt.plot(x,y2,'r')
# plt.show()
