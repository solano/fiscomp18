import numpy as np
import scipy.linalg as la
from sympy import Matrix, N
from mpmath import findroot

A1 = Matrix([[2, 8,10],
               [8, 4, 5],
               [10,5, 7]])
A2 = Matrix([[10, -2,  3,  2],
               [-2, 10, -3,  4],
               [ 3, -3,  6,  3],
               [ 2,  4,  3,  6]])
A3 = Matrix([[-10,   2,  -3,  -2,  -1],
               [  2, -10,   3,  -4,  -2],
               [ -3,   3,  -6,  -3,  -3],
               [ -2,  -4,  -3,  -6,  -4],
               [ -1,  -2,  -3,  -4, -13]])

print(N(list(A1.eigenvals().keys())[0], 20))
print(N(list(A2.eigenvals().keys())[2], 20))

pol = A3.charpoly()
print(findroot(pol,-17,tol=1e-15))
