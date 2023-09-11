---
title: Basic programming
permalink: /exercices
layout: default
---

1. Write the logical expression that is True when $a \in [10, 20]$.

   ```python
   a = 12
   ```

2. Write a program which computes the volume of a cone given a radius and a height.
   Use the formula $V = \dfrac{\pi r^2 h}{3}$

   ```python
   import math  # access to math.pi

   r = 1
   h = 4
   ```

3. Given a variable 's' containing a string, write an expression that, using this variable, constructs the same string with the first letter of each word capitalized, surrounded by '=' characters, all within a width of 60 characters.
   The [official documentation](https://docs.python.org/3/library/string.html) could be of use

   ```python
   s = "Dark side of the moon"

   # Expected result
   # '===================Dark Side Of The Moon===================='
   ```

4. Write a function that, for an integer between 1 and 3999, returns its representation in the form of a Roman numeral.

   | `I` | `V` | `X` | `L` | `C` | `D` | `M`  |
   | :-: | :-: | :-: | :-: | :-: | :-: | :--: |
   |  1  |  5  | 10  | 50  | 100 | 500 | 1000 |

   ```python
   # Python allows you to annotate arguments and return values of a function
   # with  syntactically correct elements. Those are optional, and ignored
   # during the execution. We use them to help documenting functions. Some extra
   # tools can perform consistency checking based on annotations.

   def roman_numeral(n: int) -> str:
       pass
   ```

5. The _Monge shuffle_ of a deck of cards numbered from 2 to 2n consists of starting a new deck with the card 1, placing card 2 above this new deck, then card 3 below the new deck, and so on, placing even-numbered cards above the new deck and odd-numbered cards below.

   Write a function that returns the initial deck and the shuffled deck

   ```python
   # Reference:
   # https://docs.python.org/3/tutorial/datastructures.html?highlight=list

   def monge(n: int):
       pass
   ```

6. Consider a list containing tuples of values (name, mass, volume), where 'name' is the name of a chemical element, 'mass' is a floating-point value in grams, and 'volume' is a floating-point value in cm^3.

   ```python
   lst: list[tuple[str, float, float]] = [
       ("Arsenic", 17.8464, 3.12),
       ("Aluminium", 16.767, 6.21),
       ("Gold", 239320, 12400),
   ]
   ```

   Save the data from 'lst' into a text file where each line corresponds to an element, with the format: `name = density g/cm3`

   For example:

   ```text
   Arsenic = 5.72 g/cm3
   ```

   Then, write a function that takes as input a volume and, for each of the elements in the `elements.txt` file, displays the mass of a sample of that element for the given volume, following the template:

   ```text
   Arsenic: 28.60 g
   Aluminium: 13.50 g
   Gold: 96.50 g
   ```

   ```python
   # Write a file
   from pathlib import Path

   with Path("elements.txt").open("w") as fh:
       pass

   # Read a file
   def compute_mass(volume: float) -> None:
       with Path("elements.txt").open("r") as fh:
           pass
   ```

7. Write a program that approximates the mathematical constant $e$ for a sufficiently large value of $n$ using the following formula:

   $$e = \sum_{i=0}^{n} \dfrac{1}{i!}$$

   ```python
   def compute_e(n: int) -> float:
       pass

   # Check the precision
   import math
   (math.e - calcule_e(15)) / math.e
   ```

8. Write a program that checks if a given string is a palindrome (reads the same forwards and backwards).

   Then, write another program to check if two words are anagrams (the same letters in a different order).  
   Find all the anagrams in a text file.
