from pyproj import Geod

orly = (48.725278, 2.359444)
blagnac = (43.629075, 1.363819)

geod = Geod(ellps="WGS84")
_, _, distance = geod.inv(orly[1], orly[0], blagnac[1], blagnac[0])

print(f"{distance=}")

x1, y1 = sph2lcc(orly[1], orly[0])
x2, y2 = sph2lcc(blagnac[1], blagnac[0])

print(f"({x1=}, {y1=}), ({x2=}, {y2=})")
distance_lcc = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
print(f"{distance_lcc=}")
