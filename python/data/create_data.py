import xml.etree.ElementTree as tree

import pandas as pd


def iter_pdv(root, stations=False):
    for doc in root.iterfind("pdv"):
        info = doc.attrib.copy()
        info["adresse"] = doc.find("adresse").text
        info["ville"] = doc.find("ville").text
        if stations:
            yield info
        else:
            for prix in doc.iterfind("prix"):
                output = prix.attrib.copy()
                output["id"] = info["id"]
                yield output


with open("/home/xo/Downloads/PrixCarburants_annuel_2016.xml", "r") as f:
    etree = tree.fromstringlist(f.readlines())
    stations = pd.DataFrame(list(iter_pdv(etree, True)))
    stations = stations.set_index("id")
    stations[["adresse", "cp", "ville", "pop"]].to_csv("stations_2016.csv")
    print(stations.head())
    prix = pd.DataFrame(list(iter_pdv(etree, False)))
    prix.valeur = prix.valeur.astype(float) / 1000
    print(prix.head())
    prix.to_csv("prix_2016.csv", index=False)
