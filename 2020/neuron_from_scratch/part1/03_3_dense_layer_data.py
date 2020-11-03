import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data

# Initializes NNFS
nnfs.init()

# Dense Layer or fully connected layer, these layers are commonly referred to as "dense" layers in papers,
# literature, and code.

class Layer_Dense:
  def __init__ (self, number_inputs, number_neurons):
    # Initialize weights and biases
    self.weights = 0.01 * np.random.randn(number_inputs, number_neurons)
    self.biases = np.zeros((1, number_neurons))

  # Forward pass
  def forward(self, inputs)  :

    print(inputs.shape, self.weights.shape)
    # Calculate output values from intpus, weights and biases
    self.output = np.dot(inputs, self.weights) + self.biases


# Create datasets with 100 samples and 3 class
x, y = spiral_data(100, 3)

# Create Dense layer with 3 input features and 2 output values
dense = Layer_Dense(2, 5)


# print(x[:5])
# Perform a forward pass of our training data through this layer
dense.forward(x)

# print the first few samples
print(dense.output[:5])

