---
layout: default
title: Basic types and arithmetic
permalink: /basic
---

> Code snippets may either be:
>
> - typesetted with syntax coloring, or
> - prefixed with the `>>>` sign, which imitates the behaviour of the REPL[^1] interpreter.
>
> You are encouraged to copy paste the snippets into your Python interpreter to become familiar with its behaviour.

[^1]: Read, Evaluate, Print, Loop (REPL) is the common behaviour of interactive shells, like the Python interpreter.

### Some elements of syntax

Python is a dynamically typed language: variables are untyped, but **values are**. In the following example, variable `a` can _point_ to an integer, then to a string. However values `12` and `"hello world"` are resp. of types `int` and `str`.

```python
>>> a = 12
>>> type(a)
int
>>> a = "hello world"
>>> type(a)
str
```

It is considered good practice to add type annotations to your code. We will see later how they can help writing a correct programme. Annotations are made of **any valid Python syntax**: they are placed after a column sign and are **ignored at runtime**. All the following annotations are valid.

```python
a: int = 12
b: str = "hello world"
distance: float = 7.3
distance: "nautical_miles" = 7.3
```

At this point, consider type annotations as an additional way to comment or document your code with useful information.

The return type of functions can also be annotated after the `->` symbol. In the following example, the `fact` function takes an integer as a parameter and returns an integer.

```python
def fact(n: int) -> int:
    """Returns the factorial of n.

    >>> fact(6)
    720
    >>> [fact(n) for n in range(6)]
    [1, 1, 2, 6, 24, 120]

    n is negative, a ValueError exception is raised:

    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be a positive integer
    """
    res = 1
    if n < 0:
        raise ValueError("n must be a positive integer")
    while n > 0:
        res = n * res
        n = n - 1
    return res
```

You may note here that:

