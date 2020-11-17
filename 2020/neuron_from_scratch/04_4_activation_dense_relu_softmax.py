import numpy as np
import nnfs
from nnfs.datasets import spiral_data
from libraries import Layer_Dense
from libraries import Activation_ReLU
from libraries import Activation_Softmax


# Initializes NNFS
nnfs.init()

# Create dataset
x,y = spiral_data(samples=100, classes=3)

# Create Dense layer with 2 input features and 3 output values
dense1 = Layer_Dense(2,3)

# Create Relu Activation (to be used with Dense Layer)
activation_relu = Activation_ReLU()

# Create second Dense layer with 3 input features (as we take output of previous layer here)
# and 3 output values
dense2 = Layer_Dense(3, 3)

# Create Softmax actiavtion (to be used with Dense layer):
activation_softmax = Activation_Softmax()

# Make a forward pass of our training data through this layer
dense1.forward(x)

# Make a forward pass through activation fucntion
# it takes the output of first dense layer here
activation_relu.forward(dense1.output)

#  Make a forward pass through second Dense layer
#  it takes outputs of activation function of first layer as inputs
dense2.forward(activation_relu.output)

# Make a forward pass through activation function it takes the output of the second dense layer here
activation_softmax.forward(dense2.output)

# Let's see ouput of the first few samples:
print(activation_softmax.output[:10])
