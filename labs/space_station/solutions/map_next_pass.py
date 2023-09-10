def europe_ext_map(projection, shapefile_path=shapefile_path):

    items = [p for p in fiona.open(shapefile_path)]
    polygons = []

    for i in items:
        if i["properties"]["CNTR_ID"] in [
            "FR",  # France
            "DE", "IT", "ES",  # Germany, Italy, Spain
            "PT", "UK", "BE",  # Portugal, United Kingdom, Belgium
            "CH", "LU", "AD",  # Switzerland, Luxembourg, Andorra
            "NL", "AT", "LI",  # Netherlands, Austria, Liechtenstein
            "CZ", "PL", "IE",  # Czech Republic, Poland, Ireland
            "SK", "SI", "DK",  # Slovakia, Slovenia, Denmark
            "HR", "SE", "HU",  # Croatia, Sweden, Hungary
            "BA",  # Bosnia
        ]:
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


# Compute a new track (and keep additional parameters)
VisiblePoint = namedtuple(
    "VisiblePoint", ["lat", "lon", "iss_alt", "iss_az", "sun_alt", "time", "localtime"]
)


def visible_track(start, position):
    track = []
    sun = planets["sun"]
    for k in range(60):  # 10 minutes à 10 secondes
        t = ts.utc(start + k * datetime.timedelta(seconds=10))
        iss_alt, iss_az, _ = position.at(t).observe(earth + iss).apparent().altaz()
        sun_alt, _, _ = position.at(t).observe(sun).apparent().altaz()
        lat, lon, _ = geo.cartesian_to_geodesic(*iss.at(t).position.m)

        if iss_alt.degrees > 10:
            point = VisiblePoint(
                lat,
                lon - 15 * t.gmst,
                iss_alt,
                iss_az,
                sun_alt,
                t,
                t.astimezone(pytz.timezone("Europe/Paris")).strftime(
                    "%d/%m/%Y %H:%M:%S"
                ),
            )
            track.append(point)
    return track


# Choose the most visible pass
choice = max(visible, key=lambda x: x[1].degrees)
# Compute the track of the pass over
track = visible_track(choice[0] - datetime.timedelta(minutes=3), toulouse)

fig = plt.figure()
ax = fig.gca()

for p in europe_ext_map(prj.sph2lcc):
    ax.add_patch(PolygonPatch(p[0], alpha=0.5, zorder=2, **p[1]))

graticule(ax, (-10, 15), (30, 60), prj.sph2lcc)
terminator(ax, now, prj.sph2lcc)

# Where am I ?
ax.plot(
    *prj.sph2lcc(
        toulouse.positives[2].longitude.degrees,
        toulouse.positives[2].latitude.degrees
    ),
    "o",
    color="#f13a31",
    markeredgecolor="#f13a31"
)
ax.annotate(
    "  Toulouse",
    prj.sph2lcc(
        toulouse.positives[2].longitude.degrees,
        toulouse.positives[2].latitude.degrees
    ),
)

# ISS
coords = np.array([(point.lon, point.lat) for point in track])
coords[:, 0] = np.degrees(np.angle(np.exp(1j * np.radians(coords[:, 0]))))
ax.plot(
    *prj.sph2lcc(coords[:, 0], coords[:, 1]),
    "o-",
    color="#ff5d55",
    markeredgecolor="#ff5d55"
)

# Finitions
ax.set_xlim((-320000, 1800000))
ax.set_ylim((5600000, 7700000))
ax.set_xticks([])
ax.set_yticks([])
fig.set_size_inches(7, 7)
ax.set_frame_on(False)


def str_hour(t):
    return t.astimezone(pytz.timezone("Europe/Paris")).strftime("%H:%M:%S")


def str_day(t):
    return t.astimezone(pytz.timezone("Europe/Paris")).strftime("%d/%m/%Y")


print("Passage de l'ISS le {}".format(str_day(track[0].time)))
print(
    "Altitude maximum {:.2f}° à {}".format(
        *max((t.iss_alt.degrees, str_hour(t.time)) for t in track)
    )
)
print(
    "Azimuth entre {:.2f}° ({}) et {:.2f}° ({})".format(
        track[0].iss_az.degrees,
        str_hour(track[0].time),
        track[-1].iss_az.degrees,
        str_hour(track[-1].time),
    )
)
