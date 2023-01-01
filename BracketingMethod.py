from math import *
from Precision import *


class BracketingMethod:

    def __init__(self, noOfSig, xl, xu, exp, es=1e-5, iterations=50):
        self.sig = noOfSig
        self.steps = {}
        self.es = es
        self.nIteration = iterations
        self.xl = xl
        self.xu = xu
        self.exp = "BracketingMethod.f = lambda self,x : " + exp
        exec(self.exp)

    def func(self, x):
        res = self.f(x)
        if res == inf:
            raise Exception
        return Precision.sigFigures(self.sig, res)

    def bisection(self):
        xr = 0
        ea = 0
        xr_old = 0
        Fxl = self.func(self.xl)
        Fxu = self.func(self.xu)
        xlold=self.xl
        xuold=self.xu
        # self.steps['iteration 0'] = [self.xl, self.xu]
        if Fxl * Fxu > 0:
            return 'No root in this interval'
        for i in range(self.nIteration):
            xr_old = xr
            xr = Precision.sigFigures(self.sig, (self.xl + self.xu) / 2)
            if i > 0:
                if xr != 0:
                    ea = abs((xr - xr_old) / xr)
            Fxr = self.func(xr)
            Fxl = self.func(self.xl)
            Fxu = self.func(self.xu)
            if Fxl * Fxr < 0:
                self.xu = xr
            elif Fxl * Fxr > 0:
                self.xl = xr
            else:
                break
            self.steps[f'iteration {i + 1}'] = [self.xl, self.xu, xr,xlold,xuold]
            if ea < self.es and i > 0:
                break
        return xr

    # "false position method"
    def falsePosition(self):
        xr = 0
        ea = 0
        xr_old = 0
        xlold=self.xl
        xuold=self.xu
        Fxl = self.func(self.xl)
        Fxu = self.func(self.xu)
        # self.steps['iteration 0'] = [self.xl, self.xu]
        if Fxl * Fxu > 0:
            return 'No root in this interval'
        for i in range(self.nIteration):
            xr_old = xr
            if abs(Fxu - Fxl) < 1e-18:
                print(abs(Fxu - Fxl))
                return xr
            xr = Precision.sigFigures(self.sig, self.xu - Fxu * (self.xu - self.xl) / (Fxu - Fxl))
            Fxr = self.func(xr)
            if i > 0:
                if xr != 0:
                    ea = abs((xr - xr_old) / xr)
            Fxr = self.func(xr)
            Fxl = self.func(self.xl)
            Fxu = self.func(self.xu)

            if Fxr == 0:
                break
            elif Fxl * Fxr < 0:
                self.xu = xr
                Fxu = Fxr
            elif Fxl * Fxr > 0:
                self.xl = xr
                Fxl = Fxr
            else:
                return "false position method fails"
            if ea < self.es and i > 0:
                break
            self.steps[f'iteration {i + 1}'] = [self.xl, self.xu, xr,xlold,xuold]
        return xr

    def manager(self, function):
        try:
            if function == 'bisection':
                return self.bisection()
            elif function == 'falsePosition':
                return self.falsePosition()
        except:
            return "can't find root"
