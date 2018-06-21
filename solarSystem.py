import turtle
import math


class SolarSystem:
    # create a sun
    def __init__(self, name, width, height):
        self.name = name
        self.theSun = None
        self.planets = []

        self.solarSystemTurtle = turtle.Turtle()
        self.solarSystemTurtle.screen.bgcolor("black")
        self.solarSystemTurtle.hideturtle()
        self.solarSystemTurtle.screen.setworldcoordinates(-width/2.0, -height/2.0,width/2.0, height/2.0)


    # add planets to the planet array
    def addPlanet(self, newPlanet):
        self.planets.append(newPlanet)

    # add a sun
    def addSun(self, newSun):
        self.theSun = newSun

    def printPlanets(self):
        for planet in self.planets:
            print(planet.name)

    def movePlanets(self):
        gravitationalConstant = .1
        timeStep = .001
        for p in self.planets:
            #move the planet to a new position
            p.moveTo(p.getXPos() + timeStep * p.getXvel(),  p.getYPos() + timeStep * p.getYvel())
        # recompute the distance from the planet to the sun
        xdistanceFromSun = self.theSun.getXPos() - p.getXPos()
        ydistanceFromSun = self.theSun.getYPos() - p.getYPos()
        distanceFromPlanetToSun = math.sqrt(xdistanceFromSun**2 + ydistanceFromSun**2)

        #compute acceleration
        xAcceleration = gravitationalConstant * self.theSun.getMass() * xdistanceFromSun/distanceFromPlanetToSun ** 3
        YAcceleration = gravitationalConstant * self.theSun.getMass() * ydistanceFromSun/distanceFromPlanetToSun ** 3

        p.setXvel(p.getXvel() + timeStep * xAcceleration)
        p.setYvel(p.getYvel() + timeStep * YAcceleration)


    def freezeScreen(self):
        self.solarSystemTurtle.screen.exitonclick()

