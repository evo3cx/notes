# Simplified code from previous chapter
# NOTE: Watch video for more interactive
# https://nnfs.io/com/

# Forward pass
x = [1.0, -2.0, 3.0]
w = [-3.0, -1.0, 2.0]
b = 1.0  # bias

# Multiplying inputs by weights
xw0 = x[0] * w[0]
xw1 = x[1] * w[1]
xw2 = x[2] * w[2]

# Adding weighted input and a bias
z = xw0 + xw1 + xw2 + b

# ReLU activation function
y = max(z, 0)

# Backward pass
# The derivative from the next layer
dvalue = 1.0


# Partial derivative of the multiplication, the chain rule
dmul_dx0 = dvalue * (1. if z > 0 else 0.) * w[0]
dmul_dw0 = dvalue * (1. if z > 0 else 0.) * x[0]
dmul_dx1 = dvalue * (1. if z > 0 else 0.) * w[1]
dmul_dw1 = dvalue * (1. if z > 0 else 0.) * x[1]
dmul_dx2 = dvalue * (1. if z > 0 else 0.) * w[2]
dmul_dw2 = dvalue * (1. if z > 0 else 0.) * x[2]
drelu_db = dvalue * (1. if z > 0 else 0.) * b
print(dmul_dx0, dmul_dw0, dmul_dx1, dmul_dw1, dmul_dx2, dmul_dw2)

# gradient on inputs
dx = [dmul_dx0, dmul_dx1, dmul_dx2]

# gradient on weights
dw = [dmul_dw0, dmul_dw1, dmul_dw2]

#  gradient on bias
db = drelu_db * dvalue
