carburant = carburant.rename(
    columns={
        "maj": "date",
        "nom": "type",
        "valeur": "prix"
    }
)
