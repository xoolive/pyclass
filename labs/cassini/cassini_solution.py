import math
from collections import UserDict


class Distances(UserDict):
    """Structure de données qui facilite l'accès aux distances.

    Cette structure de données vous permettra de stocker les distances entre
    les points repères utilisés par Cassini lors du calcul de la méridienne de
    Paris.

    Nous nous familiariserons avec ce formalisme plus tard dans la semaine.
    Pour le moment, il vous suffit de savoir que cette structure se comporte
    comme un dictionnaire dont la clé est une paire de deux chaînes de
    caractères interchangeables.

    Une fois la distance entre a et b remplie, vous pourrez interroger la
    structure pour récupérer la distance entre b et a.

    >>> distances = Distances()
    >>> distances["Juvisy", "Villejuif"] = 5748
    >>> distances["Juvisy", "Villejuif"]
    5748
    >>> distances["Villejuif", "Juvisy"]
    5748
    """

    def __getitem__(self, key):
        """Accès à d[key]"""
        if key[0] > key[1]:
            return super().__getitem__((key[1], key[0]))
        else:
            return super().__getitem__(key)

    def __setitem__(self, key, item):
        """Assignation de d[key] = item"""
        if key[0] > key[1]:
            super().__setitem__((key[1], key[0]), item)
        else:
            super().__setitem__(key, item)


distances = Distances()
# Ligne de base
distances["Juvisy", "Villejuif"] = 5748
# Ligne de base
distances["Sig.Nord", "Sig.Sud"] = 7928 + 5 / 6

# Pour la deuxième question: « La Tour de Montlhery décline à l'Occident de la
# Méridienne de l'Observatoire de 11°58′28″ »


with open("data/triangles.txt", "r") as fh:  # fh = open("...", "r")
    cumul = []
    i = -1
    #    for i, line in enumerate(fh.readlines()):
    for line in fh.readlines():
        i += 1
        if i % 4 != 3:
            city, deg, mn, sec = (
                line.replace("°", " ")
                .replace("′", " ")
                .replace("″", " ")
                .split()
            )
            cumul.append(
                (
                    city,
                    math.pi / 180 * (int(deg) + int(mn) / 60 + int(sec) / 3600),
                )
            )

        else:
            (a, alpha), (b, beta), (c, gamma) = cumul
            distances[a, c] = distances[a, b] * math.sin(beta) / math.sin(gamma)
            distances[b, c] = (
                distances[a, b] * math.sin(alpha) / math.sin(gamma)
            )

            cumul.clear()


total_distance = 0

with open("data/inclinaisons.txt", "r") as fh:
    for line in fh.readlines():
        line = line.strip()
        if len(line) == 0:
            continue

        v1, v2, deg, mn, sec = (
            line.replace("°", " ").replace("′", " ").replace("″", " ").split()
        )
        angle = math.pi / 180 * (int(deg) + int(mn) / 60 + int(sec) / 3600)
        total_distance += math.cos(angle) * distances[v1, v2]

angles = [
    2 + 11 / 60 + 50 / 3600 + 17 / (60**3),
    1 + 47 / 60 + 7 / 3600 + 20 / (60**3),
    2 + 43 / 60 + 51 / 3600 + 5 / (60**3),
    1 + 39 / 60 + 11 / 3600 + 12 / (60**3),
]

print(total_distance * 1.949 / (sum(angles) * math.pi / 180))
