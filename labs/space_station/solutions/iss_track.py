shapefile_path = "../data/CNTR_2014_03M_SH/Data/CNTR_RG_03M_2014.shp"

import fiona
import numpy as np

from descartes import PolygonPatch
from shapely.geometry import MultiPolygon, Polygon, shape

import geotools.projection as prj


def world_map(projection, shapefile_path=shapefile_path):

    items = [p for p in fiona.open(shapefile_path)]
    shapes = [shape(i["geometry"]) for i in items if i["properties"]["CNTR_ID"] != "AQ"]

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


mercator = world_map(prj.sph2merc)


def trajectory(ax, now, iss):
    """Plots the trajectory of the ISS on ax."""
    # Trajectory
    stack = []
    for k in range(60):
        t = ts.utc(now + k * datetime.timedelta(minutes=2))
        lat, lon, _ = geo.cartesian_to_geodesic(*iss.at(t).position.m)
        stack.append(prj.sph2merc(lon - 15 * t.gmst, lat))

    merc = np.array(stack)

    a = np.angle(np.exp(1j * merc[:, 0]))
    wh = np.where(np.abs(a[1:] - a[:-1]) > np.pi)[0]

    def leftmost(wh):
        yield -1
        yield from wh

    def rightmost(wh):
        yield from wh
        yield -1

    for p, q in zip(leftmost(wh), rightmost(wh)):
        ax.plot(a[p + 1 : q], merc[:, 1][p + 1 : q], "r-")

    ax.plot(a[0], merc[:, 1][0], "ro")


fig = plt.figure(figsize=(20, 10))
ax = fig.gca()
now = datetime.datetime.now(utc)

# Countries
for p in mercator:
    ax.add_patch(PolygonPatch(p, fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2))

trajectory(ax, now, iss)

# Finitions
ax.axis("scaled")
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim((-2, 3))
ax.set_frame_on(False)
