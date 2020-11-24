import math
import numpy as np
from libraries import Loss_CategoricalCrossentropy

# Consider a scenario with a neural network that performs classification between three classes, and the neural network classifies in batches of threee.
# After running through the softmax activation function with a batch of samples and 3 classes, the network's output layer yields:

# Probabilities for 3 samples
softmax_outputs = np.array([
  [0.7, 0.1, 0.2],
  [0.1, 0.5, 0.4],
  [0.02, 0.9, 0.08]
])

# Let asumes we trying to classify something as a "dog", "cat" or "human". 
# A dos is class 0 (at index 0),  cat class 1 (index 1), and a human class 2 (index 2)
# in the book the author say it categorical labels
# class_target = np.array([0, 1, 1])
class_targets = np.array([
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0]
])


loss_class = Loss_CategoricalCrossentropy()
loss = loss_class.calculate(softmax_outputs, class_targets)
print(loss)
