import numpy as np

def tanh(x):
    """
    Compute the Tanh (Hyperbolic Tangent) activation function.

    Parameters:
    x (numpy.ndarray): Input array.

    Returns:
    numpy.ndarray: Output array with Tanh applied element-wise.
    """
    return np.tanh(x)
