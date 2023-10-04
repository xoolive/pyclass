import matplotlib.pyplot as plt
import numpy as np
from shapely.plotting import patch_from_polygon


def sph2wkl3(lon, lat):
    lon, lat = np.radians(lon), np.radians(lat)
    phi = np.arccos(2 / np.pi)
    alpha = np.arccos(np.cos(lat) * np.cos(lon / 2))
    x = (
        lon * np.cos(phi)
        + 2 * np.cos(lat) * np.sin(lon / 2) / np.sinc(alpha / np.pi)
    ) / 2
    y = (lat + np.sin(lat) / np.sinc(alpha / np.pi)) / 2
    return x, y


fig, ax = plt.subplots(figsize=(20, 10))
for p in world_map(sph2wkl3, shapefile_path=shapefile_path):
    ax.add_patch(
        patch_from_polygon(p, fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2)
    )

graticule(ax, (-180, 181), (-90, 91), sph2wkl3, 10)

# Finitions
ax.axis("scaled")
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
