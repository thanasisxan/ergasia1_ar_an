import numpy as np

A1 = np.array([[2, 1, 5],
               [4, 4, -4],
               [1, 3, 1]])


def get_LUp(A):
    n = len(A)
    A = np.asarray(A, float)
    p = np.eye(n)
    for k in range(0, n-1):
        print("k:", k)
        maxdiag = np.max(abs(A[k:, k]))
        m = int(np.where(A == maxdiag)[0][0])
        m = m + k
        if k > 0:
            m -= 1
        if A[m, k] != 0:
            if m != k:
                A[[k, m]] = A[[m, k]]
                p[[k, m]] = p[[m, k]]
            A[k + 1:, k] = np.divide(A[k + 1:, k], A[k, k+1])
            A[k + 1:, k + 1:] = np.subtract(A[k + 1:, k + 1:], np.multiply(A[k + 1:, k], A[k, k + 1:]))
    L = np.tril(A, -1) + np.eye(n, n)
    U = np.triu(A)
    return L, U, p, A


(L1, U1, p1, A2) = get_LUp(A1)
