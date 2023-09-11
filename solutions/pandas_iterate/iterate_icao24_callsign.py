def iterate_icao24_callsign(data):
    for _, chunk in data.groupby(["icao24", "callsign"]):
        yield chunk

sum(1 for _ in iterate_icao24_callsign(df))
