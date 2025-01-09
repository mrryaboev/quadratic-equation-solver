import pytest
import cmath
from quadratic_equation import solve_quadratic_equation

def are_close(x, y, tolerance=1e-9):
    if isinstance(x, complex) or isinstance(y, complex):
        return abs(x - y) < tolerance
    else:
        return abs(x - y) < tolerance

def test_positive_discriminant():
    x1, x2 = solve_quadratic_equation(1, -3, 2)
    assert are_close(x1, 1) and are_close(x2, 2) or are_close(x1, 2) and are_close(x2, 1)
    x1, x2 = solve_quadratic_equation(2, 5, -3)
    assert are_close(x1, -3) and are_close(x2, 0.5) or are_close(x1, 0.5) and are_close(x2, -3)

def test_zero_discriminant():
    x1, x2 = solve_quadratic_equation(1, -4, 4)
    assert are_close(x1, 2) and are_close(x2, 2)
    x1, x2 = solve_quadratic_equation(4, 4, 1)
    assert are_close(x1, -0.5) and are_close(x2, -0.5)

def test_negative_discriminant():
    x1, x2 = solve_quadratic_equation(1, 2, 5)
    assert are_close(x1, complex(-1, -2)) and are_close(x2, complex(-1, 2)) or are_close(x1, complex(-1, 2)) and are_close(x2, complex(-1, -2))

    x1, x2 = solve_quadratic_equation(2, 4, 5)
    assert are_close(x1, complex(-1, -0.5)) and are_close(x2, complex(-1, 0.5)) or are_close(x1, complex(-1, 0.5)) and are_close(x2, complex(-1, -0.5))


def test_a_is_zero():
    assert solve_quadratic_equation(0, 5, 2) is None
    assert solve_quadratic_equation(0, 0, 5) is None

def test_negative_coefficients():
    x1, x2 = solve_quadratic_equation(-1, 3, -2)
    assert are_close(x1, 1) and are_close(x2, 2) or are_close(x1, 2) and are_close(x2, 1)
    x1, x2 = solve_quadratic_equation(-2, -5, 3)
    assert are_close(x1, -3) and are_close(x2, 0.5) or are_close(x1, 0.5) and are_close(x2, -3)


def test_fractional_coefficients():
     x1, x2 = solve_quadratic_equation(0.5, 1.5, -1)
     assert are_close(x1, 0.5) or are_close(x1, -4.5)
     assert are_close(x2, 0.5) or are_close(x2, -4.5)

def test_large_coefficients():
    x1, x2 = solve_quadratic_equation(100000, 100000, 10000)
    assert are_close(x1, -0.1) and are_close(x2, -0.1)
    x1,x2 = solve_quadratic_equation(0.00001, 0.00001, 0.00001)
    assert are_close(x1, complex(-0.5, -0.8660254037844386)) or are_close(x1, complex(-0.5, 0.8660254037844386))
    assert are_close(x2, complex(-0.5, -0.8660254037844386)) or are_close(x2, complex(-0.5, 0.8660254037844386))
