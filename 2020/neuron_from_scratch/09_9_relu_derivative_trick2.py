# page 37
import numpy as np

# NOTE: it's same with prev code but with different technique

# Example layer output
z = np.array([[1, 2, -3, -4],
              [2, -7, -1, 3],
              [-1, 2, 5, -1]])

dvalues = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

# ReLU activation's derivative,
drelu = dvalues.copy()
drelu[z < 1]  = 0 # update element to 0 if value lower than 1

print (drelu)
