import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[0, 0, 0]])
C = np.concatenate((A,B.T), axis=1)
# D = np.linalg.inv(A)*B
print (C)
print(np.linalg.matrix_rank(A, 0.0001), np.linalg.matrix_rank(C, 0.0001))
# print(np.linalg.lstsq(A, B, rcond=None))
print(np.linalg.solve(A, B))
# print(D)

# Я не знаю, почему у меня не считается Х.