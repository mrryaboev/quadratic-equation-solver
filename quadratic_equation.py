# quadratic_equation.py

import cmath

def solve_quadratic_equation(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.

    Args:
        a: Коэффициент при x^2.
        b: Коэффициент при x.
        c: Свободный член.

    Returns:
        Кортеж (x1, x2) с корнями уравнения.
        Возвращает None, если a равно нулю (не квадратное уравнение).
    """
    if a == 0:
        return None  # Не квадратное уравнение

    delta = (b**2) - 4*(a*c)

    if delta >= 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
    else:
        x1 = (-b - cmath.sqrt(delta)) / (2 * a)
        x2 = (-b + cmath.sqrt(delta)) / (2 * a)
    return x1, x2
