import numpy as np


class NumericalMethods:

    def GaussElimination(self, a, b, scaling, precision, er=0, tol=1e-18):
        n = a[0].size
        s = np.zeros(n)
        self.getMaxInCol(a, s)
        x = np.zeros(n)

        self.m = {
            "": a.copy()
        }

        print(a)
        self.eliminate(a, b, x, s, er, tol, scaling)
        if er != -1:
            if self.substitute(a, b, x) == "Singular":
                return "Singular"
        else:
            return "Singular"
        return x

    def getMaxInCol(self, a, s):
        for i in range(a[0].size):
            s[i] = abs(a[i][0])
            for j in range(1, a[0].size):
                if abs(a[i][j]) > s[i]:
                    s[i] = a[i][j]

    def eliminate(self, a, b, x, s, er, tol, scaling):
        n = a[0].size
        for k in range(0, n - 1):
            if scaling:
                self.pivotWithScaling(a, b, s, k)
            else:
                self.pivotWithoutScaling(a, b, k)

            if abs(a[k][k]) < tol:
                er = -1
                return

            for i in range(k + 1, n):
                factor = a[i][k] / a[k][k]

                for j in range(k, n):
                    a[i][j] -= float(round(a[k][j] * factor, 5))
                b[i] = b[i] - factor * b[k]
                print(a)
                print(f"R{i + 1} - {factor} * R{k + 1}\n")

                s = f"R{i + 1} - {factor} * R{k + 1}\n"
                self.m[s] = a.copy()

        if abs(a[n - 1][n - 1]) < tol:
            er = -1

    def substitute(self, a, b, x):
        n = a[0].size

        if a[n - 1][n - 1] == 0:
            return "Singular"

        x[n - 1] = round(b[n - 1] / a[n - 1][n - 1], 5)
        for i in range(n - 2, -1, -1):
            sm = 0
            for j in range(i + 1, n):
                sm += a[i][j] * x[j]

            if a[i][i] == 0:
                return "Singular"

            x[i] = round((b[i] - sm) / a[i][i], 5)

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

            print(a, )
            print(f"R{k + 1} <-> R{p + 1}\n")
            s = f"R{k + 1} <-> R{p + 1}\n"
            self.m[s] = a.copy()

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

            print(a, )
            print(f"R{k + 1} <-> R{p + 1}\n")
            s = f"R{k + 1} <-> R{p + 1}\n"
            self.m[s] = a.copy()
