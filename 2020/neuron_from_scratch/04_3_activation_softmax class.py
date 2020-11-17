import numpy as np


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

softmax = Activation_Softmax()
softmax.forward([[1,2,3]])
print(softmax.output)
