# Page 64

import numpy as np
import nnfs
from libraries import Activation_Softmax_Loss_CategoricalCorssentropy
from libraries import Activation_Softmax
from libraries import Loss_CategoricalCrossentropy
from timeit import timeit

# initialize nnfs dataset
nnfs.init()

# dummy output from activation softmax
softmax_output = np.array([[0.7, 0.1, 0.2],
                           [0.1, 0.5, 0.4],
                           [0.02, 0.9, 0.08]])

class_targets = np.array([0, 1, 1])

softmax_loss = Activation_Softmax_Loss_CategoricalCorssentropy()
softmax_loss.backward(softmax_output, class_targets)

dvalues1 = softmax_loss.dinputs

activation = Activation_Softmax()
activation.output = softmax_output

loss = Loss_CategoricalCrossentropy()
loss.backward(softmax_output, class_targets)

# update activation softmax backward
activation.backward(loss.dinputs)
dvalues2 = activation.dinputs

print('Gradient: combined loss and activation:')
print(dvalues1)
print('Gradient: seperate loss and activation:')
print(dvalues2)


# Now we measure how faster combined and seperate loss and activation.
def f1():
  # calculate backward combine softmax with loss
    softmax_loss = Activation_Softmax_Loss_CategoricalCorssentropy()
    softmax_loss.backward(softmax_output, class_targets)
    dvalues1 = softmax_loss.dinputs


def f2():
  # calculate backward seperate softmax with loss
    activation = Activation_Softmax()
    activation.output = softmax_output

    loss = Loss_CategoricalCrossentropy()
    loss.backward(softmax_output, class_targets)
    activation.backward(loss.dinputs)
    dvalues2 = activation.dinputs


time1 = timeit(lambda: f1(), number=10000)
time2 = timeit(lambda: f2(), number=10000)

print(time2/time1)
