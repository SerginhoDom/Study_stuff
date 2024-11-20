import sys
import numpy as np
import statistics

A = []
for line in sys.stdin:
    A.append([float(x) for x in line.split()])
A = np.array(A)

for i in range (len(A)):
    avg = sum(A[i])/len(A[i])
    for j in range (len(A[i])):
        A[i, j] -= avg

print(A)