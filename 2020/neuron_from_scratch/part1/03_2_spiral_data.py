import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data

nnfs.init()

x, y = spiral_data(100,3)
plt.scatter(x[:, 0], x[:, 1], c=y, cmap='brg')
plt.show()
