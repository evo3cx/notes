import numpy as np


# Softmax Formula
# source: https://en.wikipedia.org/wiki/Softmax_function

# values from previous output we described in file 04_1_activation_rely.py
layer_outputs = [4.8, 1.121, 0]

# e - mathematical constant, w use E here to match a common coding
# style where constants are uppercased
E = 2.71828182846 # you can also use math.e

# For each value in a vector calculate the exponential value
exp_values = []
for output in layer_outputs:
  exp_values.append( E** output) # ** - power operator in python
  print(E**output)

print ('exponentated values:')
print (exp_values)

# Now normalize values
norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
  norm_values.append(value / norm_base)

print("Normalized exponentiated values:")
print(norm_values)
print("Sum of normalized values:", sum(norm_values))


# Numpy way
print('\n\n Numpy way \n\n')

#  For each value in a vector, calculate the exponential value
nump_exp_values = np.exp(layer_outputs)
print('exponentiated values:')
print(nump_exp_values)

# Now Normalize values
norm_values = nump_exp_values / np.sum(nump_exp_values)
print('normalized exponentiated values:')
print(norm_values)
print('sum of normalized values:', np.sum(norm_values))

print("layer", layer_outputs)

# Normalize them for each sample
probabilities = nump_exp_values / np.sum([nump_exp_values], axis = 1, keepdims=True)
print("probabilities", probabilities)

# Activation Softmax define

