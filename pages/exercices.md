---
title: Exercices de programmation
documentclass: tufte-handout
classoption: twoside
lang: fr
mainfont: Linux Libertine
mathfont: Asana Math
header-includes:
  - \usepackage{graphicx}
  - \usepackage{marvosym}
  - \usepackage{tikz}
  - \setmonofont[Scale=0.8]{Fira Mono}
  - \renewcommand\allcapsspacing[1]{{\addfontfeature{LetterSpace=15}#1}}
  - \renewcommand\smallcapsspacing[1]{{\addfontfeature{LetterSpace=10}#1}}
  - \usepackage{xpatch}
  - \xapptocmd\ttfamily{\XeTeXinterchartokenstate=0 }{}{}
permalink: /exercices
layout: default
---

## Exercice nº1

Écrire l'expression logique qui est vraie quand $a \in [10, 20]$.

On pourra partir du code Python suivant:

```python
a = 12
```

## Exercice nº2

Écrire un programme qui à partir d'un rayon et d'une hauteur calcule le volume
d'un cône droit. On rappelle la formule $V = \dfrac{\pi r^2 h}{3}$

On pourra partir du code Python suivant:

```python
import math  # accès à math.pi

r = 1
h = 4
```

## Exercice nº3

À partir d'une variable s contenant une chaîne de caractères, écrire
l'expression permettant à partir de cette variable de construire cette même
chaîne avec la première lettre de chaque mot en majuscule, encadrée de
caractères `=`, l'ensemble sur une largeur de 60 caractères.

La [documentation officielle](https://docs.python.org/3/library/string.html) pourrait être utile.

```python
s = "Dark side of the moon"

# Produire la chaîne de caractères suivante
# '===================Dark Side Of The Moon===================='

```

## Exercice nº4

Écrire une fonction qui pour un entier entre 1 et 3999 retourne sa représentation sous forme de nombre romain.

| `I` | `V` | `X` | `L` | `C` | `D` | `M`  |
| :-: | :-: | :-: | :-: | :-: | :-: | :--: |
|  1  |  5  | 10  | 50  | 100 | 500 | 1000 |

```python
# Note: Python 3 permet d'*annoter* les arguments et le retour d'une fonction
# avec des éléments de syntaxe valide. Ces éléments sont *facultatifs*, ignorés
# par le langage. En général, on les utilise pour préciser l'interface des
# fonctions.
# Dans l'exemple suivant, Python comprend "def romain(n):" mais le programmeur
# sait que la fonction prend un entier et retourne une chaîne de caractères.

def romain(n: int) -> str:
    pass
```

## Exercice nº5

Le _mélange de Monge_ d'un paquet de cartes numérotées de 2 à 2n consiste à
démarrer un nouveau paquet avec la carte 1, à placer la carte 2 au-dessus de ce
nouveau paquet, puis la carte 3 au-dessous du nouveau paquet et ainsi de suite
en plaçant les cartes paires au dessus du nouveau paquet et les cartes impaires
au dessous.

Écrire une fonction qui retourne le paquet initial et le paquet mélangé.

```python
# Référence:
# https://docs.python.org/3/tutorial/datastructures.html?highlight=list

def monge(n: int):
    pass
```

## Exercice nº6

Soit une liste contenant des tuples de valeurs (nom, masse, volume), où nom est
le nom d'un élément chimique, masse est une valeur flottante en grammes et
volume une valeur flottante en cm$^3$

```python
lst: list[tuple[str, float, float]] = [
    ("Arsenic", 17.8464, 3.12),
    ("Aluminium", 16.767, 6.21),
    ("Or", 239320, 12400),
]
```

Enregistrer les données de lst dans un fichier texte dont chaque ligne
correspond à un élément, avec le format: `nom = masse volumique g/cm3`

Par exemple:

```text
Arsenic = 5.72 g/cm3
```

Puis écrire une fonction qui prend en entrée un volume et affiche pour chacun
des éléments du fichier `elements.txt` la masse d'un échantillon de cet élément
pour le volume donné, sur le modèle:

```text
Arsenic: 28.60 g
Aluminium: 13.50 g
Or: 96.50 g
```

```python
# Écriture du fichier
from pathlib import Path

with Path("elements.txt").open("w") as fh:
    pass

# Lecture du fichier
def calcule_masse(volume: float) -> None:
    with Path("elements.txt").open("r") as fh:
        pass
```

## Exercice nº7

Écrire un programme qui approche la valeur de la constante mathématique $e$ pour
$n$ assez grand en utilisant la formule suivante:

$$e = \sum_{i=0}^{n} \dfrac{1}{i!}$$

```python
def calcule_e(n: int) -> float:
    pass

# Vérifier la précision du calcul
import math
(math.e - calcule_e(15)) / math.e
```

---

[Lien vers les corrections](corrections)
