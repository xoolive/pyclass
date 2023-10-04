fig, ax = plt.subplots(figsize=(20, 10))
for p in world_map(sph2wkl3, shapefile_path=shapefile_path):
    ax.add_patch(
        patch_from_polygon(p, fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2)
    )

graticule(ax, (-180, 181), (-90, 91), sph2wkl3, 10)

# Great circle
line = geod.npts(cdg[1], cdg[0], tokyo[1], tokyo[0], 200)
ax.plot(*sph2wkl3(*np.array(line).T), color="#f58518")

# Finitions
ax.axis("scaled")
ax.set_xticks([])
ax.set_yticks([])
ax.set_frame_on(False)
