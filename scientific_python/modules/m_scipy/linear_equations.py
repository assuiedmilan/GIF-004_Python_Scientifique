import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([[2, 3, 4], [3, 5, -4], [4, 7, -2]])
b = np.array([53, 2, 31])

lu, piv = lu_factor(A)
x = lu_solve((lu, piv), b)

print(x)