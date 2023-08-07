# 175 Day 19 Goals_ what we will make by the end of the day

# We will be making etch a sketch and a turtle racing game


# 176 Python Higher Order Functions & Event Listeners

# To make the turtle respond to our keystrokes, we need the turtle to 'listen' to the keystrokes
# The code that allows us to do that are called event listeners

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# The screen object will control the window we are going to run our code on

screen.listen()


# This makes the screen start listening
# Once it starts listening, we have a bind/map a function that will be triggered when a particular key is pressed
# These functions are called event listeners

# In order to bind a keystroke (suppose shift) to an event (function) we have to use an event listener
# From the documentation -
# turtle.onkey(fun, key)
# fun – a function with no arguments or None
# key – a string: key (e.g. “a”) or key-symbol (e.g. “space”)


# First let's create our function
def move_forwards():
    tim.forward(10)


# Now pass the function and the key it will correspond to in the onkey method
screen.onkey(key="space", fun=move_forwards)
# Note - do not write move_forwards() when binding a function to a key, we don't want to trigger it now
# We want to trigger it only when space is pressed

screen.exitonclick()

# Run the code
# You can see that the turtle moves 10 paces only when you press space

# Now how does a function (screen.onkey is essentially a function, right?) work with another function?
# Imagine the calculator project
# You had various functions
# Add()
# Subtract()
# Multiply()
# Divide()
# # Let's say now you have another function called calculator...
# Calc(n1, n2, func)
# ...that takes two variables and a function

# So it would work like this -
calc(10, 5, add)

# These types of functions (calc) are called higher order functions
# These are functions that take other functions as inputs

# In other languages, you cannot do this at all, but you can do it in python

# A suggestion - for methods that you haven't created yourself, like this screen.onkey(), use keyword arguments
# Like do not positional arguments like this - screen.onkey("space", move_forwards)
# Specifically denote the key, i.e. use keyword arguments - screen.onkey(key="space", fun=move_forwards)


# 177 Challenge_ Make an Etch-A-Sketch App

# Make an etch a sketch game with the following key bindings -

# W = Forwards
# S = Backwards
# A = Counter - Clockwise
# D = Clockwise
# C = Clear Drawing

import turtle
# Create turtle object
sketcher = turtle.Turtle()
screen = turtle.Screen()
# Identify the methods used for the actions
#     Forwards
sketcher.forward(10)

#     Backwards
sketcher.back(10)

#     Counter - clockwise
sketcher.left(10)

#     Clockwise
sketcher.right(10)

#     Clear Drawing
# From the documentation -
# turtle.clear()
# Delete the turtle’s drawings from the screen.
# Do not move turtle. State and position of the turtle as well as drawings of other turtles are not affected.
sketcher.clear()

# Bring turtle at the home position
# turtle.home()
# Move turtle to the origin – coordinates (0,0) – and set its heading to its start-orientation
# (which depends on the mode) (we do not need mode for this right now)
sketcher.home()

# Define functions for the actions
def move_forwards():
    sketcher.forward(10)
def move_backwards():
    sketcher.back(10)
def move_left():
    sketcher.left(10)
def move_right():
    sketcher.right(10)
def clear():
    sketcher.clear()
    sketcher.home()

# Start listening

screen.listen()

# Use event listener

screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="D", fun=move_right)
screen.onkey(key="C", fun=clear)

# Now put it all together

import turtle
sketcher = turtle.Turtle()
screen = turtle.Screen()

def move_forwards():
    sketcher.forward(10)
def move_backwards():
    sketcher.back(10)
def move_left():
    sketcher.left(10)
def move_right():
    sketcher.right(10)
def clear():
    sketcher.clear()
    # after trying, we saw that the turtle draws its way back to home
    sketcher.penup()
    sketcher.home()
    sketcher.pendown()


screen.listen()

screen.onkey(key="W", fun=move_forwards)
screen.onkey(key="S", fun=move_backwards)
screen.onkey(key="A", fun=move_left)
screen.onkey(key="D", fun=move_right)
screen.onkey(key="C", fun=clear)

screen.exitonclick()


# 178 Object State and Instances

# Objective - we want to build a turtle race game
# So we would need multiple turtle objects, right?

import turtle
screen = turtle.Screen()
tim = turtle.Turtle()
tom = turtle.Turtle()

# tim and tom are actually independent of each other
# in programming, we would say that they are each a separate instance

# that means they can have different attributes and have different methods, in programming this is known as state
# In this case they have different states in terms of attributes

tim.color("red")
tom.color("green")
print(tim.color())
# ('black', 'black')
tim.forward(100)
screen.exitonclick()


# 179 Understanding the Turtle Coordinate System

Goals -
# A pop up asking which colored turtle they would like to bet on
# 7 turtles all lined up side by side at the edge of the screen
# Turtles randomly moving paces with each step
# First one to cross the edge is winner
# Winner compared to our bet, telling us if we won or lost

