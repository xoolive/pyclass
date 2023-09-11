import re


def verify(string: str):
    """Match valid registration numbers.

    >>> verify("AA-229-BY")
    >>> verify("1234-WC-75")
    Traceback (most recent call last):
        ...
    ValueError: Not a valid registration number: 1234-WC-75
    """
    if not re.match(r"[A-Z]{2}-\d{3}-[A-Z]{2}$", string):
        raise ValueError("Not a valid registration number: %s" % string)
