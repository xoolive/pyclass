bigger_chunk = df.query('icao24 == "3924a4"')
bigger_chunk.agg(dict(timestamp=["min", "max"]))
