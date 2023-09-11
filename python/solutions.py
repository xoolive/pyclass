# ruff: noqa: E402

# %%
# Exercice 5


# Don't feel bad if you cannot figure the annotation for the return value here
def monge(n: int) -> tuple[list[int], list[int]]:
    initial = list(range(1, 2 * n + 1))
    monge = [1]
    for i in range(2, 2 * n + 1):
        if i % 2 == 0:  # pair
            monge.insert(0, i)
        else:
            monge.append(i)

    return initial, monge


print(monge(5))
# ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 8, 6, 4, 2, 1, 3, 5, 7, 9])

# %%
# Exercice 6

lst: list[tuple[str, float, float]] = [
    ("Arsenic", 17.8464, 3.12),
    ("Aluminium", 16.767, 6.21),
    ("Gold", 239320, 12400),
]

from pathlib import Path

with Path("elements.txt").open("w") as fh:
    for name, mass, volume in lst:
        density = mass / volume
        fh.write("{} = {:.2f} g/cm3\n".format(name, density))


def compute_mass(volume: float) -> None:
    with Path("elements.txt").open("r") as fh:
        for line in fh:
            items = line.split("=")
            name = items[0].strip()
            density = float(items[1].split()[0])
            print("{}: {:.2f} g".format(name, density * volume))


compute_mass(5)

# %%

# Exercice 7

import math


def compute_e(n: int) -> float:
    e = 1.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        e += 1 / fact
    return e


(math.e - compute_e(15)) / math.e

# Euler formula for pi (similar exercice)
# $\pi = 1 + \frac{1}{3} + \frac{1 · 2}{1 · 3} + \frac{1 · 2 · 3}{1 · 3 · 5}  + \cdots$


def compute_pi(n: int) -> float:
    pi2 = 1.0
    num = 1
    denum = 1
    for i in range(1, n + 1):
        num *= i
        denum *= 2 * i + 1
        pi2 += num / denum
    return 2 * pi2


(math.pi - compute_pi(30)) / math.pi

# %%

# Exercice 8


def palindrome(word: str) -> bool:
    return word == word[::-1]


def anagram(word1: str, word2: str) -> bool:
    return "".join(sorted(word1)) == "".join(sorted(word2))


from pathlib import Path

words = Path("common-english-words.txt").read_text().split()
# %%
from collections import defaultdict

anagrams = defaultdict(list)
for word in words:
    anagrams["".join(sorted(word))].append(word)

# %%
# Remove all elements with no anagrams
list(
    anagram_list for anagram_list in anagrams.values() if len(anagram_list) > 1
)
# %%
# Sorted by number of anagrams of the same word
sorted(
    (
        anagram_list
        for anagram_list in anagrams.values()
        if len(anagram_list) > 1
    ),
    key=len,
)
