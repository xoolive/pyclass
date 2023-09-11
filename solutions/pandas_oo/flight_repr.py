class FlightCollection:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"FlightCollection with {self.data.shape[0]} records"
