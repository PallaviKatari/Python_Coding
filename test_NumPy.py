import unittest

import numpy as np

import NumPy


class NumPyTest(unittest.TestCase):
    def test_matrix_multiplication(self):
        expected = np.array([
            [36, 41],
            [64, 73],
        ])
        np.testing.assert_array_equal(NumPy.result, expected)

    def test_matrix_inverse(self):
        expected = np.array([
            [-2.5, 1.5],
            [2.0, -1.0],
        ])
        np.testing.assert_allclose(NumPy.inverse, expected)

    def test_determinant(self):
        self.assertAlmostEqual(NumPy.det, -2.0)


if __name__ == "__main__":
    unittest.main()
