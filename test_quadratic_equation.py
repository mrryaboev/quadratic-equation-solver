import pytest
from quadratic_equation import solve_quadratic_equation

def test_two_real_roots():
    x1, x2 = solve_quadratic_equation(1, -3, 2)
    assert x1 == 1.0
    assert x2 == 2.0

def test_one_real_root():
    x1, x2 = solve_quadratic_equation(1, -4, 4)
    assert x1 == 2.0
    assert x2 == 2.0

def test_complex_roots():
    x1, x2 = solve_quadratic_equation(1, 2, 5)
    assert x1 == (-1+2j)
    assert x2 == (-1+2j)

def test_integer_coefficients():
    x1, x2 = solve_quadratic_equation(2, -4, 2)
    assert x1 == 1.0
    assert x2 == 1.0

def test_float_coefficients():
    x1, x2 = solve_quadratic_equation(0.5, -1.5, 1)
    assert x1 == 1.0
    assert x2 == 2.0

def test_a_equal_zero_no_solution():
     assert solve_quadratic_equation(0, 0, 1) == 'Нет решений'

def test_a_equal_zero_inf_solutions():
     assert solve_quadratic_equation(0, 0, 0) == 'Бесконечное число решений'

def test_a_equal_zero_linear():
     x1, x2 = solve_quadratic_equation(0, 2, 2)
     assert x1 == -1.0
     assert x2 == -1.0

def test_large_coefficients():
    x1, x2 = solve_quadratic_equation(1000, -3000, 2000)
    assert x1 == 1.0
    assert x2 == 2.0
    
def test_small_coefficients():
    x1, x2 = solve_quadratic_equation(0.001, -0.003, 0.002)
    assert x1 == 1.0
    assert x2 == 2.0

def test_invalid_input():
    with pytest.raises(TypeError):
        solve_quadratic_equation("a", "b", "c")
