# page 44
import numpy as np

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
        y_pred_clipped = np.clip(y_pred, 1e-7, 1-1e-7)

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

    def backward(self, dvalues, y_true):
        # Number of samples
        sampels = len(dvalues)

        # Number of labels in every sample
        # We'll use the first sample to count them
        labels = len(dvalues[0])

        # If labels are sparse, turm them into one-hot vector
        if len(y_true.shape) == 1:
            y_true = np.eye(labels)[y_true]

        # Calculate gradient
        self.dinputs = -y_true / dvalues

        # Normalize gradient
        self.dinputs = self.dinputs / sampels
