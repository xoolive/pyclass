from cartopy.crs import EuroPP, PlateCarree

fig, ax = plt.subplots(figsize=(10, 7), subplot_kw=dict(projection=EuroPP()))
ax.coastlines("50m")

for flight in collection[pd.Timestamp("2019-07-18")]:
    flight.plot(
        ax,
        color="crimson" if flight.callsign.startswith("PXR") else "steelblue",
        alpha=0.5,
    )

ax.set_extent((-1, 5, 42, 45))
ax.set_yticks([])

fig, ax = plt.subplots(figsize=(10, 7))
for flight in collection[pd.Timestamp("2019-07-18")]:
    flight.data.plot(ax=ax, x="timestamp", y="altitude", label=flight.callsign)

# All flights fly at a different altitude, ensuring that they don't collide.
# Note that the PXR missions are aircraft taking pictures of the Tour while the
# ASR missions fly at a higher altitude to catch their signals and broadcast it
# to static ground stations for live TV programs.

dict(
    (f.callsign, f.max("altitude"))
    for f in collection[pd.Timestamp("2019-07-18")]
)
