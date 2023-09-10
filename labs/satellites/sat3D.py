from __future__ import division, print_function

import math

from vpython import canvas, color, mag2, norm, rate, sphere, vector

# Right button drag or Ctrl-drag to rotate "camera" to view scene.
# To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
#  On a two-button mouse, middle is left + right.

scene = canvas(title="MyFirstSatellite")

G = 6.7e-11
radiusEarth = 6.4e6
earth = sphere(
    pos=vector(0, 0, 0),
    radius=radiusEarth,
    color=color.blue,
    make_trail=True,
    trail_type="points",
    interval=10,
    retain=200,
)
earth.mass = 5.98e24

mu = earth.mass * G

altMEO = 20e6 + radiusEarth

satMEO = sphere(
    pos=vector(0, altMEO, 0),
    radius=1e6,
    color=color.yellow,
    make_trail=True,
    trail_type="points",
    interval=10,
    retain=200,
)
satMEO.mass = 1.0
satMEO.initSpeed = math.sqrt(G * earth.mass / altMEO)
satMEO.speed = vector(-satMEO.initSpeed, 0, 0)

altGEO = 36e6 + radiusEarth
satGEO = sphere(
    pos=vector(0, altGEO, 0),
    radius=1e6,
    color=color.green,
    make_trail=True,
    trail_type="points",
    interval=10,
    retain=200,
)
satGEO.mass = 1.0
satGEO.initSpeed = math.sqrt(G * earth.mass / altGEO)
satGEO.speed = vector(-satGEO.initSpeed, 0, 0)


altLEO = 163e3 + radiusEarth
satLEO = sphere(
    pos=vector(0, altLEO, 0),
    radius=1e6,
    color=color.orange,
    make_trail=True,
    trail_type="points",
    interval=10,
    retain=200,
)
satLEO.mass = 1.0
satLEO.initSpeed = math.sqrt(G * earth.mass / altLEO)
satLEO.speed = vector(-satLEO.initSpeed, 0, 0)

print("init speed " + str(satMEO.initSpeed) + " m/s")

# dt = 1e5
dt = 10

i = 0
imax = 1000
while i < imax:
    rate(100)
    satMEO.r = earth.pos - satMEO.pos

    # <satMEO.F> = m.g.<r>/||<r>||  = m.g.<norm(r)>
    # g = G.M/r^2
    # mu = G.M
    satMEO.F = satMEO.mass * mu / (mag2(satMEO.r)) * norm(satMEO.r)
    satMEO.speed = satMEO.speed + satMEO.F / satMEO.mass * dt
    satMEO.pos = satMEO.pos + satMEO.speed * dt

    satGEO.r = earth.pos - satGEO.pos
    satGEO.F = satGEO.mass * mu / (mag2(satGEO.r)) * norm(satGEO.r)
    satGEO.speed = satGEO.speed + satGEO.F / satGEO.mass * dt
    satGEO.pos = satGEO.pos + satGEO.speed * dt

    satLEO.r = earth.pos - satLEO.pos
    satLEO.F = satLEO.mass * mu / (mag2(satLEO.r)) * norm(satLEO.r)
    satLEO.speed = satLEO.speed + satLEO.F / satLEO.mass * dt
    satLEO.pos = satLEO.pos + satLEO.speed * dt

    i += 1
