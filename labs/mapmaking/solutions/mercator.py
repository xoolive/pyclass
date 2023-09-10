import fiona
import matplotlib.pyplot as plt
import numpy as np
from descartes import PolygonPatch
from shapely.geometry import MultiPolygon, Polygon, shape


def sph2merc(lon: float, lat: float) -> tuple[float, float]:
    # Mercator projection (from spherical coordinates)
    lon, lat = np.radians(lon), np.radians(lat)
    return (lon, np.log(np.tan(lat) + 1.0 / np.cos(lat)))


def world_map(projection, shapefile_path):

    items = [p for p in fiona.open(shapefile_path)]
    shapes = [
        shape(i["geometry"])
        for i in items
        if i["properties"]["CNTR_ID"] != "AQ"
    ]

    polygons = []
    for s in shapes:
        if s.geom_type == "Polygon":
            s = MultiPolygon([s])
        for idx, p in enumerate(s):
            lon = np.array([lon for (lon, _) in list(p.exterior.coords)])
            lat = np.array([lat for (_, lat) in list(p.exterior.coords)])
            x, y = projection(lon, lat)
            polygons.append(Polygon([a for a in zip(x, y)]))

    return polygons


fig, ax = plt.subplots(figsize=(20, 10))

for p in world_map(sph2merc, shapefile_path=shapefile_path):
    ax.add_patch(
        PolygonPatch(p, fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2)
    )

# Finitions
ax.axis("scaled")
ax.set_frame_on(False)
