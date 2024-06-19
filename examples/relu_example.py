import numpy as np
from activation_functions import relu

# Example usage of ReLU activation function
data = np.array([-1, 0, 1, 2])
activated_data = relu(data)
print("ReLU Activation:", activated_data)
