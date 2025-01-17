import math
from typing import Tuple, Union

def solve_quadratic(a: float, b: float, c: float) -> Union[str, Tuple[float, float]]:
    if a == 0:
        return "Not a quadratic equation"
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "No real roots"
    elif discriminant == 0:
        root = -b / (2*a)
        return (root, root)
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)

