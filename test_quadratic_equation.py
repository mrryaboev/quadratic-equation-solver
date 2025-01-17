import unittest
from quadratic_solver import solve_quadratic

class TestQuadraticSolver(unittest.TestCase):
    def test_two_roots(self):
        self.assertEqual(solve_quadratic(1, -3, 2), (2.0, 1.0))

    def test_one_root(self):
        self.assertEqual(solve_quadratic(1, 2, 1), (-1.0, -1.0))

    def test_no_real_roots(self):
        self.assertEqual(solve_quadratic(1, 0, 1), "No real roots")

    def test_not_quadratic(self):
        self.assertEqual(solve_quadratic(0, 2, 1), "Not a quadratic equation")

    def test_zero_root(self):
        self.assertEqual(solve_quadratic(1, 1, 0), (0.0, -1.0))

if __name__ == "__main__":
    unittest.main()

