import numpy as np
import scipy.linalg


A = np.array([[1, 2, 3], [2, 16, 21], [4, 28, 73,]])
P, L, U = scipy.linalg.lu(A)

print(P)
print(L)
print(U)
print(np.dot(P.transpose(), A) - np.dot(L, U))
