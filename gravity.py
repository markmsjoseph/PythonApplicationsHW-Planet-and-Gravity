from solarSystem import *
from sun import *
from planet import *

# create a solar system that will hold planets and sun
solarSystem = SolarSystem("milkyWay", 200, 200)
earth = Planet("earth",5,1000,50,"green",0,10)# name, radius, mass, distance, color, velocityx, velocityy):
mercury = Planet("mercury",2,500,25,"red",0,6)#name, radius, mass, distance, color
sun = Sun("Sun", 9, 10, 50)# name, radius, mass, temperature

solarSystem.addSun(sun)
solarSystem.addPlanet(earth)
solarSystem.addPlanet(mercury)

def animate():
    #clear the planets in order to animate
    for i in range(len(solarSystem.planets)):
        solarSystem.planets[i].planetTurtle.clear()

    # earth = Planet("earth",5,1000,50,"green",0,10)# name, radius, mass, distance, color, velocityx, velocityy):
    # mercury = Planet("mercury",2,500,25,"red",0,6)#name, radius, mass, distance, color
    # solarSystem.addPlanet(earth)
    # solarSystem.addPlanet(mercury)
    solarSystem.movePlanets()
    solarSystem.solarSystemTurtle.screen.ontimer(animate, 50)
    solarSystem.solarSystemTurtle.screen.update()# to remind Python to actually refresh the window with the new drawing

animate()
solarSystem.freezeScreen()
