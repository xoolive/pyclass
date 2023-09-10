import fiona
from cartes.crs import Lambert93
from shapely.geometry import shape

items = [p for p in fiona.open(shapefile_path)]

fig, ax = plt.subplots(
    figsize=(10, 10), subplot_kw=dict(projection=Lambert93())
)

ax.gridlines(color="#cccccc", alpha=0.5)

ax.add_geometries(
    list(
        shape(i["geometry"])
        for i in items
        if i["properties"]["CNTR_ID"] == "FR"
    ),
    crs=crs.PlateCarree(),
    facecolor="#6699cc",
    alpha=0.5,
)
# fmt: off
neighbours = ["DE", "IT", "ES", "PT", "UK", "BE", "CH", "LU", "AD", "NL", "AT", "LI"]
# fmt: on

ax.add_geometries(
    list(
        shape(i["geometry"])
        for i in items
        if i["properties"]["CNTR_ID"] in neighbours
    ),
    crs=crs.PlateCarree(),
    facecolor="#cccccc",
    edgecolor="#aaaaaa",
    alpha=0.5,
)

ax.set_frame_on(False)
