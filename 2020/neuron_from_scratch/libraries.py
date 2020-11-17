import numpy as np

class Layer_Dense:
  def __init__ (self, number_inputs, number_neurons):
    # Initialize weights and biases
    self.weights = 0.01 * np.random.randn(number_inputs, number_neurons)
    self.biases = np.zeros((1, number_neurons))

  # Forward pass
  def forward(self, inputs)  :
    # Calculate output values from intpus, weights and biases
    self.output = np.dot(inputs, self.weights) + self.biases


# Rectified Linear Activation function is simple than the sigmoid. 
# It's quite literally y=x, clipped at 0 from the negative side. If x is less than or equal to 0, the y is 0
# otherwise, y is equal to x.
# y = x <= 0 ? 0 : X
class Activation_ReLU:

  # forward pass
  def forward(self, input):
    # in plain python
    # output = []
    # for i in input:
    #   val = 0 if x <= 0 else x
    #   output.append(val)
    # self.output = output

    # use numpy creat more clear result
    # Calculate ouput values from input
    self.output = np.maximum(0, input)


# Softmax Formula
# source: https://en.wikipedia.org/wiki/Softmax_function

# Softmax activation
class Activation_Softmax:

  # forward pass
  def forward(self, input):

    # Get unnormalized probabilities
    exp_values = np.exp(input - np.max(input, axis=1, keepdims=True))
    print(exp_values)

    # Normalize them for each sample
    probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

    self.output = probabilities
