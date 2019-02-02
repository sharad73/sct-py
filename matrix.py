#!/bin/python

import math
import os
import random
import re
import sys
import numpy as np

print(sys.path)

A = np.array([[1, 4, 5], 
    [-5, 8, 9],
    [-6, 7, 11]])
n=len(A)
print("Length of Array is %d:"%n)

print(A[:2, :4])  # two rows, four columns

''' Output:
[[ 1  4  5 12]
 [-5  8  9  0]]
'''


print(A[:1,])  # first row, all columns

''' Output:
[[ 1  4  5 12 14]]
'''

print(A[:,2])  # all rows, second column

''' Output:
[ 5  9 11]
'''

print(A[:, 2:5])  # all rows, third to fifth column

'''Output:
[[ 5 12 14]
 [ 9  0 17]
 [11 19 21]]
'''

for i in range(n):
    print(A[i])
