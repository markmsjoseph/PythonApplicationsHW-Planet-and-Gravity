import turtle
import math
from solarSystem import *

class Planet:
    # create a sun
    def __init__(self, name, radius, mass, distance, color, velocityx, velocityy):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.color = color
        self.xVelocity = velocityx
        self.yVelocity = velocityy

        # sun will always be at the center
        self.x = distance
        self.y = 0

        # used for animation
        self.planetTurtle = turtle.Turtle() # create a turtle object
        self.planetTurtle.color(self.color)# set the color of the thing being drawn
        self.planetTurtle.hideturtle()# hide the pen head
        self.planetTurtle.screen.tracer(0)# turn off animation



        # go to area then draw the planet, all planets will be on the same y axis but different x axis coordinates 
        self.planetTurtle.up()
        self.planetTurtle.goto(self.x,self.y)
        self.planetTurtle.down()
        self.planetTurtle.begin_fill()# Call just before drawing a shape to be filled
        self.planetTurtle.circle(self.radius)
        self.planetTurtle.end_fill()

    # get the x position of the sun
    def getXPos(self):
        return self.x

    # get the y position
    def getYPos(self):
        return self.y

    def getXvel(self):
        return self.xVelocity

    def getYvel(self):
        return self.yVelocity

    def setXvel(self, newVel):
        self.xVelocity = newVel

    def setYvel(self, newVel):
        self.yVelocity = newVel

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.planetTurtle.goto(newx,newy)




    # override string method so that we can print any object of class Planet and not get the memory address
    def __str__(self):
        return "Planet name is " + self.name + " and its size is " + str(self.radius)