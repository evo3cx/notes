# Page 61

import numpy as np
from libraries import Activation_Softmax
from libraries import Loss_CategoricalCrossentropy

# Softmax classifier - combined Softmax activation
# and cross-entropy loss for faster backward step
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

  # Backward pass
  def backward(self, dvalues, y_true):

    # Number of samples 
    samples = len(dvalues)

    # If labels are one-hot encoded,
    # turn them into discrete values
    if len(y_true.shape) == 2 :
      # argmax with axis 1, will return index the higest value
      y_true = np.argmax(y_true, axis=1)

    # Copy so we can safely modify
    self.dinputs = dvalues.copy()

    # Calculate gradient
    self.dinputs[range(samples), y_true] -= 1

    # Normalize gradient
    self.dinputs = self.dinputs / samples