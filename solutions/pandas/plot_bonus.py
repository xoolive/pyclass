# Bonus: On affiche la même carte pour tous les types de carburant...

def plot_map(X, carburant="SP98"):

    fig = plt.figure(figsize=(15, 10))
    ax = plt.axes(projection=lambert93)

    # X = stats_dept.mean()
    norm = plt.Normalize(X.min(axis=0), X.max(axis=0))

    for dept, value in zip(X.index[:-1], X):
        if dept not in ["20", "974"]:  # On omet la Corse et la Réunion...
            ax.add_geometries(
                shapes[dept],
                ccrs.PlateCarree(),
                edgecolor="#aaaaaa",
                facecolor=colormap(norm(value)),
            )

    ax.coastlines("10m", color="#226666")

    ax.set_xlim((80000, 1150000))
    ax.set_ylim((6100000, 7150000))

    mappable = plt.cm.ScalarMappable(norm, colormap)
    mappable.set_array(X)
    fig.colorbar(mappable, label="Prix moyen du {}".format(carburant))


for dept, data in carburant.groupby("type"):

    X = (
        data.merge(stations, on="id")
        .groupby(["departement", "week"])["prix"]
        .mean()
        .unstack("departement")
        .mean()
    )

    plot_map(X, dept)
