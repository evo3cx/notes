# PAGE 63
import numpy as np
import matplotlib.pyplot as plt
import nnfs
from nnfs.datasets import spiral_data

from libraries import Activation_Softmax_Loss_CategoricalCorssentropy
from libraries import Activation_Softmax
from libraries import Loss_CategoricalCrossentropy
from libraries import Activation_ReLU
from libraries import Layer_Dense
from libraries import Optimizer_Adam


# initialize nnfs dataset
nnfs.init()


# Create dataset
x, y = spiral_data(samples=100, classes=3)

#  Create dense layer with 2 input features and 64 output valus
dense1 = Layer_Dense(2, 64)

#  Create ReLU activation (to be used with Dense Layer).
activation_relu = Activation_ReLU()

# Create second dense layer with 64 iput features ( as we take output of previous layer here)
# and 3 output values
dense2 = Layer_Dense(64, 3)

# Create softmax classfier's combined loss and activation
loss_activation = Activation_Softmax_Loss_CategoricalCorssentropy()

# Create optimizer kita menggunakan decay dan momentum untuk mendapatkan LR global minimum
optimizer = Optimizer_Adam(decay=5e-7, learning_rate=0.06,)

# Train in loop
for epoch in range(10001):

    # Perform a forward pass of our training data through this layer
    dense1.forward(x)

    # perform a forward pass through activation function
    # takes the output of first dense layer here
    activation_relu.forward(dense1.output)


    # Perform a forward pass through second dense layer
    # takes output of activation function of first layer as inputs
    dense2.forward(activation_relu.output)

    # Perform a forward pass through second Dense layer
    # takes the output of second dense layer here and return loss
    loss = loss_activation.forward(dense2.output, y)

    # Calculate accuracy from output of activation loss and target calculate values along first axis
    predictions = np.argmax(loss_activation.output, axis=1)
    if len(y.shape) == 2:
        y = np.argmax(y, axis=1)

    accuracy = np.mean(predictions == y)
    if not epoch % 100:
        print(f'epoch: {epoch}, ' +
              f'acc: {accuracy:.3f}, ' +
              f'loss: {loss:.3f}, ' +
              f'lr: {optimizer.current_learning_rate}')

    # Backward pass/ backpropagation
    loss_activation.backward(loss_activation.output, y)
    dense2.backward(loss_activation.dinputs)
    activation_relu.backward(dense2.dinputs)
    dense1.backward(activation_relu.dinputs)

    # Then we finnaly use our optimizer to update weights and biases

    # Update weight and biases
    optimizer.pre_update_params()
    optimizer.update_params(dense1)
    optimizer.update_params(dense2)
    optimizer.post_update_params()
