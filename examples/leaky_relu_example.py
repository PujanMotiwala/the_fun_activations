import numpy as np
from activation_functions import leaky_relu

# Example usage of Leaky ReLU activation function
data = np.array([-1, 0, 1, 2])
activated_data = leaky_relu(data)
print("Leaky ReLU Activation:", activated_data)
