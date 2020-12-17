import numpy as np

class Layer_Dense:
  def __init__ (self, number_inputs, number_neurons):
    # Initialize weights and biases
    self.weights = 0.01 * np.random.randn(number_inputs, number_neurons)
    self.biases = np.zeros((1, number_neurons))

  # Forward pass
  def forward(self, inputs)  :
    # store inputs for later use in backpropagation
    self.inputs = inputs

    # Calculate output values from intpus, weights and biases
    self.output = np.dot(inputs, self.weights) + self.biases

  # Backward pass,
  # 1. What purpose of backpropagation? to optimize loss we can calculate how much of an "impact" this neurons bias had
  # by calculate how much of an "impact" weights had
  # 2. We can calculate how much of an impact the input into this neuron had, 
  # Now if the neuron we are looking at was an input layer neuron, this wouldn't really mattersince we can't update the inputs we get, 
  # but if the input into this neuron came from another neuron, this value basically represents how much of an impact that neuron had on this neuron. 
  # 
  # So we can then use this value (dinputs) to further update the next neurons weights.
  def backward(self, dvalues):
    # gradient on parameters
    self.dweights = np.dot(self.inputs.T, dvalues)
    self.dbiases = np.sum(dvalues, axis=0, keepdims=True)

    # Gradient on values
    self.dinputs = np.dot(dvalues, self.weights.T)



# Rectified Linear Activation function is simple than the sigmoid. 
# It's quite literally y=x, clipped at 0 from the negative side.
# If x is less than or equal to 0, the y is 0 otherwise, y is equal to x.
# y = x <= 0 ? 0 : X
class Activation_ReLU:

  # forward pass
  def forward(self, input):
    # Remember input value
    self.input = input

    # in plain python
    # output = []
    # for i in input:
    #   val = 0 if x <= 0 else x
    #   output.append(val)
    # self.output = output

    # use numpy creat more clear result
    # Calculate ouput values from input
    self.output = np.maximum(0, input)

  def backward(self, dvalues):
    # Since we need to modify original variable,
    # let's make a copy of values first
    self.dinputs = dvalues.copy()

    # ReLU activation's derivative,
    self.dinputs[self.input <= 0]  = 0 # update element to 0 if value lower than 0


# Softmax Formula
# source: https://en.wikipedia.org/wiki/Softmax_function

# Softmax activation
class Activation_Softmax:

  # forward pass
  def forward(self, input):
    # Remember input values
    self.inputs = input

    # Get unnormalized probabilities
    exp_values = np.exp(input - np.max(input, axis=1, keepdims=True))

    # Normalize them for each sample
    probabilities = exp_values / np.sum(exp_values, axis=1, keepdims=True)

    self.output = probabilities

  # Backward pass
  def backward(self, dvalues):

    # Create uninitialized array
    self.dinputs = np.empty_like(dvalues)

    # Enumerate output and gradients
    for index, (single_output, single_dvalues) in enumerate(zip(self.output, dvalues)):
      # Flatten output array
      single_output = single_output.reshape(-1, 1)

      # Calculate Jacobian matrix of the output
      jacobian_matrix = np.diagflat(single_output) - np.dot(single_output, single_output.T)

      # Calculate sample-wise gradient
      # and add it to the array of sample gradients
      self.dinputs[index] = np.dot(jacobian_matrix, single_dvalues)


# Common loss class
class Loss:

  # Calculate the data and regularization losses, no matter which loss function we'll use,
  # the overall loss is always a mean value of all sample losses.
  # given model output and ground truth values
  def calculate(self, output, y):

    # Calculate sample losses
    sample_losses = self.forward(output, y)

    # Calculate mean loss
    data_loss = np.mean(sample_losses)

    # Return loss
    return data_loss

# Corss-entropy loss
class Loss_CategoricalCrossentropy(Loss):

  # forward pass
  def forward(self, y_pred, y_true):

    # Number of samples in a batch
    samples = len(y_pred)

    # Clip data to prevent division by 0, read in book chapter 5 page 18
    # Clip both sides to not drag mean toward any value
    # read more about numpy.clip here: https://numpy.org/doc/stable/reference/generated/numpy.clip.html
    y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

    # Probabilities for target values - 
    # only if categorical labels
    if len(y_true.shape) == 1:
      correct_confidences = y_pred_clipped[
        range(samples),
        y_true,
      ]

    #  Make values - only for one hot encoded labels
    elif len(y_true.shape) == 2:
      correct_confidences = np.sum(
        y_pred_clipped * y_true,
        axis=1,
      )

    # Losses 
    negative_log_likehoods = -np.log(correct_confidences)
    return negative_log_likehoods

  # Implement loss derivative backpropagation in page 45 chapter 9
  def backward(self, dvalues, y_true):
    # Number of samples
    sampels = len(dvalues)

    # Number of labels in every sample
    # We'll use the first sample to count them
    labels = len(dvalues[0])

    # If labels are sparse, turn them into one-hot vector
    if len(y_true.shape) == 1:
        y_true = np.eye(labels)[y_true]

    # Calculate gradient
    self.dinputs = -y_true / dvalues

    # Normalize gradient
    self.dinputs = self.dinputs / sampels

