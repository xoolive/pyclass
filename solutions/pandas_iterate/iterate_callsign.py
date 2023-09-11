def iterate_callsign(data):
    for _, chunk in data.groupby("callsign"):
        yield chunk
