# Page 54

import numpy as np

class Activation_Softmax:

  # Backward pass
  def backward(self, dvalues):

    # Create uninitialized array
    self.dinputs = np.empty_like(dvalues)

    # Enumerate output and gradients
    for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
      # Flatten output array
      single_output = single_output.reshape(-1, 1)

      # Calculate Jacobian matrix of the output and
      jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)

      # Calculate sample-wise gradient
      # and add it to the array of sample gradients
      self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)
