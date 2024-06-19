import unittest
import numpy as np
from activation_functions import leaky_relu

class TestLeakyReLU(unittest.TestCase):
    def test_leaky_relu(self):
        data = np.array([-1, 0, 1, 2])
        result = leaky_relu(data)
        expected = np.where(data > 0, data, data * 0.01)
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
