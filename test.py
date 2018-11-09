import numpy as np
from iteration import SimpleIterationRoots
from zeidel import zeidel
from print_res import print_tbl

A = np.array([[25, -10, 8],
              [0.5, 5, (4/3)],
              [3, -1, 6]])
B = np.array([[-10],
              [5],
              [-1]])

print_tbl(SimpleIterationRoots(A, B, 0.001))
print_tbl(zeidel(A, B, 0.001))

