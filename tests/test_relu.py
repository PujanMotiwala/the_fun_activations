import unittest
import numpy as np
from activation_functions import relu

class TestReLU(unittest.TestCase):
    def test_relu(self):
        data = np.array([-1, 0, 1, 2])
        result = relu(data)
        expected = np.array([0, 0, 1, 2])
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
