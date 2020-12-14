# page 9
import numpy as np
import matplotlib.pyplot as plt
import nnfs
from nnfs.datasets import spiral_data

from libraries import Activation_Softmax_Loss_CategoricalCorssentropy
from libraries import Activation_Softmax
from libraries import Loss_CategoricalCrossentropy
from libraries import Activation_ReLU
from libraries import Layer_Dense

# initialize nnfs dataset
nnfs.init()


class Optimizer_SGD:
    # Initialize optimizer - set settings,
    #  learning rate of 1. is default for this optimizer
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    # Update parameters
    def update_params(self, layer):
        # Our goal to minimize value and gradient point towards steepest function ascent,
        # thus we substractd learning rate
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases


# create dataset, with 100 sample 3 features
x, y = spiral_data(samples=100, classes=3)

# Create Dense layer with 2 input fatures and 64 output values
dense1 = Layer_Dense(2, 64)

# Create Relu activation (to be used with Dense Layer)
activation_relu = Activation_ReLU()

# Create Dense layer with 2 input fatures and 64 output values
dense_hidden = Layer_Dense(64, 64)

# Create Relu activation (to be used with Dense Layer)
activation_hidden_relu = Activation_ReLU()

# Create second Dense layer with 64 input features (as we take output of
# previous layer here) and 3 output values (output values)
dense2 = Layer_Dense(64, 3)

# create softmax classfier's combined loss and activation
loss_activation = Activation_Softmax_Loss_CategoricalCorssentropy()

# Create optimizer
optimizer = Optimizer_SGD(1)

# Each full pass through all of the training data is called an epoch
for epoch in range(10001):

    # Perform a forward pass of our training data though this layer
    dense1.forward(x)

    # Perform a forward pass through activation function
    # takes the output of first dense layer here
    activation_relu.forward(dense1.output)

        # Perform a forward pass of our training data though this layer
    dense_hidden.forward(activation_relu.output)

    # Perform a forward pass through activation function
    # takes the output of first dense layer here
    activation_hidden_relu.forward(dense_hidden.output)


    # Perform a forward pass through second Dense layer
    # takes output of activation function of first layer as input
    dense2.forward(activation_hidden_relu.output)

    # Perform a forward pass through the activation/loss function
    # takes the output of second dense layer here and returns loss
    loss = loss_activation.forward(dense2.output, y)

    # Calculate accuracy from output of loss activation and targets
    # calculate values along first axis
    predictions = np.argmax(loss_activation.output, axis=1)
    if len(y.shape) == 2:
        y = np.argmax(y, axis=1)

    accuracy = np.mean(predictions == y)

    # Let's print loss value

    if not epoch % 100:
        print(f'epoch: {epoch}, ' +
              f'acc: {accuracy:.3f}, ' +
              f'loss: {loss:.3f}')

    # Backward pass/ backpropagation
    loss_activation.backward(loss_activation.output, y)
    dense2.backward(loss_activation.dinputs)
    
    activation_hidden_relu.backward(dense2.dinputs)
    dense_hidden.backward(activation_hidden_relu.dinputs)

    activation_relu.backward(dense_hidden.dinputs)
    dense1.backward(activation_relu.dinputs)

    # Then we finnaly use our optimizer to update weights and biases

    # Update weight and biases
    optimizer.update_params(dense1)
    optimizer.update_params(dense_hidden)
    optimizer.update_params(dense2)
