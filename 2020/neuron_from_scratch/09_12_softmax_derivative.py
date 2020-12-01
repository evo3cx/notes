# Page 52
import numpy as np

# Let's make up a single sample
softmax_output = [0.7, 0.1, 0.2]

softmax_output = np.array(softmax_output).reshape(-1, 1)
print(softmax_output)

print(softmax_output * np.eye(softmax_output.shape[0]))

# or with simple concultion
print(np.diagflat(softmax_output))

# From the equation part is  we should multiplication of the Softmax output, iteraing over index
# we'll have to multiply the values from the Softmax function's output (in all of the combinations), 
# we can use the dot product operation.

print(np.dot(softmax_output, softmax_output.T))

# Finally, we can perform the substraction of both arrays (following the equation),
# The matrix result of the equation and the array solution provided by the code is called the
# Jacobian matrix. In our case, the Jacobian matrix is an array of partial derivatives in all of the combinations of bot input vectors.
print(np.diagflat(softmax_output) - np.dot(softmax_output, softmax_output.T))
