import math
import numpy as np
import nnfs
from nnfs.datasets import spiral_data


from libraries import Loss_CategoricalCrossentropy
from libraries import Layer_Dense
from libraries import Activation_ReLU
from libraries import Activation_Softmax

# Initial seed data
nnfs.init()

# Create dataset
x, y = spiral_data(samples=100, classes=3)

#  Create Dense layer with 2 input features and 3 output values
dense1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense Layer)
activation_relu = Activation_ReLU()

# Create second Dense layer with 3 input features (as we take output of previous dense layer here)
# And 3 output values 
dense2 = Layer_Dense(3, 3)

# Create Softmax activation (to make sure we remove negative value and large value from output)
activation_softmax = Activation_Softmax()

# Create loss function
loss_function = Loss_CategoricalCrossentropy()

#  Perform a forward pass of our training data through this layer
dense1.forward(x)

#  Perform a forward pass through activation function
#  it takes the output of first dense layer here
activation_relu.forward(dense1.output)

# Perform a forward pass through second Dense Layer
#  it takes output of activation function of first layer as inputs
dense2.forward(activation_relu.output)

#  Perform a forward pass through activation function
#  it takes the output of second dense layer here
activation_softmax.forward(dense2.output)

print(activation_softmax.output[:5])

#  Perform a forward pass through loss function
#  it take the output of second dense layer here and return loss
loss = loss_function.calculate(activation_softmax.output, y)

#  Print loss value
print('loss:', loss)


# Calculate accuracy from output of activation2 and targets
# calculate values along first axis
prediction = np.argmax(activation_softmax.output, axis = 1)
if len(y.shape) == 2:
  y = np.argmax(y, axis=1)
accuracy = np.mean(prediction==y)

# Print accuracy
print('acc:', accuracy)
