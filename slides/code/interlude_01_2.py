import doctest
import math


def prime(n: int) -> set:
    """Computes all prime numbers below n.

    Computes the sieve of Eratosthenes
    >>> prime(20)
    {1, 2, 3, 5, 7, 11, 13, 17, 19}
    """
    p = set(range(1, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        p = p - set(x * i for x in range(2, n // i + 1))
    return p


if __name__ == "__main__":
    print(doctest.testmod())
