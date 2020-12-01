# page 34
import numpy as np


# Passed in gradient from the next layer for the purpose of this example
# we're going to use an array of an incremental gradient values
dvalues = np.array([
    [1., 1., 1],
    [2., 2., 2.],
    [3., 3., 3.]
])

# One bias for each neuron
# biases are the row vector with a shape (1, n of neurons)
biases = np.array([[2, 3, 0.5]])

# dbiases - sum values , do this over samples (first axis) 
# keep dims since this by default will product a plain list - 
# they explain this in chapter 4
dinputs = np.sum(dvalues, axis=0, keepdims=True)
print(dinputs)
