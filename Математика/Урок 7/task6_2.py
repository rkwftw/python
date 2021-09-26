import numpy as np
import matplotlib.pyplot as plt

A = np.array([[1, 2, -1], [3, -4, 0], [8, -5, 2], [2, 0, -5], [11, 4, -7]], float)
B = np.array([1, 7, 12, 7, 15])
print(np.linalg.lstsq(A, B, rcond=None))


