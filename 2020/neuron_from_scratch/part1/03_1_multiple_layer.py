import numpy as np

inputs = [
    [1, 2, 3, 2.5],
    [2, 5, -1, 2],
    [-1.5, 2.7, 3.3, -0.8]
]

weights = [
    [0.2, 0.8, -0.5, 1],
    [0.6, -0.91, 0.26, -0.5],
    [-0.26, -0.27, 0.17, 0.87]
]
biases = [2, 3, 0.5]

weights2 = [
    [0.1, -0.14, 0.5],
    [-0.5, 0.12, -0.33],
    [-0.44, 0.73, -0.13]
]
biases2 = [-1, 2, 0.5]

# Transposition weights from shape 3,4 into 4,3 so we can multiply with inputs
layer1_outputs = np.dot(inputs, np.array(weights).T) + biases
layer2_outputs = np.dot(layer1_outputs, np.array(weights2).T) + biases2

# print(inputs)
# print(layer1_outputs)
# print(layer2_outputs)


a = np.array( [
  [1,2,3],
  [2,2,2]])
b = np.array( [
  [2,2],
  [2,2],
  [2,2]])

# print(b.T)
print(a.shape, b.shape)
print( np.dot(a , b))
# print(np.multiply(a,b))
