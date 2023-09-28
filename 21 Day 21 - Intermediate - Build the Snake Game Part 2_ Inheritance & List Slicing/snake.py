from turtle import Turtle, Screen
screen = Screen()

paces = 20


class Snake:
    # now remember what variables you created and what processes or functions you made
    def __init__(self):
        # basically in the __init__ section you define the variables
        self.turtles = []
        self.create_snake()
        # create a snake when the object is created, currently empty
        self.head = self.turtles[0]
        # this is explained in the def(right) function
        # mind the positioning of this self.head variable. if it was placed before self.create_snake() that'd be wrong
        # bcz there'd be no first item in the list to begin with, since the list would be empty

    def create_snake(self):
        turtle1 = Turtle(shape='square')
        turtle1.color('white')
        self.turtles.append(turtle1)
        turtle2 = Turtle(shape='square')
        turtle2.color('white')
        self.turtles.append(turtle2)
        turtle3 = Turtle(shape='square')
        turtle3.color('white')
        self.turtles.append(turtle3)
        a = 0
        b = 0
        for i in self.turtles:
            i.penup()
            i.setposition(a, b)
            a -= 20
        # creates the snake in full

    def increase_length(self):
        new_turtle = Turtle(shape='square')
        # new_turtle.hideturtle()
        # hideturtle() conceals the snake as it lengthens too
        new_turtle.color('white')
        new_turtle.penup()
        new_turtle.goto(self.turtles[-1].position())
        # so the turtle generation is shown at the tail end of the existing snake
        self.turtles.append(new_turtle)


    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            x = self.turtles[i - 1].xcor()
            y = self.turtles[i - 1].ycor()
            self.turtles[i].goto(x, y)
        self.head.forward(paces)
        # moves the snake

    def right(self):
        # add another variable head = turtles[0] in the __init__ block
        # it cannot go right if it is moving leftwards, other times ok
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

# WE COULD USE VARIABLES FOR THE DEGREES, SO THAT UP IS 90 AND SO ON
# IN THAT CASE WE WOULD HAVE TO DECLARE SOME VARIABLES AT THE TOP, OUTSIDE THE CLASS
# Why outside?
# Because if it were an attribute that would mean other users could edit it
# UP = 90 (set by me)
# UP = 1000 (set by someone else)
# I do not want that, therefore declare it outside the class