- blocks are defined by indentation. [PEP 8](https://www.python.org/dev/peps/pep-0008/) recommends indentation blocks made of 4 spaces;

<img class="giphy" src="https://media.giphy.com/media/l0IylSajlbPRFxH8Y/giphy.webp">

- A function definition may start by a string value, not assigned to any variables. This is the _documentation_ of the function, called _docstrings_;

- Docstrings may contain example codes with the expected result of the execution. These tests may be executed with the `doctests` module.

- The ellipsis literal `...` in the docstring matches any string.

<div class="alert alert-info">
<b>Exercice</b> &nbsp;&nbsp; Copy the code above in a new file <code>fact.py</code> (in Visual Studio Code).<br/> Add the following import at the top of the file:

<div class="highlight">
<pre class="highlight">
<code>import doctest</code>
</pre>
</div>
and the following snipped at the bottom:<br/>
<div class="highlight">
<pre class="highlight">
<code>if __name__ == "__main__":
    print(doctest.testmod())</code>
</pre>
</div>

<ul>
<li>Execute the file and check the tests are correct.</li>
<li>Add examples (tests) so that the following examples return a meaningful value or exception.<br/> There is no unique answer here, it's really up to you.
<div class="highlight">
<pre class="highlight">
<code>fact("12")
fact(3.14)
fact([1, 4, 7])</code>
</pre>
</div>

</li>
</ul>
</div>

### Basic types and arithmetic

Python offers a number of data structures with syntactic and algorithmic facilities. The art of programming consists in choosing (and adapting) the most appropriate data structure.

- In Python, the type `str` (**string**) consists in a sequence of Unicode characters. This means that any accentuated character, in any language, even emoji 🦄 can all be concatenated in a valid string. Only the `\` (backslash) character must be _escaped_ (add an extra `\` before) because it is used to _escape_ many characters (`\n` for a carriage return, `\t` for a tabulation, etc.) The `r` prefix deactivates the interpretation of the backslash.

  ```python
  >>> str()
  ''
  >>> "bon" + "jour"
  'bonjour'
  >>> "你好" + " (nĭ hăo)" + "☀️"
  '你好 (nĭ hăo) ☀️'
  ```

  Triple quotes allow for multiline strings:

  ```python
  >>> a: str = """Hello.
      How are you?"""
  'Hello.\nHow are you?'
  ```

  Strings may be indexed and sliced:

  ```python
  >>> a[0]
  'H'
  >>> a[2:4]
  'll'
  >>> a[-1]
  '?'
  >>> a[-8:]
  'are you?'
  ```

  Other common useful operations:

  ```python
  >>> b = a = "heLLo"
  >>> (a + " ") * 2
  'heLLo heLLo '
  >>> len(a)
  5
  >>> a.capitalize()
  'Hello'
  >>> " hello ".strip()
  'hello'
  >>> "hello y’all".split()
  ['hello', 'y’all']
  ```

  However, strings are **not mutable**:

  ```python
  >>> "hello"[1] = "a"
  Traceback (most recent call last):
    File "<input>", line 1, in <module>
      "hello"[1] = "a"
  TypeError: 'str' object does not support item assignment
  ```

- **Tuples** are _immutable_ containers that concatenate values of heterogeneous types. They are defined with the comma operator. The tuple is always displayed with round brackets. A tuple with a single element requires a final comma. An empty tuple require brackets but the explicit constructor helps.

  ```python
  >>> tuple()
  ()
  >>> latlon: tuple = 43.6, 1.45
  >>> latlon
  (43.6, 1.45)
  >>> 1,
  (1,)
  >>> # tuple unpacking
  >>> lat, lon = latlon
  >>> lat
  43.6
  ```

  Tuple unpacking requires as many elements on the left and right sides of the equal sign. You can make an unused variable explicit with the `_` sign. If many such variables are unnecessary, you can group them with the `*` unpacking operator.

  ```python
  >>> lat, _ = latlon  # silent variable
  >>> ten_first = tuple(range(10))
  >>> ten_first
  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
  >>> zero, *_, nine = ten_first
  >>> zero, nine
  0, 9
  ```

- **Lists** are sequential, _mutable_ containers for heterogeneous values. This structure is very intuitive: its rich set of associated methods, esp. for sorting and searching, makes it a structure of choice by default for beginners.

  ```python
  >>> list()
  []
  >>> a: list = [1, "deux", 3.0]
  >>> a[0]
  1
  >>> len(a)
  3
  >>> a.append(1)
  >>> a
  [1, 'deux', 3.0, 1]
  >>> a.count(1)
  2
  >>> 3 in a
  True
  >>> a[1] = 2
  >>> a
  [1, 2, 3.0, 1]
  >>> a.sort()
  >>> a
  [1, 1, 2, 3.0]
  >>> a[1:3]
  [1, 2]
  ```

  _List comprehensions_ are a comfortable mechanism to construct lists. For example:

  ```python
  >>> [i for i in range(5)]
  [0, 1, 2, 3, 4]
  >>> list(i for i in range(5))
  [0, 1, 2, 3, 4]
  >>> list(range(5))
  [0, 1, 2, 3, 4]

  >>> [str(i) for i in range(5)]
  ['0', '1', '2', '3', '4']
  >>> [i ** 2 for i in range(5)]
  [0, 1, 4, 9, 16]
  >>> [i ** 2 for i in range(5) if i & 1 == 0]  # smarter than i % 2 == 0
  [0, 4, 16]
  >>> [x.upper() for x in "hello"]  # even with strings
  ['H', 'E', 'L', 'L', 'O']
  ```

  The `sorted` built-in function creates a new sorted list based on values passed in parameters as an iterable structure or a generator. We will insist on this later.

  ```python
  >>> sorted(i ** 2 for i in range(-5, 5))
  [0, 1, 1, 4, 4, 9, 9, 16, 16, 25]
  ```

- **Sets** are sequential containers of unique elements. They can be constructed by value enumeration, from an iterable structure (lists, strings, etc.) or by comprehension.

  ```python
  >>> set()
  set()
  >>> s = {1, 2, 3, 1}
  >>> s
  {1, 2, 3}
  >>> set("coucou")
  {'c', 'o', 'u'}
  >>> set(i ** 2 for i in (-2, -1, 0, 1, 2))
  {0, 1, 4}
  ```

  A set may be modified by adding and removing values. Set arithmetics is based on usual operators for union `|`, intersection `&`, symmetric difference `^` (the `xor` operator in logics) and difference `-`. The `+` operator is undefined.

  ```python
  >>> s.add(4)
  >>> s
  {1, 2, 3, 4}
  >>> s.remove(4)
  >>> s
  {1, 2, 3}
  >>> s.pop(), s
  (1, {2, 3})
  >>> s1 = set(range(3))
  >>> s2 = set(range(0, -3, -1))
  >>> s1, s2
  ({0, 1, 2}, {0, -1, -2})
  >>> s1 | s2  # union
  {0, 1, 2, -2, -1}
  ```

- **Dictionaries** (the `dict` type) are hash tables along the key/value model. All values used as keys must be _hashable_. Dictionaries are mutable: you are free to add and remove new keys and replace values. This structure lies at the core of the implementation of the Python language, so they are particularly optimised in terms of performance.

  ```python
  >>> tour_eiffel = {
          "latitude": 48.8583,
          "longitude": 2.2945,
          "nom": "Tour Eiffel",
          "ville": "Paris",
      }
  >>> tour_eiffel["pays"] = "France"
  >>> point = dict(latitude=43.6, longitude=1.45)  # équivalent
  >>> point
  {'latitude': 43.6, 'longitude': 1.45}
  >>> "latitude" in point
  True
  ```

  The `.get()` method allows you to define a default fallback value if the key is not available in the dictionary:

  ```python
  >>> altitude = point.get("altitude", 0)
  >>> altitude
  0
  ```

  Common accessors are:

  ```python
  >>> point.keys()
  dict_keys(['latitude', 'longitude'])
  >>> point.values()
  dict_values([43.6, 1.45])
  >>> point.items()
  dict_items([('latitude', 43.6), ('longitude', 1.45)])
  >>> dict((key.upper(), value) for (key, value) in point.items())
  {'LATITUDE': 43.6, 'LONGITUDE': 1.45}
  ```

  The prefix operator `**` unpacks dictionaries (remember the `*` operator for tuples). You can use it to update a dictionary or to concatenate two dictionaries (also possible with the union operator `|`)

  ```python
  >>> {**point, **{"pays": "France", "longitude": 1.45}}
  {'latitude': 43.6, 'longitude': 1.45, 'pays': 'France'}
  >>> point | {"pays": "France", "longitude": 1.45}
  {'latitude': 43.6, 'longitude': 1.45, 'pays': 'France'}
  ```

### Exercices

<img class="giphy" src="https://media.giphy.com/media/toXKzaJP3WIgM/giphy.webp">

All exercices are to be implemented in single files. Solutions are located in the `solutions/basic/` folder.

1. Write a function returning the Roman numeral representation of any integer between 1 and 3999.  
   Test your function with the following numbers:

   - 476: `"CDLXXVI"`
   - 1515: `"MDXV"`
   - 1789: `"MDCCLXXXIX"`

2. Write a function returning all prime integers below `n` (integer). Annotate your function and local variables with types and run tests with the `doctest` module.  
   Hint: [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), then ask yourself what is the most appropriate structure to handle this.

3. Find the `lorem-ipsum.txt` file in the `data/` folder. Count the occurrences of all words in the text, and **print** the 10 most frequent words with their number of occurrences.  
   You may start your code based on the following snippet:

   ```python
   from pathlib import Path

   def main(filename: str) -> None:
       txt = Path(filename).read_text()

   if __name__ == "__main__":
       main("data/lorem_ipsum.txt")
   ```

[↑ Home](.) \| [>> Next](structures)

---

### Footnotes
