import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Compute the Leaky ReLU (Rectified Linear Unit) activation function.

    Parameters:
    x (numpy.ndarray): Input array.
    alpha (float): Slope of the function for x < 0.

    Returns:
    numpy.ndarray: Output array with Leaky ReLU applied element-wise.
    """
    return np.where(x > 0, x, x * alpha)
