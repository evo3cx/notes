# PAGE 63
import numpy as np
import matplotlib.pyplot as plt
import nnfs
from nnfs.datasets import spiral_data

from libraries import Layer_Dense
from libraries import Activation_Softmax_Loss_CategoricalCorssentropy


# Optimizer ADAM - Chapter 10 - Page 62
class Optimizer_Adam:

    #  Initialize optimizer - set settings
    def __init__(self, learning_rate=0.001, decay=0., epsilon=1e-7, beta_1=0.9, beta_2=0.999):
        self.learning_rate = learning_rate
        self.current_learning_rate = learning_rate
        self.decay = decay
        self.iterations = 0
        self.epsilon = epsilon
        self.beta1 = beta_1
        self.beta2 = beta_2

    # Call once before any parameter updates
    def pre_update_params(self):
        if self.decay:
            self.current_learning_rate = self.learning_rate * \
                (1. / (1. + self.decay * self.iterations))

    #  Update paramters
    def update_params(self, layer):

        # If layer does not contain cache arrays
        # create them filled with zeros
        if not hasattr(layer, 'weight_cache'):
            layer.weight_momentums = np.zeros_like(layer.weights)
            layer.weight_cache = np.zeros_like(layer.weights)
            layer.bias_momentums = np.zeros_like(layer.biases)
            layer.bias_cache = np.zeros_like(layer.biases)

        # Update momentum with current gradients
        layer.weight_momentums = self.beta1 * \
            layer.weight_momentums + (1 - self.beta1) * layer.dweights
        layer.bias_momentums = self.beta1 * \
            layer.bias_momentums + (1 - self.beta1) * layer.dbiases

        # Get corrected momentum
        #  self.iteration is 0 at first pass and we need to start with 1 here
        weight_momentums_corrected = layer.weight_momentums / (1 - self.beta1 ** (self.iterations + 1)) \
            / (1 - self.beta1 ** (self.iterations+1))
        bias_momentums_corrected = layer.bias_momentums / (1 - self.beta1 ** (self.iterations + 1)) \
            / (1 - self.beta1 ** (self.iterations+1))

        # Update cache with squared current gradients
        layer.weight_cache = self.beta2 * layer.weight_cache + \
            (1 - self.beta2) * layer.dweights ** 2

        layer.bias_cache = self.beta2 * layer.bias_cache + \
            (1 - self.beta2) * layer.dbiases ** 2

        # Get corrected cache
        weight_cache_corrected = layer.weight_cache / \
            (1 - self.beta2 ** (self.iterations + 1))
        bias_cache_corrected = layer.bias_cache / \
            (1 - self.beta2 ** (self.iterations + 1))

        # Vanila SGD parameter update + normalization
        # with square rooted cache
        layer.weights += -self.current_learning_rate * \
            weight_momentums_corrected / \
            (np.sqrt(weight_cache_corrected)+self.epsilon)

        layer.biases += -self.current_learning_rate * \
            bias_momentums_corrected / \
            (np.sqrt(bias_cache_corrected) + self.epsilon)

    # Call once after any paramter updates
    def post_update_params(self):
        self.iterations += 1


# --------------------------------


# initialize nnfs dataset
nnfs.init()


# Create dataset
x, y = spiral_data(samples=100, classes=3)

#  Create dense layer with 2 input features and 64 output valus
dense1 = Layer_Dense(2, 64)

# Create softmax classfier's combined loss and activation
loss_activation = Activation_Softmax_Loss_CategoricalCorssentropy()


optimizer = Optimizer_Adam(learning_rate=0.02, decay=1e-5)


# forward
dense1.forward(x)
loss_activation.forward(dense1.output,y)
dense1.backward(loss_activation.output)

# Update weight and biases
optimizer.pre_update_params()
optimizer.update_params(dense1)
optimizer.post_update_params()

print(dense1.weights[0])
print(dense1.biases[0])
