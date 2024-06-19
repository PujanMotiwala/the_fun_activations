import unittest
import numpy as np
from activation_functions import tanh

class TestTanh(unittest.TestCase):
    def test_tanh(self):
        data = np.array([-1, 0, 1, 2])
        result = tanh(data)
        expected = np.tanh(data)
        np.testing.assert_array_almost_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