# Softmax classifier - combined Softmax activation
# and cross-entropy loss for faster backward step
class Activation_Softmax_Loss_CategoricalCorssentropy():

  # Create activation and loss function object
  def __init__(self):
    self.activation = Activation_Softmax()
    self.loss = Loss_CategoricalCrossentropy()

  def forward(self, inputs, y_true):
    # Output layer's activation function
    self.activation.forward(inputs)

    # Set the output
    self.output = self.activation.output

    # Calculate and return loss value
    return self.loss.calculate(self.output, y_true)

  # Backward pass
  def backward(self, dvalues, y_true):

    # Number of samples 
    samples = len(dvalues)

    # If labels are one-hot encoded,
    # turn them into discrete values
    if len(y_true.shape) == 2 :
      # argmax with axis 1, will return index the higest value
      y_true = np.argmax(y_true, axis=1)

    # Copy so we can safely modify
    self.dinputs = dvalues.copy()

    # Calculate gradient
    self.dinputs[range(samples), y_true] -= 1

    # Normalize gradient
    self.dinputs = self.dinputs / samples


# Optimizer Stochastic gradient descent Chapter 10
class Optimizer_SGD:
    # Initialize optimizer - set settings,
    #  learning rate of 1. is default for this optimizer
    def __init__(self, learning_rate=1.0):
        self.learning_rate = learning_rate

    # Update parameters
    def update_params(self, layer):
        # Our goal to minimize value and gradient point towards steepest function ascent,
        # thus we substractd learning rate
        layer.weights += -self.learning_rate * layer.dweights
        layer.biases += -self.learning_rate * layer.dbiases


# Optimizer_SGD with learning rate decay, Chapter 10 page 30
class Optimizer_SGD_version2:
  # Initialize optimizer - set settings,
  # learning rate of 1. is default for this optimizer
  def __init__(self, learning_rate=1.0, decay=0.):
    self.starting_learing_rate = learning_rate
    self.current_learning_rate = learning_rate
    self.decay = decay
    self.iterations = 0

  # call once before any parameter updates
  def pre_update_params(self):
    if self.decay:
      self.current_learning_rate = self.starting_learing_rate * (1. / (1 + self.decay * self.iterations))

  # Update parameters
  def update_params(self, layer):
    layer.weights += -self.current_learning_rate * layer.dweights
    layer.biases += -self.current_learning_rate * layer.dbiases

  def post_update_params(self):
    self.iterations += 1

# Optimizer_SGD version 3 with momentum
class Optimizer_SGD_version3:
  # Initialize optimizer - set settings,
  # learning rate of 1. is default for this optimizer
  def __init__(self, learning_rate=1.0, decay=0., momentum=0.):
    self.starting_learing_rate = learning_rate
    self.current_learning_rate = learning_rate
    self.decay = decay
    self.iterations = 0
    self.momentum = momentum

  # call once before any parameter updates
  def pre_update_params(self):
    # if optimizer use Decay Learning Rate
    if self.decay:
      self.current_learning_rate = self.starting_learing_rate * (1. / (1 + self.decay * self.iterations))

  # Update parameters
  def update_params(self, layer):
    # If we use momentum
    if self.momentum:

      # If layer does not contain momentum arrays, create them  array filled with zeros
      if not hasattr(layer, 'weight_momentums'):
        layer.weight_momentums = np.zeros_like(layer.weights)

        # If there is no momentum array for weights
        # The array doesn't exists for biases yet either
        layer.bias_momentums = np.zeros_like(layer.biases)

      # Build weight updates with momentum - take previous
      # updates multiplied by retain factor and update with current gradient
      weight_updates = self.momentum * layer.weight_momentums - \
        self.current_learning_rate * layer.dweights

      # Build bias updates
      bias_updates = self.momentum * layer.bias_momentums - \
        self.current_learning_rate * layer.dbiases

      layer.weight_momentums = weight_updates
      layer.bias_momentums = bias_updates
    
    # Vanila SGD update (as before momentum update)
    else:
      weight_updates = -self.current_learning_rate * layer.dweights
      bias_updates = -self.current_learning_rate * layer.dbiases

    # Update weights and biases using either
    # vanilla or momentum updates
    layer.weights += weight_updates
    layer.biases += bias_updates

  def post_update_params(self):
    self.iterations += 1

