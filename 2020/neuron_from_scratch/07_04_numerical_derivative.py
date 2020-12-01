import numpy as np
import matplotlib.pyplot as plt


def nonLinear(x):
    return 2*x**2


# np.arange(start, stop, step) to give us smoother line
x = np.arange(0, 5, 0.001)
y = nonLinear(x)

plt.plot(x, y)

colors = ['k', 'g', 'r', 'b', 'c']


# We put the tangent line calculation into  a function so we can call
# it multiple times for different values of x
# approximate_derivative and b are contstant for give function
# thus calculated once above this function
def approximate_tangent_line(x, approximate_derivative, b):
    return (approximate_derivative*x) + b


for i in range(5):
    p2_delta = 0.0001
    x1 = i
    x2 = x1+p2_delta

    y1 = nonLinear(x1)
    y2 = nonLinear(x2)

    print((x1, y1), (x2, y2))
    approximate_derivative = (y2-y1)/(x2-x1)
    b = y2-(approximate_derivative*x2)

    to_plot = [x1-0.9, x1, x1+0.9]
    plt.scatter(x1, y1, c=colors[i])
    plt.plot([point for point in to_plot],
             [
        approximate_tangent_line(point, approximate_derivative, b)
        for point in to_plot
    ], colors[i])

    print('Approximate derivative for f(x)',
          f'where x {x1} is {approximate_derivative}')


plt.show()
