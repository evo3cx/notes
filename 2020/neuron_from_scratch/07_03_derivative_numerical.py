import matplotlib.pyplot as plt 
import numpy as np


def f(x):
  return 2*x

def nonliearFun(x):
  return 2*x**2

#  np.arange (start, stop, step) to give us smoother line
x = np.arange(0, 5, 0.001)
y = nonliearFun(x)

plt.plot(x, y)
# plt.show()


# The point and the "close enough" point, 0.001 its value for every step
p2_delta = 0.001
x1 = 2
x2 = x1+p2_delta

y1 = nonliearFun(x1)
y2 = nonliearFun(x2)
print((x1, y1), (x2, y2))

# Derivative approximation and y-intercept for the tangent line
#  implement approximate derivate formula
approximate_derivative = (y2-y1)/(x2-x1)

# calculate intercept y
b = y2 - approximate_derivative*x2

# We put the tangent line calculation into a function so we can call
# it multiple times for different values of x
# approximate_derivative and b are constant for given function
# thus calculated once above this function
def tangent_line(x):
  return approximate_derivative*x + b

# plotting the tangent line
# +/- 0.9 to draw the tangen line on our graph (panjang line)
# then we calculate the y for given x using the tangen line function
# Matplotlib will draw a line for us through these points
to_plot = [x1-0.9, x1, x1+0.9]
plt.plot(to_plot, [tangent_line(i) for i in to_plot])

print([tangent_line(i) for i in to_plot])

print('Approximate derivative for f(x)', f'where x = {x1} is {approximate_derivative}')
plt.show()
