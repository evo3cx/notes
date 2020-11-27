import matplotlib.pyplot as plt 
import numpy as np


def f(x):
  return 2*x

def nonliearFun(x):
  return 2*x**2

x = np.array(range(5))
y = f(x)

print(x)
print(y)

# Ini akan membuat garis lurus dengan y * 2
# plt.plot(x, y)
# plt.show()

# Slope adalah impact yang di dapat dari y dari x
# calculate slope
slope = (y[1]-y[0]) / (x[1]-x[0])
print("slope x on y:",slope)


y = nonliearFun(x)
print("non linar", y)

plt.plot(x, y)
plt.show()

slope = (y[1]-y[0]) / (x[1]-x[0])
slope2 = (y[3]-y[2]) / (x[3]-x[2])
print("slope x on y:",slope)
print("slope x on y:",slope2)
