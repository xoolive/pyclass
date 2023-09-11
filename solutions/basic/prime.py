import doctest
import math
import sys

# You may run the following command:
#   python solutions/basic/prime.py 50


def prime(n: int) -> list[int]:
    """Computes all prime numbers below n.
    Computes the sieve of Eratosthenes
    >>> prime(20)
    [1, 2, 3, 5, 7, 11, 13, 17, 19]
    """
    assert n > 0, "Positive integers only"
    p: set[int] = set(range(1, n))
    for i in range(2, int(math.sqrt(n)) + 1):
        p = p - set(x * i for x in range(2, n // i + 1))
    return sorted(p)


if __name__ == "__main__":
    print(doctest.testmod())
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 20
    print(prime(n))
