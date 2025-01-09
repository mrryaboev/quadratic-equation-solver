import cmath

def solve_quadratic_equation(a, b, c):
    """
    Решает квадратное уравнение вида ax^2 + bx + c = 0.

    Args:
        a: Коэффициент при x^2 (не должен быть равен 0).
        b: Коэффициент при x.
        c: Свободный член.

    Returns:
        Кортеж (tuple) с корнями (могут быть комплексными), либо None, если a = 0.
    """
    if a == 0:
        return None  # Если a = 0, то не квадратное уравнение

    delta = b**2 - 4*a*c

    if delta >= 0:
      x1 = (-b - delta**0.5) / (2*a)
      x2 = (-b + delta**0.5) / (2*a)
    else:
      x1 = (-b - cmath.sqrt(delta)) / (2*a)
      x2 = (-b + cmath.sqrt(delta)) / (2*a)

    return x1, x2
