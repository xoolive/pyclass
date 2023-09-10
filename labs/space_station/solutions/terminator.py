def shade(dec, merc, max_=85):
    """Yields the terminator polygon."""
    yield prj.sph2merc(-180, -np.sign(dec) * max_)
    yield from zip(*merc)
    yield prj.sph2merc(180, -np.sign(dec) * max_)
    yield prj.sph2merc(-180, -np.sign(dec) * max_)


def terminator(ax, now, projection=prj.sph2merc):
    """Adds the terminator to current plot (Mercator)."""
    sun = planets["sun"]
    lat, lon, _ = geo.cartesian_to_geodesic(
        *earth.at(ts.utc(now)).observe(sun).position.m
    )
    _, dec, _ = earth.at(ts.utc(now)).observe(sun).radec()

    # Greenwich hour angle
    #   => angle between the Greenwich meridian and the meridian containing the subsolar point
    tau = 15 * ts.utc(now).gmst - lon
    lons = np.linspace(-180, 180)

    # Solar terminator
    lats = np.degrees(np.arctan(-np.cos(np.radians(lons + tau)) / np.tan(dec.radians)))

    def plus(altitude):
        return np.degrees(
            np.arcsin(
                np.sin(np.radians(altitude))
                / np.sqrt(
                    np.sin(dec.radians) ** 2
                    + (np.cos(dec.radians) * np.cos(np.radians(lons + tau))) ** 2
                )
            )
        )

    lats6 = lats + plus(6.)
    lats12 = lats + plus(12.)
    lats18 = lats + plus(18.)

    p = Polygon(list(shade(dec.radians, projection(lons, lats))))
    ax.add_patch(PolygonPatch(p, fc="#cccccc", ec="#cccccc", alpha=0.25, zorder=1))

    # TODO debug this part

    p = Polygon(list(shade(dec.radians, projection(lons, lats6))))
    # ax.add_patch(PolygonPatch(p, fc='#cccccc', ec='#cccccc', alpha=0.25, zorder=1))

    p = Polygon(list(shade(dec.radians, projection(lons, lats12))))
    # ax.add_patch(PolygonPatch(p, fc='#cccccc', ec='#cccccc', alpha=0.25, zorder=1))

    p = Polygon(list(shade(dec.radians, projection(lons, lats18))))
    # ax.add_patch(PolygonPatch(p, fc='#cccccc', ec='#cccccc', alpha=0.25, zorder=1))


fig = plt.figure(figsize=(20, 10))
ax = fig.gca()
now = datetime.datetime.now(utc)

for p in mercator:
    ax.add_patch(PolygonPatch(p, fc="#6699cc", ec="#6699cc", alpha=0.5, zorder=2))

trajectory(ax, now, iss)
terminator(ax, now)

# Finitions
ax.axis("scaled")
ax.set_xticks([])
ax.set_yticks([])
ax.set_ylim((-2, 3))
ax.set_frame_on(False)
