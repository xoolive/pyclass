import requests

c = requests.get("http://celestrak.com/NORAD/elements/stations.txt")
s = c.content.splitlines()
assert s[0].decode().strip() == "ISS (ZARYA)"
iss = EarthSatellite(s[1].decode(), s[2].decode())

