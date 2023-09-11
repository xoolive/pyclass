colormap = plt.cm.YlGnBu  # choose your favourite one!

fig = plt.figure(figsize=(15, 10))
ax = plt.axes(projection=lambert93)

X = sp98_dept_filled.mean()
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
fig.colorbar(mappable, label="Prix moyen du SP98")
