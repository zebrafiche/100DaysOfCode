# 182 Day 20 Goals_ what we will make by the end of the day

# We will use OOP and turtle to build the famous snake game
# Breakdown of the goals -
# Create a snake body (three squares)
# Move the snake
# Control the snake using keyboard
# Detect collision with food
# Keeping score
# Detect collision with the wall
# Detect collision with the tail


# 183 Screen Setup and Creating a Snake Body
# Set up the screen just like in the turtle race example and create a snake body

from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)

# Change screen's background color
screen.bgcolor('black')
# Change screen's title
screen.title("Rafi's snake game")


# screen.exitonclick()

# Now let's tackle the objectives one by one
# Create a snake body
# We are going to create three square shaped turtles that are going to be lined up next to each other
# Challenge -
# a. create three turtles
turtle1 = Turtle(shape='square')
turtle1.color('white')
turtle2 = Turtle(shape='square')
turtle2.color('white')
turtle3 = Turtle(shape='square')
turtle3.color('white')
turtles = [turtle1, turtle2, turtle3]
# b. by default a turtle is positioned at (0,0), you want the turtles to be positioned so that they are lined together
x = 0
y = 0
for i in turtles:
    i.penup()
    i.setposition(x, y)
    x -= 20

# screen.exitonclick()


# 184 Animating the Snake Segments on Screen
# Move the snake
# move the snake automatically without doing anything
game_on = True
while game_on:
    for i in turtles:
        i.forward(20)

# how to make the movement smooth?
# a bit complex, bear with me
# we need to use the screen animation control methods, delaY(), tracer(), update()
# by default, turtle shows the user all the changes that happen with the turtle
# now think how cartoons were made in the old days
# they used to draw multiple pictures of the same object undergoing small incremental changes
# and then they showed all the pictures one by one
# so basically the viewer only saw the pictures after the incremental changes happened, not the changes being made
# similarly by default, turtle shows the changes being made, rendering it stuttering

# so we need to first turn the animation off, then update the screen at regular intervals after every incremental change
# use tracer()
screen.tracer(0)
# and update after the necessarily changes have been made

import time
game_on = True
while game_on:
    for i in turtles:
        i.forward(20)
        screen.update()
        # to see it in slow motion, import time module (top)
        time.sleep(1)
        # this basically creates a one-second delay till the code continues on to the next line
        # (next iteration in the loop in this case)
# we can see that the blocks move one by one, now that it is in slow motion

# Now if we move the screen.update() to after all the blocks have shifted position
import time
game_on = True
while game_on:
    screen.update()
    for i in turtles:
        i.forward(20)
        time.sleep(1)

# Now if we move the time.sleep(1) after all the blocks have moved and reduce the time
import time
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in turtles:
        i.forward(20)

# We can see that the snake moves at a reasonably high speed


# Now how do we command the blocks to move forward?
# a. turn the head turtle
def move_right():
    turtle1.setheading(0)


def move_left():
    turtle1.setheading(180)


def move_up():
    turtle1.setheading(90)


def move_down():
    turtle1.setheading(270)


screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")

# b. the other turtles must follow the head turtle
# do it so that the last turtle moves to the second last position, the second last to the third last and so on
while game_on:
    destination = turtle1.position()
    screen.update()
    time.sleep(0.1)
    for i in range(len(turtles) - 1, 0, -1):
        x = turtles[i - 1].xcor()
        y = turtles[i - 1].ycor()
        turtles[i].goto(x, y)
    turtles[0].forward(20)

# Now put it all together

from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Rafi's snake game")
screen.tracer(0)

turtle1 = Turtle(shape='square')
turtle1.color('white')
turtle2 = Turtle(shape='square')
turtle2.color('white')
turtle3 = Turtle(shape='square')
turtle3.color('white')
turtles = [turtle1, turtle2, turtle3]

x = 0
y = 0
for i in turtles:
    i.penup()
    i.setposition(x, y)
    x -= 20
screen.update()


def move_right():
    turtle1.setheading(0)


def move_left():
    turtle1.setheading(180)


def move_up():
    turtle1.setheading(90)


def move_down():
    turtle1.setheading(270)


screen.listen()

screen.onkey(move_right, "Right")
screen.onkey(move_left, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for i in range(len(turtles)-1, 0, -1):
        x = turtles[i - 1].xcor()
        y = turtles[i - 1].ycor()
        turtles[i].goto(x, y)
    turtles[0].forward(20)


screen.exitonclick()


# 185 Create a Snake Class & Move to OOP

# We should have three classes, a snake class, a food class and a scoreboard class
# We should be able to create a snake object by calling Snake() and move the snake by calling snake.move

# a. define the attributes of the snake
class Snake:
    # now remember what variables you created and what processes or functions you made
    def __init__(self):
        # basically in the __init__ section you define the variables
        self.turtles = []
        self.create_snake()
        # create a snake when the object is created, currently empty
# b. define the methods of the snake

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
        # creates the snake in full

    def move(self):
        for i in range(len(self.turtles) - 1, 0, -1):
            m = self.turtles[i - 1].xcor()
            n = self.turtles[i - 1].ycor()
            self.turtles[i].goto(m, n)
        self.turtles[0].forward(20)
        # moves the snake

# So now your snake_game should look like this -

from turtle import Turtle, Screen
import time
import snake

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Rafi's snake game")
screen.tracer(0)

snake = snake.Snake()

screen.update()

# dealing with the movement and follow part later

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


# 186 How to Control the Snake with a Keypress

# Already coded above, Angela is getting to it just now
# In the end, I should have the necessary methods created in the snake class so that -

# screen.onkey(snake.right, "Right")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")

# a. modify the functions for the snake class


    def right(self):
        # add another variable head = turtles[0] in the __init__ block
        self.head.setheading(0)


    def left(self):
        self.head.setheading(180)


    def up(self):
        self.head.setheading(90)


    def down(self):
        self.head.setheading(270)


# b. in the snake_game file, change code from screen.onkey(move_right, "Right") to screen.onkey(snake.right, "Right")

# Done

# Now there is one thing still left, the snake currently can move back on its head
# It should not be able to do that, for example it should not be able to move down when it is moving up
# We gotta change the directional methods above with an if block


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

# And that's it! Our goal for the first day was -

# Create a snake body (three squares)
# Move the snake
# Control the snake using keyboard

# We will complete the snake game the next day
# Good luck


# 187 Programming is not Memorising

