carburant = carburant.assign(
    month=carburant.date.apply(lambda x: x.month)
)
