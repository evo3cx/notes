import numpy as np

inputs = [1.0, 2.0, 3.0, 2.5]
weights = [
   [0.2, 0.8, -0.5, 1.0],
   [0.5, -0.91, 0.26, -0.5],
   [-0.26, -0.27, 0.17, 0.87]
]

# STEP 3 neuron 1 layer menggunakan numpy
biases = [2.0, 3.0, 0.5]
output_np = np.dot(weights, inputs) + biases
print("output np.dot", output_np)
