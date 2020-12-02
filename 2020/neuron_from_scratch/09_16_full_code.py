# page 67

import numpy as np
import nnfs
from nnfs.datasets import spiral_data

from libraries import Activation_Softmax_Loss_CategoricalCorssentropy
from libraries import Activation_Softmax
from libraries import Loss_CategoricalCrossentropy
from libraries import Activation_ReLU
from libraries import Layer_Dense

# initialize nnfs dataset
nnfs.init()

# Create dataset
x, y = spiral_data(samples=100, classes=3)

# Create Dense Layer with 2 input features and 3 output values
dense1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense Layer)
activation1_relu = Activation_ReLU()

# Create second Dense layer with 3 input features (as we take  ouput of previous layer here)
# and 3 output values (output values)
dense2 = Layer_Dense(3, 3)

# Create a softmax classfier's combined loss and activation
loss_activation = Activation_Softmax_Loss_CategoricalCorssentropy()

# Perform a forward pass of our training data through this layer
dense1.forward(x)

# Perform a forward pass through activation function
# takes the output of first dense layer here
activation1_relu.forward(dense1.output)

# Perform a forward pass through second Dense layer takes
# output of activation function of first layer as inputs
dense2.forward(activation1_relu.output)

# Perform a forward pass through the activation/loss function
# take the output of second dense layer here and return loss
loss = loss_activation.forward(dense2.output, y)

# Let's see output of the first few sampels:
print(loss_activation.output[:5])

# Print loss value
print('loss:', loss)

# Calculate accuracy from output of loss activation and targets
# calculate values along first axis
predictions = np.argmax(loss_activation.output, axis=1)
if len(y.shape) == 2:
  y = np.argmax(y, axis=1)

accuracy = np.mean(predictions == y)

print('acc', accuracy)

# Backward pass
loss_activation.backward(loss_activation.output, y)

# run backward backpropagtion from derivative loss activation
dense2.backward(loss_activation.dinputs)

# run backward from derivative dense2
activation1_relu.backward(dense2.dinputs)

# then passed it to dense1
dense1.backward(activation1_relu.dinputs)


# Print gradients
print("dense1 w", dense1.dweights)
print("dense1 bias", dense1.dbiases)
print("dense1 w", dense2.dweights)
print("dense1 biase",dense2.dbiases)
