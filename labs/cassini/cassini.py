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
