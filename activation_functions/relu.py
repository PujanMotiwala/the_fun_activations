import numpy as np

def relu(x):
    """
    Compute the ReLU (Rectified Linear Unit) activation function.

    Parameters:
    x (numpy.ndarray): Input array.

    Returns:
    numpy.ndarray: Output array with ReLU applied element-wise.
    """
    return np.maximum(0, x)
