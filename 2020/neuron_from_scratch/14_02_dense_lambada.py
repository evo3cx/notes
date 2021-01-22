# chapter 14 page 8 

import numpy as np
import matplotlib.pyplot as plt
import nnfs
from nnfs.datasets import spiral_data

from libraries import Loss_CategoricalCrossentropy
from libraries import Activation_Softmax
from libraries import Loss
from libraries import Activation_ReLU
from libraries import Optimizer_Adam

class Layer_Dense:
  def __init__(self, number_inputs, number_neurons,
    weigth_regularizer_l1=0, weight_regularizer_l2=0, 
    bias_regulaizer_l1=0, bias_regulaizer_l2=0):
    
    # Initialize weights and biases
    self.weights = 0.01 * np.random.randn(number_inputs, number_neurons)
    self.biases = np.zeros((1, number_neurons))

    # Set regularization strength
    self.weigth_regularizer_l1 = weigth_regularizer_l1
    self.weight_regularizer_l2 = weight_regularizer_l2
    self.bias_regulaizer_l1 = bias_regulaizer_l1
    self.bias_regulaizer_l2 = bias_regulaizer_l2

    # Forward pass
  def forward(self, inputs):
    # store inputs for later use in backpropagation
    self.inputs = inputs

    # Calculate output values from intpus, weights and biases
    self.output = np.dot(inputs, self.weights) + self.biases

  def backward(self, dvalues):
    # gradient on parameters
    self.dweights = np.dot(self.inputs.T, dvalues)
    self.dbiases = np.sum(dvalues, axis=0, keepdims=True)

    # Gradient on values
    self.dinputs = np.dot(dvalues, self.weights.T)


class Activation_Softmax_Loss_CategoricalCorssentropy():

  # Create activation and loss function object
  def __init__(self):
    self.activation = Activation_Softmax()
    self.loss = Loss_CategoricalCrossentropy()

  def forward(self, inputs, y_true):
    # Output layer's activation function
    self.activation.forward(inputs)

    # Set the output
    self.output = self.activation.output

    # Calculate and return loss value
    return self.loss.calculate(self.output, y_true)

  # Regularizatoin loss calculation
  def regularization_loss(self, layer):

    # 0 by default
    regularization_loss = 0

    # L1 regularization - weigths
    # calculate only when factor greater than 0
    if layer.weigth_regularizer_l1 > 0 :
      regularization_loss += layer.weigth_regularizer_l1 * np.sum(np.abs(layer.weights))
    
    # L2 regularization - weights
    if layer.weight_regularizer_l2 > 0 :
      regularization_loss += layer.weight_regularizer_l2 * np.sum(layer.weights * layer.weights)

    # L1 regularization - biases
    if layer.bias_regulaizer_l1 > 0 :
      regularization_loss += layer.bias_regulaizer_l1 * np.sum(np.abs(layer.biases))

    # L2 regularization  - bises
    if layer.bias_regulaizer_l2 > 0:
      regularization_loss += layer.bias_regulaizer_l2 * np.sum(layer.biases * layer.biases)

    return regularization_loss


  # Backward pass
  def backward(self, dvalues, y_true):

    # Number of samples
    samples = len(dvalues)

    # If labels are one-hot encoded,
    # turn them into discrete values
    if len(y_true.shape) == 2:
        # argmax with axis 1, will return index the higest value
        y_true = np.argmax(y_true, axis=1)

    # Copy so we can safely modify
    self.dinputs = dvalues.copy()

    # Calculate gradient
    self.dinputs[range(samples), y_true] -= 1

    # Normalize gradient
    self.dinputs = self.dinputs / samples

# -------------------------------------------------------------------------------
# EXECUTE 
# -------------------------------------------------------------------------------

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
    data_loss = loss_activation.forward(dense2.output, y)

    # Calculate regularization penalty
    regularization_loss = loss_activation.regularization_loss(dense1) + loss_activation.regularization_loss(dense2)

    # Calculate overall loss
    loss = data_loss + regularization_loss

    # Calculate accuracy from output of activation loss and target calculate values along first axis
    predictions = np.argmax(loss_activation.output, axis=1)
    if len(y.shape) == 2:
        y = np.argmax(y, axis=1)

    accuracy = np.mean(predictions == y)
    if not epoch % 100:
        print(f'epoch: {epoch}, ' +
              f'acc: {accuracy:.3f}, ' +
              f'regulation lost {regularization_loss:.3f}' +
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
