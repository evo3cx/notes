import numpy as np

# Probabilities of 3 samples
softmax_outputs = np.array([[0.7, 0.2, 0.1],
                            [0.5, 0.1, 0.4],
                            [0.02, 0.9, 0.08]])

# Target (ground-truth) lables for 3 samples
class_targets = np.array([0,1,1])

# Calculate values along second axis (axis of index 1)
# nunmpy.argmax return the indices of the maximum values along an axis
# it's will take index of the largest value in every row
predictions = np.argmax(softmax_outputs, axis = 1)

# If targets are one-hot encoded - convert them
if len(class_targets.shape) == 2:
  class_targets = np.argmax(class_targets, axis=1)

# True evaluates to 1; False to 0
accuracy = np.mean(predictions == class_targets)

print(np.argmax(softmax_outputs, axis = 1))
print('class_targets', class_targets)
print('predictions', predictions)
print('acc:', accuracy)
