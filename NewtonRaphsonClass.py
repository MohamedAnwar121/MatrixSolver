import copy
from sympy import *
from Precision import *

class NewtonRaphsonClass:
    def __init__(self, expr, initial_guess, noOfSig, tolerance=1e-5, iter=50):
        self.steps = {}
        self.x = initial_guess
        self.sig = noOfSig
        self.errorTolerance = tolerance
        self.nIteration = iter
        self.expr = expr
        self.status="converge"
        self.steps["initial guess"] = initial_guess
        self.root = initial_guess

    def f(self, xn):
        x = Symbol('x')
        mainExpr = sympify(self.expr)
        mainExpr = lambdify(x, mainExpr)
        return mainExpr(xn)

    # Defining derivative of function
    def g(self, xn):
        x = Symbol('x')
        mainExpr = sympify(self.expr)
        diffExpr = mainExpr.diff(x)
        diffExpr = lambdify(x, diffExpr)
        return diffExpr(xn)

    # Implementing Newton Raphson Method
    def newtonRaphson(self):

        try:
            step = 1
            condition = True
            while condition:
                x0 = copy.copy(self.x)

                if self.g(x0) == 0.0:
                    self.root = "can't find root"
                    return

                x1 = Precision.sigFigures(self.sig, x0 - self.f(x0) / self.g(x0))
                self.x = copy.copy(x1)
                self.steps["iteration " + str(step)] = copy.copy(x1)
                step = step + 1
                self.root = x1
                if step > self.nIteration:
                    self.status="diverge"
                    break

                if x1 != 0:
                    ea = abs((x1 - x0) / x1);
                    if (ea <= self.errorTolerance):
                        self.root = x1
                        self.steps["root: "] = copy.copy(x1)
                        return

        except:
            self.root = "can't find root"
            return

# if __name__ == "__main__":

#     myRaf = NewtonRaphsonClass("(x**3)-(0.165*(x**2))+(3.993*(10**-4))",0.05,6,1e-5,10)
#     myRaf.newtonRaphson()
#     print(myRaf.root)
#     print(myRaf.steps)