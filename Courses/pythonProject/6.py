import statistics
import numpy as np
import pandas as pd

arr1 = np.array([1, 1, 2, 5, 6, 7, 3, 4, 5, 6], float)
arr2 = np.array([ 1, 5, 6, 2, 8, 4, 3], float)
arr3 = np.array([545, 546, 550, 544, 548, 547, 543], float)

print(statistics.mean(arr1))
print(statistics.pvariance(arr1))
print(round(np.std(arr1, ddof=1), 2))
print(statistics.pvariance(arr2) - statistics.pvariance(arr3))

x = [3, 5, 3, 6, 7, 2, 1, 0, 15, 4]
y = [-3, -2, 6, 8, 4, 1, 0, 8, 2, 8]

correlation = np.corrcoef(x, y)[0, 1]

correlation = round(correlation, 2)
print(correlation)