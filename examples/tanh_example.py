import numpy as np
from activation_functions import tanh

# Example usage of Tanh activation function
data = np.array([-1, 0, 1, 2])
activated_data = tanh(data)
print("Tanh Activation:", activated_data)
