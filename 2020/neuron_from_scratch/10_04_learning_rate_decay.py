# Page 31
# NOTE: The idea of a learning rate decay is to start with a large learning rate, say 1.0 in our case, and
# then decrease it during training.

# NOTE: How Learning Rate Decay works
# We're hoing to udpate the learning rate each step by the reciprocal of step count fraction.
# This fractions is a new hyper-parameter that we'll add to the optimizer, and this new hyper parameter called "learning rate decay"


# NOTE: implementation it takes the step and the decaying ration and multiplication them. The further in training, the bigger the step is and the bigger result of this multiplication
# We then take its reciprocal (the further in training, the lower the value) and multiply the initial learning rate by it.
# Te added 1 make sure that the resulting alhorithm never raises the learning rate. For example, for the first step, we might devide 1 by the learning rate.
# 0.001 for example, which will result in current learning rate of 1000. That's definitely not what we wanted.
# 1 diveded by the 1+fraction ensure that the result, a fraction of the starting learning rate, will always be less than or equal to 1, decreasing over time.
# that's the desired result


#  Implement LR decay basic
def learning_rate_decay_calc(starting_learing_rate, learning_rate_decay, step):
    return starting_learing_rate * (1. / (1 + learning_rate_decay * step))


starting_learing_rate = 1.
learning_rate_decay = 0.1
step = 1

learning_rate = learning_rate_decay_calc(
    starting_learing_rate, learning_rate_decay, step)


print(learning_rate)


# Implement with step 20
step = 20
print("step 20", learning_rate_decay_calc(
    starting_learing_rate, learning_rate_decay, step))

# Let's implement it with loop
for step in range(20):
    learning_rate = learning_rate_decay_calc(
        starting_learing_rate, learning_rate_decay, step)
    print("step ", step, "lr", learning_rate)


# Update SGD Optimizer with LR decay

class Optimizer_SGD:

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
