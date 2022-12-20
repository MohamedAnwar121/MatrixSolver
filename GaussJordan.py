import time
import numpy as np
from Precision import *


class GaussJordan:
    def gaussjordan(self, a, b, scaling, sigfig=5):
        start = time.time()
        n = len(b)
        s = np.zeros(n)
        ans = np.zeros(n)
        det = np.linalg.det(a)
        self.steps = {
            "Initial Matrix": [a.copy(), b.copy()]
        }
        # check for singularity
        # if np.fabs(det) < 1e-18:
        #     print("singular")
        #     return
        # scaling
        for i in range(n):
            s[i] = a[i, 0]
            for j in range(1, n):
                if np.fabs(a[i, j]) > np.fabs(s[i]):
                    s[i] = a[i, j]

            # if np.fabs(s[i]) < 1e-18:
            #     return "Invalid"

        # elimination
        for k in range(n):

            # partial pivoting
            if scaling:
                if np.fabs(s[i]) < 1e-18:
                    x = a[k, k]
                else:
                    x = a[k, k] / s[k]
                y = k
                for i in range(k + 1, n):
                    if np.fabs(a[i, k] / s[i]) > np.fabs(x):
                        x = a[i, k] / s[i]
                        y = i
                if y != k:
                    for j in range(k, n):
                        a[k, j], a[y, j] = a[y, j], a[k, j]
                    b[k], b[y] = b[y], b[k]
                    s[k], s[y] = s[y], s[k]
                    step = f"R{y + 1} <-> R{k + 1}\n"
                    self.steps[step] = [a.copy(), b.copy()]
            else:
                x = a[k, k]
                y = k
                for i in range(k + 1, n):
                    if np.fabs(a[i, k]) > np.fabs(x):
                        x = a[i, k]
                        y = i
                if y != k:
                    for j in range(k, n):
                        a[k, j], a[y, j] = a[y, j], a[k, j]
                    b[k], b[y] = b[y], b[k]
                    step = f"R{y + 1} <-> R{k + 1}\n"
                    self.steps[step] = [a.copy(), b.copy()]

            # dividing all row elements by pivot
            pivot = a[k, k]
            if np.fabs(pivot) < 1e-18 and np.fabs(b[k]) < 1e-18:
                return "Infinite"
            elif np.fabs(pivot) < 1e-18 and np.fabs(b[k]) >= 1e-18:
                return "Invalid"
            for j in range(n):
                a[k, j] = Precision.sigFigures(sigfig, a[k, j] / pivot)
            b[k] = Precision.sigFigures(sigfig, b[k] / pivot)
            print("R", (k + 1), "= R", (k + 1), "/", pivot)
            step = f"R{k + 1} = R{k + 1} / {pivot}"
            self.steps[step] = [a.copy(), b.copy()]

            # forward and backward elimination
            for i in range(n):
                if i == k or a[i, k] == 0:
                    continue
                factor = a[i, k]
                for j in range(k, n):
                    a[i, j] = Precision.sigFigures(sigfig, a[i, j] - (factor * a[k, j]))
                b[i] = Precision.sigFigures(sigfig, b[i] - (factor * b[k]))
                print("R", (i + 1), "= R", (i + 1), "-", factor, "* R", (k + 1))
                step = f"R{i + 1}  = R{i + 1} - {factor} * R{k + 1}\n"
                self.steps[step] = [a.copy(), b.copy()]
                print(a)
                print(b)
        # print(b)
        for i in range(n):
            if np.fabs(a[i, i]) < 1e-18 and np.fabs(b[i]) < 1e-18:
                return "Infinite"
            elif np.fabs(a[i, i]) < 1e-18 and np.fabs(b[i]) >= 1e-18:
                return "Invalid"
            ans[i] = b[i]
        step = "Final Matrix\n"
        self.steps[step] = [a.copy(), b.copy()]
        # print(self.steps)
        return ans
