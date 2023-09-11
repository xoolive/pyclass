import doctest


def roman_numeral(n: int) -> str:
    """Returns the Roman numeral representation of an integer.

    >>> roman_numeral(476)
    'CDLXXVI'
    >>> roman_numeral(778)
    'DCCLXXVIII'
    >>> roman_numeral(1229)
    'MCCXXIX'
    >>> roman_numeral(1453)
    'MCDLIII'
    >>> roman_numeral(1492)
    'MCDXCII'
    >>> roman_numeral(1515)
    'MDXV'
    >>> roman_numeral(1789)
    'MDCCLXXXIX'
    >>> roman_numeral(1945)
    'MCMXLV'
    >>> roman_numeral(1989)
    'MCMLXXXIX'
    >>> roman_numeral(2019)
    'MMXIX'
    """
    assert 1 <= n <= 3999
    cumul = ""

    while n >= 1000:
        cumul += "M"
        n -= 1000

    if n >= 900:
        cumul += "CM"
        n -= 900

    if n >= 500:
        cumul += "D"
        n -= 500

    if n >= 400:
        cumul += "CD"
        n -= 400

    while n >= 100:
        cumul += "C"
        n -= 100

    if n >= 90:
        cumul += "XC"
        n -= 90

    if n >= 50:
        cumul += "L"
        n -= 50

    if n >= 40:
        cumul += "XL"
        n -= 40

    while n >= 10:
        cumul += "X"
        n -= 10

    if n >= 9:
        cumul += "IX"
        n -= 9

    if n >= 5:
        cumul += "V"
        n -= 5

    if n >= 4:
        cumul += "IV"
        n -= 4

    while n >= 1:
        cumul += "I"
        n -= 1

    return cumul


if __name__ == "__main__":
    print(doctest.testmod())
