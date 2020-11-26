import numpy as np
import matplotlib.pyplot as plt
import nnfs 
from nnfs.datasets import vertical_data

from libraries import Layer_Dense
from libraries import Loss_CategoricalCrossentropy
from libraries import Activation_ReLU
from libraries import Activation_Softmax

# Optimization determine how to adjust the weights and biases to decrease the loss. 
# Finding an intelligent way to adjust the neurons’ input’s weights and biases to minimize loss is the main difficulty of neural networks.


# initialize dataset
nnfs.init()

# Create dataset
x, y = vertical_data(samples=100, classes=3)

# Create model
dense1 = Layer_Dense(2, 3) # First dense layer with 2 input, 3 output
activation_relu = Activation_ReLU()
dense2 = Layer_Dense(3, 3) # Second dense layer, 3 inputs, 3 output
activation_softmax = Activation_Softmax()

# Create loss function
loss_function = Loss_CategoricalCrossentropy()

# Then create some variables to track the best loss and the associated weights and biases 
lowest_loss = 9999999 # some initial value
best_dense1_weights = dense1.weights.copy()
best_dense1_biases = dense1.biases.copy()
best_dense2_weights = dense2.weights.copy()
best_dense2_biases = dense2.biases.copy()

# we iterate as many times as desired, pick random values for weights and biases, and save the weights
# and bises if they gnerate the lowest-seen loss:

for iteration in range(10000):

  # Generate a new set of weights for iteration
  dense1.weights += 0.05 * np.random.randn(2,3)
  dense1.biases += 0.05 * np.random.randn(1,3)
  dense2.weights += 0.05 * np.random.randn(3, 3)
  dense2.biases += 0.05 * np.random.randn(1, 3)

  # Perform a forward pass of the training data through this layer
  dense1.forward(x)

  # we use Activation ReLU for hidden layer
  activation_relu.forward(dense1.output)
  dense2.forward(activation_relu.output)

  # we use Activation Softmax for output layer
  activation_softmax.forward(dense2.output)

  # Perform a forward pass through activation function
  # it takes the output of second dense layer here and returns loss
  loss = loss_function.calculate(activation_softmax.output, y)

  # Calculate accuracy from output of activation2 and tragets
  # calculate values along first axis
  predictions = np.argmax(activation_softmax.output, axis=1)
  accuracy = np.mean(predictions==y)

  # If loss is smaller - print and save weights and biases asid
  if loss < lowest_loss:
    print('New set of weight found, iteration:', iteration, 'loss:', loss, 'accucray', accuracy)

    best_dense1_weights = dense1.weights.copy()
    best_dense1_biases = dense1.biases.copy()
    best_dense2_weights = dense2.weights.copy()
    best_dense2_biases = dense2.biases.copy()
    lowest_loss = loss
  else:
    # Revert weight and bises to the best form
    dense1.weights = best_dense1_weights.copy()
    dense1.biases = best_dense1_biases.copy()
    dense2.weights = best_dense2_weights.copy()
    dense2.biases = best_dense2_biases.copy()
  

  
