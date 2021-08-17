from numpy import array, dot, arccos, clip, rad2deg
from numpy.linalg import norm, inv, solve

A = array([[2, -3, 1], [3, 1, 1], [-1, -2, -1]])
b = array([2, -1, 1])

print(solve(A, b))