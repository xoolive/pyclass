import doctest
import math


def area(x: float) -> float:
    """Computes the area of an equilateral triangle.

    >>> area(2)
    1.7320508075688772
    """
    return x * x * math.sqrt(3) / 4


if __name__ == "__main__":
    print(doctest.testmod())
