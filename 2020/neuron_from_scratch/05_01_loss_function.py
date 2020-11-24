import math
import numpy as np

# An example output from the output layer of the neural network
softmax_output = [0.7, 0.1, 0.2]

# ground truth
target_output = [1,0, 0]

loss = -(math.log(softmax_output[0])*target_output[0] +
        math.log(softmax_output[1]) * target_output[1] + 
        math.log(softmax_output[2]) * target_output[2])

print(loss)

print(-math.log(softmax_output[0]))


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
# in the book the author say it one-hot encoded labels
class_target = [0, 1, 1]

# let get every array from softmax_output with class_target
for targ_idx, distribution in zip(class_target, softmax_outputs):
  print(distribution[targ_idx])

# same with above, but we use numpy function, 
# what are the 0, 1, and 2 values? NumPy lets us index an array in multiple ways
print(softmax_outputs[[0,1,2], class_target])

# or with built in functio nrange
print(softmax_outputs[range(len(softmax_outputs)), class_target])

# we calculate average loss per batch to have an idea how our model is doing during traning
# this operation is euqaivalent with line 8
neg_log = -np.log(softmax_outputs[range(len(softmax_outputs)), class_target])

average_loss = np.mean(neg_log)
print("average_loss", average_loss)



# Probabilities for 3 samples
softmax_outputs = np.array([
  [0.7, 0.1, 0.2],
  [0.1, 0.5, 0.4],
  [0.02, 0.9, 0.08]
])

#  now calculate output with class target with multple array or  one-hot encoded labels
class_targets = np.array([
  [1, 0, 0],
  [0, 1, 0],
  [0, 1, 0]
])

# probabilites for target values - 
# only if categorical labels
if len(class_targets.shape) == 1:
  correct_confidences = softmax_outputs[
    range(len(softmax_outputs)),
    class_targets
  ]

# Mask values - only for one hot encoded labels
elif len(class_targets.shape) == 2:
  correct_confidences = np.sum(
    softmax_outputs*class_targets, axis=1
  )


# Losses
neg_log = -np.log(correct_confidences)

average_loss = np.mean(neg_log)
print("avg",average_loss)
