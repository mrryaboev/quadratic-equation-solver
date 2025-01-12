import cmath

def solve_quadratic_equation(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0
    Возвращает кортеж из двух корней (возможно комплексных).
    """

    if a == 0:
      if b == 0:
           if c == 0:
               return "Бесконечное число решений"
           else:
                return "Нет решений"
      else:
        return -c/b, -c/b # Линейное уравнение

    delta = (b**2) - 4*(a*c)
    if delta >= 0:
        x1 = (-b - delta**0.5) / (2*a)
        x2 = (-b + delta**0.5) / (2*a)
    else:
         x1 = (-b - cmath.sqrt(delta)) / (2 * a)
         x2 = (-b + cmath.sqrt(delta)) / (2 * a)
    return x1, x2
