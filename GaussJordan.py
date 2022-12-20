import time
import numpy as np


class GaussJordan:
    def gaussjordan(self, a, b, sigfig=5):
        start = time.time()
        a = np.array(a, float)
        b = np.array(b, float)
        al = a.copy()
        bl = b.copy()
        n = len(b)
        s = np.zeros(n)
        ans = np.zeros(n)
        det = np.linalg.det(a)
        self.steps = {

        }
        print(round(det, sigfig))
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

            if np.fabs(s[i]) < 1e-18:
                return "singular"

        # elimination
        for k in range(n):
            x = a[k, k] / s[k]
            y = k

            # partial pivoting
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
                self.steps[step] = [al.copy(), bl.copy()]
                al = a.copy()
                bl = b.copy()

            # dividing all row elements by pivot
            pivot = a[k, k]
            if np.fabs(pivot) < 1e-18:
                return "singular"
            for j in range(n):
                a[k, j] = round(a[k, j] / pivot, sigfig)
            b[k] = round(b[k] / pivot, sigfig)
            print("R", (k + 1), "= R", (k + 1), "/", pivot)
            step = f"R{k + 1} = R{k + 1} / {pivot}"
            self.steps[step] = [al.copy(), bl.copy()]
            al = a.copy()
            bl = b.copy()

            # forward and backward elimination
            for i in range(n):
                if i == k or a[i, k] == 0: continue
                factor = a[i, k]
                for j in range(k, n):
                    a[i, j] = round(a[i, j] - (factor * a[k, j]), sigfig)
                b[i] = round(b[i] - (factor * b[k]), sigfig)
                print("R", (i + 1), "= R", (i + 1), "-", factor, "* R", (k + 1))
                step = f"R{i + 1}  = R{i + 1} - {factor} * R{k + 1}\n"
                self.steps[step] = [al.copy(), bl.copy()]
                al = a.copy()
                bl = b.copy()
                print(a)
                print(b)
        end = (time.time())
        print((end - start) * (10 ** 3), "ms")
        # print(b)
        for i in range(n):
            if np.fabs(a[i, i] < 1e-18):
                return "inconsistent system"
            ans[i] = b[i]
        step = "final matrix\n"
        self.steps[step] = [al, bl]
        print(self.steps)
        return ans
