carburant[carburant["prix"] == carburant["prix"].min()]

# Alternative (more efficient in general)
carburant.query("prix == prix.min()")
