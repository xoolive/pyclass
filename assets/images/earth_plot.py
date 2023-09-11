import matplotlib.pyplot as plt
from cartopy.crs import NearsidePerspective, Stereographic

fig, ax = plt.subplots(
    figsize=(15, 15),
    dpi=200,
    subplot_kw=dict(
        projection=NearsidePerspective(
            satellite_height=9000000.0,
            central_longitude=-3.53,
            central_latitude=50.72,
        )
    ),
)
ax.coastlines(resolution="50m", linewidth=2)
ax.gridlines(linewidth=1)
fig.set_tight_layout(True)
fig.savefig("nearside.png")


fig, ax = plt.subplots(
    figsize=(15, 15),
    dpi=200,
    subplot_kw=dict(projection=Stereographic(scale_factor=2)),
)
ax.coastlines(resolution="50m", linewidth=2)
ax.gridlines(linewidth=1)
fig.set_tight_layout(True)
fig.savefig("stereographic.png")
