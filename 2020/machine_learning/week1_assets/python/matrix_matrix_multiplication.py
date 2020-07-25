import numpy as np


a = [
    [1,2,3],
    [2,3,4]
]
matrixA = np.matrix(a)



matrixB = np.matrix([
    [1,2],
    [3,4],
    [3,4],
])

result = matrixA* matrixB
print(result)