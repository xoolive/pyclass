---
layout: default
title: List comprehensions
permalink: /comprehensions
---

## List comprehensions

You have two options to open the `list_comprehensions.ipynb` file (in the `notebooks/` folder):

- with Jupyter Lab: open a terminal and enter the following commands:

  ```bash
  conda activate pyclass
  jupyter lab
  ```

- with Visual Studio Code: open the notebook as a regular file. If asked, specify you need to use the `pyclass` environment.

## Exercices using list comprehensions and iterators

1. Given a list of words, create a list that contains the length of these words.

2. Given a list of potentially duplicated words, create a sorted list of unique words.

3. Given a sentence, count the number of occurrences of each vowels in the text. (Think first about the structure you want to use)

4. Write a set comprehension that contains all prime numbers less than 50.

5. Given two lists of numbers, create a new list containing the pairwise sum of elements.

6. Given a matrix as a list of list, use `zip()` to transpose the matrix.

7. Given a list of elements, use `enumerate()` to find the index of the smallest item in the list.

8. Given two list of integers, create a list of interleaved elements.

   ```python
   >>> interleave(["un", "deux", "trois"], [1, 2, 3])
   ["un", 1, "deux", 2, "trois", 3]
   ```

[↑ Home](.) \| [>> Next](pandas_iterate)
