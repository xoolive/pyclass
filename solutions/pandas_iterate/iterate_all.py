def iterate_all(data, threshold):
    for group in iterate_icao24_callsign(data):
        for elt in iterate_time(group, 20000):
            yield elt

# This can be written in a more compact way with the `yield from` notation.

def iterate_all(data, threshold):
    for group in iterate_icao24_callsign(data):
        yield from iterate_time(group, 20000)