import turtle
screen = turtle.Screen()
# from the documentation -
# screen.setup (width=, height=, startx=0, starty=0)
# width – if an integer, a size in pixels, if a float, a fraction of the screen; default is 50% of screen
# height – if an integer, the height in pixels, if a float, a fraction of the screen; default is 75% of screen
# startx – if positive, starting position in pixels from the left edge of the screen, if negative from the right edge,
#          if None, center window horizontally
# starty – if positive, starting position in pixels from the top edge of the screen, if negative from the bottom edge,
#          if None, center window vertically


screen.setup(width=500, height=400)

# Now consider the first goal, we need to generate a pop up that asks the user for his/her preferred color
# From the documentation -
# turtle.textinput(title, prompt)
# screen.textinput("NIM", "Name of first player:")
# Pop up a dialog window for input of a string. Parameter title is the title of the dialog window,
# prompt is a text mostly describing what information to input. Return the string input.
# If the dialog is canceled, return None.

user_bet = screen.textinput("Place your bet", "Which turtle will win the race? Enter a color: ")
print(user_bet)
# red

# Set starting position for each turtle
# Now think forwards, we will have to work with multiple turtle objects, right?
# cannot use home() or setheading(), they will all move to the same point, don't want that
# basically the edge of the screen, so fixed x, variable y
# use the goto method
# turtle.goto(x, y=None)
# x – a number or a pair/vector of numbers
# y – a number or None

# Note, in the screen, by default, the turtle is positioned at (0,0)
# So if your screen is 500 by 400, it means, y axis runs from -200 to 200 and x axis from - 250 to 250

# timestamp - 05:30

# So move the turtle to a preferred starting point
tim = turtle.Turtle(shape="turtle")
# Since we do not want the turtle to draw its path, it will have its penup the entire time
tim.penup()
tim.goto(x=-230, y=-100)

# Challenge

import turtle
# Create multiple turtles
turtle_names = []
for i in range(1, 7):
    turtle_names.append(f"turtle{i}")
print(turtle_names)
# ['turtle1', 'turtle2', 'turtle3', 'turtle4', 'turtle5', 'turtle6']

# Create multiple turtle objects
turtle_objects = []
for t in turtle_names:
    t = turtle.Turtle(shape='turtle')
    turtle_objects.append(t)
print(turtle_objects)

# Give each turtle a separate color
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
for i in range(6):
    turtle_objects[i].color(colors[i])


# Place each turtle at their individual starting point
screen = turtle.Screen()
screen.setup(width=500, height=400)
y = -125
for tims in turtle_objects:
    tims.penup()
    tims.goto(-230, y)
    y += 50


# 180 Aaaand, we're off to the races!

# Todos
# Get the turtles moving a random paces between 0 and 10
import random
# random.randint(0, 10)
for tims in turtle_objects:
    tims.forward(random.randint(0, 10))

# Get them to continue moving until they reach a certain point
# From the documentation
#turtle.xcor()
#Return the turtle’s x coordinate.
# Let's say I want them to stop when they reach x=490 (screen width = 500)
import random
game_on = True
while game_on:
    for tims in turtle_objects:
        tims.forward(random.randint(0, 10))
        if tims.xcor() == 490:
            game_on = False

# Check the winning turtle's color with the user_bet
import random
game_on = True
while game_on:
    for tims in turtle_objects:
        tims.forward(random.randint(0, 10))
        if tims.xcor() == 490:
            game_on = False
            if tims.color() == user_bet:
                print('You win')
            else:
                print(f"You Lose. {tims.color()} won")

# Check if the user_bet is in the available colors:
if user_bet in colors:
    # enter code
else:
    print(f"Sorry there is no {user_bet} colored turtle in the race")


# Now put it all together
import turtle
import random
screen = turtle.Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput("Place your bet", "Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

if user_bet in colors:
    game_on = True

    turtle_names = []
    for i in range(1, 7):
        turtle_names.append(f"turtle{i}")

    turtle_objects = []
    for t in turtle_names:
        t = turtle.Turtle(shape='turtle')
        turtle_objects.append(t)

    for i in range(6):
        turtle_objects[i].color(colors[i])

    y = -125
    for tims in turtle_objects:
        tims.penup()
        tims.goto(-230, y)
        y += 50

    while game_on:
        for tims in turtle_objects:
            tims.forward(random.randint(0, 10))
            if tims.xcor() > 230:
                # == will not work because
                # one moment a turtle's xcor() is 225, the next moment it is 231
                # in that case this block will not be triggered
                game_on = False
                if tims.color() == user_bet:
                    print('You win')
                else:
                    print(f"You Lose. {tims.pencolor()} won")
else:
    print(f"Sorry there is no {user_bet} colored turtle in the race")

screen.exitonclick()


# 181 Expand on the Solutions