import functools

def horner(string):
    """Horner's method. Equivalent to int(string) for strings.

    >>> horner("12583")
    12583
    >>> horner("1234a")
    Traceback (most recent call last):
        ...
    TypeError: 'a' is not a number
    """
    tab = [x - b"0"[0] for x in string.encode()]
    for i, x in enumerate(tab):
        if x > 9 or x < 0:
            raise TypeError("'%s' is not a number" % string[i])
    return functools.reduce(lambda rec, x: rec * 10 + x, tab, 0)



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
