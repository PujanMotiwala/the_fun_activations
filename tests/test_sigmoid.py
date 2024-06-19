import unittest
import numpy as np
from activation_functions import sigmoid

class TestSigmoid(unittest.TestCase):
    def test_sigmoid(self):
        data = np.array([-1, 0, 1, 2])
        result = sigmoid(data)
        expected = 1 / (1 + np.exp(-data))
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
