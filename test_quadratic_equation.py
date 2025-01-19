# test_quadratic_equation.py

import unittest
from quadratic_equation import solve_quadratic_equation
import cmath

class TestQuadraticEquation(unittest.TestCase):

    def test_two_distinct_real_roots(self):
        x1, x2 = solve_quadratic_equation(1, -5, 6)
        self.assertAlmostEqual(x1, 2)
        self.assertAlmostEqual(x2, 3)

    def test_two_equal_real_roots(self):
         x1, x2 = solve_quadratic_equation(1, -4, 4)
         self.assertAlmostEqual(x1, 2)
         self.assertAlmostEqual(x2, 2)

    def test_complex_roots(self):
        x1, x2 = solve_quadratic_equation(1, 1, 1)
        self.assertAlmostEqual(x1, (-0.5-0.8660254037844386j))
        self.assertAlmostEqual(x2, (-0.5+0.8660254037844386j))

    def test_b_equals_zero(self):
        x1, x2 = solve_quadratic_equation(1, 0, -4)
        self.assertAlmostEqual(x1, -2)
        self.assertAlmostEqual(x2, 2)

    def test_c_equals_zero(self):
        x1, x2 = solve_quadratic_equation(1, -5, 0)
        self.assertAlmostEqual(x1, 0)
        self.assertAlmostEqual(x2, 5)

    def test_a_equals_zero(self):
        self.assertIsNone(solve_quadratic_equation(0, 2, 3))

    def test_returns_tuple(self):
      result = solve_quadratic_equation(1, -5, 6)
      self.assertIsInstance(result, tuple)

    def test_returns_none_if_a_is_zero(self):
        self.assertIsNone(solve_quadratic_equation(0, 5, 6))

if __name__ == '__main__':
    unittest.main()
