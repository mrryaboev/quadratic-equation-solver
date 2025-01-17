import pytest
from quadratic_equation import solve_quadratic_equation # Замените your_module_name на имя вашего файла


def test_two_distinct_roots():
    assert solve_quadratic_equation(1, -5, 6) == [2.0, 3.0]

def test_two_equal_roots():
    assert solve_quadratic_equation(1, -4, 4) == [2.0]

def test_two_equal_roots_b_zero():
    assert solve_quadratic_equation(1, 0, -9) == [-3.0, 3.0]

def test_two_equal_roots_a_zero_b_zero():
    assert solve_quadratic_equation(4, 0, 0) == [0.0]

def test_no_real_roots():
    result = solve_quadratic_equation(1, 1, 1)
    assert len(result) == 2
    assert isinstance(result[0], complex)
    assert isinstance(result[1], complex)

def test_a_zero_not_quadratic():
    result = solve_quadratic_equation(0, 5, -2)
    assert result == [0]

def test_a_zero_b_zero_c_not_zero():
  assert solve_quadratic_equation(0, 0, 2) == []

def test_a_zero_b_zero_c_zero():
    assert solve_quadratic_equation(0, 0, 0) is None

def test_large_coefficients():
    assert solve_quadratic_equation(1000, -2000, 1000) == [1.0]

def test_small_coefficients():
  roots = solve_quadratic_equation(0.001, -0.002, 0.001)
  assert len(roots) == 1
  assert abs(roots[0] - 1.0) < 1e-6


def test_invalid_input_string():
    assert solve_quadratic_equation("a", 2, 3) is None

def test_invalid_input_none():
    assert solve_quadratic_equation(1, None, 3) is None
