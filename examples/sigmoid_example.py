import numpy as np
from activation_functions import sigmoid

# Example usage of Sigmoid activation function
data = np.array([-1, 0, 1, 2])
activated_data = sigmoid(data)
print("Sigmoid Activation:", activated_data)
