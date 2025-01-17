import cmath
import math


def solve_quadratic_equation(a, b, c):
    """Решает квадратное уравнение ax² + bx + c = 0.

    Args:
      a: Коэффициент при x².
      b: Коэффициент при x.
      c: Свободный член.

    Returns:
      Список корней уравнения, если они есть.
      Пустой список, если корней нет.
      None в случае некорректных входных данных
    """
    if not all(isinstance(x, (int, float)) for x in [a, b, c]):
        print("Ошибка: Коэффициенты должны быть числами.")
        return None
    if a == 0:

                
                return [0]
            
    

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        return [x1, x2]
    elif discriminant == 0:
        x = -b / (2 * a)
        return [x]
    else:
        x1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        x2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return [x1, x2]


def get_user_input():
    """Получает коэффициенты a, b, c от пользователя."""
    while True:
        try:
            a = float(input("Введите коэффициент a: "))
            b = float(input("Введите коэффициент b: "))
            c = float(input("Введите коэффициент c: "))
            return a, b, c
        except ValueError:
            print("Ошибка: Пожалуйста, введите числа.")


if __name__ == "__main__":
    a, b, c = get_user_input()
    roots = solve_quadratic_equation(a, b, c)

    if roots is None:
        pass
    elif roots:
        if len(roots) == 1:
            print("Уравнение имеет один корень:", roots[0])
        elif len(roots) == 2 and isinstance(roots[0], complex) or isinstance(roots[1], complex):
            print("Уравнение имеет два комплексных корня:", roots[0], roots[1])
        else:
            print("Уравнение имеет два корня:", roots[0], roots[1])
    else:
        print("Уравнение не имеет вещественных корней.")
