def passing_over(
    now,
    location,
    condition,
    horizon=datetime.timedelta(days=7),
    timestep=datetime.timedelta(minutes=2),
):

    res = []
    prec_time = None
    msg = "{} : iss {:0.3f} deg ; sun {:0.3f} deg"
    sun = planets["sun"]

    for k in range(int(horizon / timestep)):  # 1 day = 720 minutes
        t = ts.utc(now + k * timestep)
        lat, lon, _ = geo.cartesian_to_geodesic(*iss.at(t).position.m)
        iss_alt, _, _ = location.at(t).observe(earth + iss).apparent().altaz()
        sun_alt, _, _ = location.at(t).observe(sun).apparent().altaz()
        if condition(iss_alt, sun_alt):
            time = t.astimezone(pytz.timezone("Europe/Paris"))
            if prec_time is None or (time - prec_time).seconds > 3600:
                res.append((time, iss_alt, sun_alt))
                print(
                    msg.format(
                        time.strftime("%Y-%m-%d %H:%M:%S"),
                        iss_alt.degrees,
                        sun_alt.degrees,
                    )
                )
                prec_time = time
    return res


now = datetime.datetime.now(utc)
toulouse = earth + Topos(43.629075, 1.363819)


def condition(iss_alt, sun_alt):
    return iss_alt.degrees > 10 and -18 < sun_alt.degrees < -6


visible = passing_over(now, toulouse, condition, horizon=datetime.timedelta(days=3))
