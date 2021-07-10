import numpy as np
import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

current_time = time.time()
c = np.dot(a, b)
toc = time.time()

print (c)
print("Vectorized version:" + str(1000*(toc-current_time)) + "ms")

#  Without vector
c = 0
for i in range(1000000):
  c += a[i] * b[i]
toc = time.time()

print (c)
print("For loop version:" + str(1000*(toc-current_time)) + "ms")


def sigmoid(x):
    """
    Compute the sigmoid of x

    Arguments:
    x -- A scalar or numpy array of any size

    Return:
    s -- sigmoid(x)
    """
    
    # (≈ 1 line of code)
    # s = 
    # YOUR CODE STARTS HERE
    s = 1/(1+np.exp(-x))
    
    # YOUR CODE ENDS HERE
    
    return s


def sigmoid_derivative(x):
    """
    Compute the gradient (also called the slope or derivative) of the sigmoid function with respect to its input x.
    You can store the output of the sigmoid function into variables and then use it to calculate the gradient.
    
    Arguments:
    x -- A scalar or numpy array

    Return:
    ds -- Your computed gradient.
    """
    
    #(≈ 2 lines of code)
    # s = 
    # ds = 
    # YOUR CODE STARTS HERE
    s = sigmoid(x)
    ds = s*(1-s) 
    # YOUR CODE ENDS HERE
    
    return ds


def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """
    
    # (≈ 1 line of code)
    # v =
    # YOUR CODE STARTS HERE
    v = image.reshape(-1,1)
    
    # YOUR CODE ENDS HERE
    
    return v
