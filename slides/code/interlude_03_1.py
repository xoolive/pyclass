"""Specifications and unit tests for the exercice.

>>> e = Container()
>>> for v in [1, 2, 'a', 3.14]:
...     e.extend(v)
>>> e.add(3.14)
>>> e.add(2)
>>> e.add(2)
>>> e
Container({2, 3.14})

>>> e.add(5)
Traceback (most recent call last):
    ...
ValueError: Value '5' is not allowed.

>>> e.extend(5)
>>> e.add(5)

>>> e.restrict(1)
>>> e.restrict(2)
Traceback (most recent call last):
    ...
ValueError: Value '2' is present in the Container.
"""


class Container(set):
    def __init__(self):
        self.allowedValues = set()
        super().__init__()

    def extend(self, v):
        """Add a value in the list of allowed values."""
        self.allowedValues.add(v)

    def add(self, v):
        """Add a value in the set."""
        if v not in self.allowedValues:
            raise ValueError("Value '%s' is not allowed." % v)
        super().add(v)

    def restrict(self, v):
        """Remove a value from the list of allowed values."""
        if v in self:
            raise ValueError("Value '%s' is present in the Container." % v)
        self.allowedValues.remove(v)
