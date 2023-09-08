---
layout: default
title: Advanced data structures
permalink: /structures
---

[↑ Home](.) \| [>> Next](numpy)

<div class="alert alert-warning">
<b>Warning</b> &nbsp;&nbsp; This section is optional. If you run after time, feel free to skip to <a href="numpy">next section</a>.
</div>

## Advanced data structures

### `defaultdict`: dictionaries with default values

The `defaultdict` is a particular dictionaries with a default _factory_ method used when accessing a key not present in the dictionary.

The idea behind the structure is to avoid checks like:

```python
# Look Before You Leap (LBYL) style
if elt in references.keys():
    references[elt].add(something)
else:
    references[elt] = {something}
```

or

```python
# More pythonic, faster
# Easier to Ask for Forgiveness than Permission (EAFP) style
try:
    references[elt].add(something)
except KeyError:
    references[elt] = {something}
```

with the code of the default case only:

```python
references[elt].add(something)
```

This is made possible by describing how to create a default value in the dictionary. Here, the default case is an empty `set` created by `set()`:

```python
from collections import defaultdict

references = defaultdict(set)
```

<div class="alert alert-info">
<b>Exercice</b> &nbsp;&nbsp; Implement the word count exercice from previous section with the proper <code>defaultdict</code> instance. 
</div>

### `Counter`: dictionaries for counting objects

A `Counter` is a particular `defaultdict` which has been designed for counting objects passed as an iterable:

```python
>>> from collections import Counter
>>> Counter(random.randint(0, 5) for _ in range(100))
Counter({4: 22, 2: 19, 1: 18, 3: 18, 5: 15, 0: 8})
```

<div class="alert alert-info">
<b>Exercice</b> &nbsp;&nbsp; Implement the word count exercice from previous section with the proper <code>Counter</code> instance. 
</div>

### `dataclass`

Dataclasses are facilities to create objects looking like dictionaries, with more flexibility with respect to mutable and non mutable entries.

```python
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
```

```python
>>> Person()  # constructor automatically generated for you
Traceback (most recent call last):
  ...
TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
>>> p = Person("John", 30)
>>> p
Person(name='John', age=30)
>>> p.name
'John'
>>> p.name = "Peter"  # mutable
>>> p
Person(name='Peter', age=30)
```

Since dataclasses are mutable, they cannot be _hashed_ and used in sets or as keys in dictionaries:

```python
>>> {p}
Traceback (most recent call last):
  ...
TypeError: unhashable type: 'Person
```

However, dataclasses provide a `frozen` option, where all fields become immutable: this allows instances to be _hashed_.

```python
@dataclass(frozen=True)
class Person:
    name: str
    age: int
```

```python
>>> p = Person("John", 30)
>>> {p}  # hashable
{Person(name='John', age=30)}
>>> p.name = "Peter"  # immutable
Traceback (most recent call last):
  ...
dataclasses.FrozenInstanceError: cannot assign to field 'name'
```

A dataclass can be extended with usual methods:

```python
@dataclass
class Person:
    name: str
    age: int

    def underage(self) -> bool:
        self.age <= 18
```

```python
>>> p = Person("John", 30)
>>> p.underage()
False
```

Fields may be hidden from the default representation.  
Also, they may be described with _factories_ to represent default values.

```python
from dataclasses import field

@dataclass
class Person:
    name: str
    age: int = field(repr=False)
    friends: list[str] = field(default_factory=list)
```

```python
>>> p = Person("John", 30)
>>> p.friends.append("Peter")
>>> p
Person(name='John', friends=['Peter'])  # age is hidden here
```

<div class="alert alert-success">
<b>Shameless advertising</b> &nbsp;&nbsp; You will find more details and examples (in French) about advanced structures in Chapter&nbsp;4 of the <a href="/python">reference book</a>.

<img class="giphy" src="https://media.giphy.com/media/34ZNcoaN5u4hi/giphy.webp"/>
</div>

[↑ Home](.) \| [>> Next](numpy)
