# Forward pass
x = [1.0, -2.0, 3.0]  # input values
w = [-3.0, -1.0, 2.0]  # weights
b = 1.0  # bias

# Multiplying inputs by weights
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

# Adding weighte inputs and a bias
z = xw0 + xw1 + xw2 + b


# ReLU activation function
y = max(z, 0)

# Backward pass

# The derivative from the layer
dvalue = 1.0

# Derivative of ReLU and the chain rule, used formula from Partial Derivative of Max
drelu_dz = dvalue * (1. if z > 0 else 0.)
print(drelu_dz)

# Partial derivative of the multiplication, the chain rule
dsum_dxw0 = 1  # derivative partial input x[0] and weight[0]
dsum_dxw1 = 1
dsum_dxw2 = 1
dsum_db = 1  # derivative partial bias

drelu_dxw0 = drelu_dz * dsum_dxw0
drelu_dxw1 = drelu_dz * dsum_dxw1
drelu_dxw2 = drelu_dz * dsum_dxw2
drelu_db = drelu_dz * dsum_db
print(drelu_dxw0)
