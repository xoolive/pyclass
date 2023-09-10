from __future__ import division, print_function
from vpython import *

# Right button drag or Ctrl-drag to rotate "camera" to view scene.
# To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
#  On a two-button mouse, middle is left + right.

#http://127.0.0.1:8968/tree/SVN/CAS/interactionadaptative/coursISAE/algoPython

from __future__ import division, print_function
from vpython import *

# Right button drag or Ctrl-drag to rotate "camera" to view scene.
# To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
#  On a two-button mouse, middle is left + right.

scene=canvas(title="MyFirstSatelliteObject")
global G
G = 6.7e-11


class Planet(sphere):
    def __init__(self,mass,position,radius,color):
        global G
        super().__init__(pos=position, radius=radius, color=color, 
                make_trail=True, trail_type='points', interval=10, retain=200)
        self.mass=mass
        self.radius = radius
        self.mu = self.mass * G
        self.pos = position
        
earth = Planet(5.98e24,vector(0,0,0),6.4e6,color.blue)
moon = Planet(0.07346e24,vector(0,378e5,0),1.736e6,color.white)#pos modif for beauty




class Satellite(Planet):
    def __init__(self,refPlanet,position,color,speed):
        massSat = 1.0
        radiusSat = 1e6
        self.refPlanet = refPlanet
        super().__init__(massSat,position,radiusSat,color)
        self.speed = speed
        
        self.wingShift = 1e6
        self.myboxRight = box(pos=vector(position.x+self.wingShift,position.y,position.z), length=1e7, height=1e4, width=5e6)
        self.myboxLeft = box(pos=vector(position.x-self.wingShift,position.y,position.z), length=1e7, height=1e4, width=5e6)
        
        self.r = self.refPlanet.pos - self.pos  
        self.withCoverage = False

    def updatePosition(self,dt):
        self.r = self.refPlanet.pos - self.pos    
        F = self.mass * self.refPlanet.mu/(mag2(self.r)) * norm(self.r)
        self.speed = self.speed + F / self.mass * dt
        self.pos = self.pos + self.speed*dt  
        self.myboxRight.pos = vector(self.pos.x+self.wingShift,self.pos.y,self.pos.z)
        self.myboxLeft.pos = vector(self.pos.x-self.wingShift,self.pos.y,self.pos.z)
        
        if self.withCoverage:
            self.coverage.axis = -self.r
            self.coverage.pos = vector(self.pos.x,self.pos.y,self.pos.z)+self.r
        
        
    def addCoverage(self,deg):
        self.withCoverage = True
        
        #self.refPlanet.radius
        radius =  math.tan(deg*math.pi/180) * mag(self.r)
        axis = -self.r
        self.coverage = cone(pos=vector(self.pos.x,self.pos.y,self.pos.z)+self.r, axis=axis,radius=radius)

    def changeOrbitSamePlane(self,alpha):
        x = mag(self.pos)*math.cos(alpha)
        y = mag(self.pos)*math.sin(alpha)
        vx = mag(self.speed)*math.sin(alpha)
        vy = -mag(self.speed)*math.cos(alpha)
        self.pos = vector(x,y,0)
        self.speed = vector(vx,vy,0)
        
mySats = []        
altMEO = 20e6+earth.radius
initSpeedMEO = math.sqrt(G*earth.mass/altMEO)
initSpeedMEOVect = vector(initSpeedMEO,0,0)
satMEO = Satellite(earth,vector(0,altMEO,0),color.yellow,initSpeedMEOVect)
mySats.append(satMEO)
#code largement reductible

#satMEO.addCoverage(12)


#altGEO = 36e6+earth.radius
#initSpeedGEO = math.sqrt(G*earth.mass/altGEO)
#initSpeedGEOVect = vector(-initSpeedGEO,0,0)
#satGEO = Satellite(earth,vector(0,-altGEO,0),color.yellow,-initSpeedGEOVect)
#satGEO.addCoverage(17)
#mySats.append(satGEO)
    
initSpeedMEOVect = vector(initSpeedMEO,0,0)
satMEO2 = Satellite(earth,vector(0,altMEO,0),color.yellow,initSpeedMEOVect)
satMEO2.changeOrbitSamePlane(math.radians(30))
mySats.append(satMEO2) 

initSpeedMEOVect = vector(initSpeedMEO,0,0)
satMEO3 = Satellite(earth,vector(0,altMEO,0),color.yellow,initSpeedMEOVect)
satMEO3.changeOrbitSamePlane(math.radians(60))
mySats.append(satMEO3) 

initSpeedMEOVect = vector(initSpeedMEO,0,0)
print(initSpeedMEOVect)
theta = math.radians(30)
initSpeedMEOVect = initSpeedMEOVect.rotate(theta,vector(0,1,0))
print(initSpeedMEOVect)
satMEO4 = Satellite(earth,vector(0,altMEO,0),color.yellow,initSpeedMEOVect)
mySats.append(satMEO4) 

dt = 10
i=0
imax=6000
while i<imax:
    rate(30)
    #satMEO4.updatePosition(dt)
    for s in mySats:
        s.updatePosition(dt)
        
    i+=1
