import numpy as np

# Matrix-Vector Multiplication
arr = [
    [1,2,3],
    [4,5,3],
]

vectors = [
    [2,1],
    [1,1],
    [3,3]
]

a = np.matrix(arr)
b = np.matrix(vectors)

print(b.shape, a.shape)
c = a * b
print(c)


