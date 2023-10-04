import fiona
import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import MultiPolygon, Polygon, shape
from shapely.plotting import patch_from_polygon

# parameters for Lambert93 projection
[lon0, lat0, lat1, lat2] = [np.radians(x) for x in [3, 46.5, 44, 49]]
x0, y0 = 700000, 6600000
r = 6371000


# Lambert conformal conic projection (from spherical coordinates)
def sph2lcc(lon, lat):
    lon, lat = np.radians(lon), np.radians(lat)
    n = np.sin(lat1)
    if lat1 != lat2:
        n = np.log(np.cos(lat1) / np.cos(lat2))
        n /= np.log(np.tan(np.pi / 4 + lat2 / 2) / np.tan(np.pi / 4 + lat1 / 2))
    F = r * np.cos(lat1) * np.exp(n * np.log(np.tan(np.pi / 4 + lat1 / 2))) / n
    rho = F / np.exp(n * np.log(np.tan(np.pi / 4 + lat / 2)))
    rho0 = F / np.exp(n * np.log(np.tan(np.pi / 4 + lat0 / 2)))
    x = x0 + rho * np.sin(n * (lon - lon0))
    y = y0 + rho0 - rho * np.cos(n * (lon - lon0))
    return (x, y)


def europe_map(projection, shapefile_path):
    items = [p for p in fiona.open(shapefile_path)]
    polygons = []

    for i in items:
        if i["properties"]["CNTR_ID"] in [
            # fmt: off
            "FR",  # France
            "DE", "IT", "ES",  # Germany, Italy, Spain
            "PT", "UK", "BE",  # Portugal, United Kingdom, Belgium
            "CH", "LU", "AD",  # Switzerland, Luxembourg, Andorra
            "NL", "AT", "LI",  # Netherlands, Austria, Liechtenstein
        ]:
            # fmt: on
            s = shape(i["geometry"])
            if s.geom_type == "Polygon":
                s = MultiPolygon([s])
            for idx, p in enumerate(s):
                lon = np.array([lon for (lon, _) in list(p.exterior.coords)])
                lat = np.array([lat for (_, lat) in list(p.exterior.coords)])
                x, y = projection(lon, lat)
                if i["properties"]["CNTR_ID"] == "FR":
                    polygons.append(
                        (
                            Polygon([a for a in zip(x, y)]),
                            {"fc": "#6699cc", "ec": "#6699cc"},
                        )
                    )
                else:
                    polygons.append(
                        (
                            Polygon([a for a in zip(x, y)]),
                            {"fc": "#cccccc", "ec": "#aaaaaa"},
                        )
                    )

    return polygons


def france_map(projection, shapefile_path):
    items = [p for p in fiona.open(shapefile_path)]
    polygons = []

    for i in items:
        if i["properties"]["CNTR_ID"] == "FR":
            s = shape(i["geometry"])
            if s.geom_type == "Polygon":
                s = MultiPolygon([s])
            for idx, p in enumerate(s):
                lon = np.array([lon for (lon, _) in list(p.exterior.coords)])
                lat = np.array([lat for (_, lat) in list(p.exterior.coords)])
                x, y = projection(lon, lat)
                polygons.append(
                    (
                        Polygon([a for a in zip(x, y)]),
                        {"fc": "#6699cc", "ec": "#6699cc"},
                    )
                )

    return polygons


def graticule(ax, longitude, latitude, projection, step=5):
    for lon in np.arange(longitude[0], longitude[1], step):
        lat_grat = np.arange(latitude[0], latitude[1])
        lon_grat = np.repeat(lon, len(lat_grat))
        x, y = projection(lon_grat, lat_grat)
        ax.add_line(plt.Line2D(x, y, color="#cccccc", alpha=0.5))

    for lat in np.arange(latitude[0], latitude[1], step):
        lon_grat = np.arange(longitude[0], longitude[1])
        lat_grat = np.repeat(lat, len(lon_grat))
        x, y = projection(lon_grat, lat_grat)
        ax.add_line(plt.Line2D(x, y, color="#cccccc", alpha=0.5))


fig, ax = plt.subplots(figsize=(7, 7))

for p in europe_map(sph2lcc, shapefile_path=shapefile_path):
    ax.add_patch(patch_from_polygon(p[0], alpha=0.5, zorder=2, **p[1]))

# Graticule
graticule(ax, (-10, 15), (30, 60), sph2lcc)

# Finitions
ax.set_xlim((100000, 1300000))
ax.set_ylim((6000000, 7200000))
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
