import turtle

class Sun:
    # create a sun
    def __init__(self, name, radius, mass, temperature):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.temperature = temperature

        # sun will always be at the center
        self.x = 0
        self.y = 0

        self.sunTurtle = turtle.Turtle()
        self.sunTurtle.hideturtle()# hide the pen head
        self.sunTurtle.screen.tracer(0)# turn off animation
        # used for animation

        self.sunTurtle.color("yellow")
        self.sunTurtle.begin_fill()# Call just before drawing a shape to be filled
        self.sunTurtle.circle(self.radius)
        self.sunTurtle.end_fill()

    # override string method so that we can print any object of class Sun and not get the memory address
    def __str__(self):
        return "We only have one sun named " + self.name

    # get the x position of the sun
    def getXPos(self):
        return self.x

    # get the y position
    def getYPos(self):
        return self.y

    def getMass(self):
        return self.mass