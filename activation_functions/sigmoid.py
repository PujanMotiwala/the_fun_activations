import numpy as np

def sigmoid(x):
    """
    Compute the Sigmoid activation function.

    Parameters:
    x (numpy.ndarray): Input array.

    Returns:
    numpy.ndarray: Output array with Sigmoid applied element-wise.
    """
    return 1 / (1 + np.exp(-x))
