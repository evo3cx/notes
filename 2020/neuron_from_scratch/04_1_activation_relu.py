import numpy as np
import nnfs
from nnfs.datasets import spiral_data
from libraries import Layer_Dense


# Initializes NNFS
nnfs.init()

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

    # use numpy to create more clear result
    # Calculate ouput values from input
    self.output = np.maximum(0, input)

# Create datasets
x,y = spiral_data(100, 3)

# Create Dense layer with 2 input features and 3 output layer
dense1 = Layer_Dense(2, 3)

# Create ReLU activation (to be used with Dense Layer)
activation1 = Activation_ReLU()

# Make a forward pass of our training data through this layer
dense1.forward(x)

# Forward pass through activation func.
# Takes in output from previous layer
activation1.forward(dense1.output)


# Print first 5 rows
print(activation1.output[:5])
