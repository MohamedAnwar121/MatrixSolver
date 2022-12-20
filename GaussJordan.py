import time
import numpy as np


def gaussjordan(a, b, sigfig=5):
    start = time.time()
    a = np.array(a, float)
    b = np.array(b, float)
    n = len(b)
    s = np.zeros(n)
    ans = np.zeros(n)
    det = np.linalg.det(a)
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
            print("singular")
            return

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

        # dividing all row elements by pivot
        pivot = a[k, k]
        if np.fabs(pivot) < 1e-18:
            print("singular")
            return
        for j in range(n):
            a[k, j] = round(a[k, j] / pivot, sigfig)
        b[k] = round(b[k] / pivot, sigfig)
        print("R", (k+1), "= R", (k+1), "/", pivot)

        # forward and backward elimination
        for i in range(n):
            if i == k or a[i, k] == 0: continue
            factor = a[i, k]
            for j in range(k, n):
                a[i, j] -= factor * a[k, j]
            b[i] -= factor * b[k]
            print("R", (i + 1), "= R", (i + 1), "-", factor, "* R", (k+1))
            print(a)
            print(b)
    end = (time.time())
    print((end - start) * (10 ** 3), "ms")
    # print(a)
    # print(b)
    for i in range(n):
        if np.fabs(a[i, i] < 1e-18):
            print("inconsistent system")
            return
        ans[i] = b[i]

    return ans


