
# 163 Day 18 Goals_ what we will make by the end of the day

# We are going to go deeper in turtle and turtle graphics
# By the end of the day, we will have created a code that generates artwork


# 164 Understanding Turtle Graphics and How to use the Documentation

from turtle import Turtle, Screen

tim = Turtle()

# When you run this, you can see a brief flash of a window and then it disappears
# In order to keep the window stay where it is -

# screen = Screen()
# screen.exitonclick()

# Now when you run it, the screen shows up and stays, only goes away when you click on it
# And these two lines need to be at the very bottom, so that the opened screen shows all our workings

# Now go to the documentation and find the shape() function from the table of contents
# turtle.shape(name=None)
# Set turtle shape to shape with given name or, if name is not given, return name of current shape.
# Shape with name must exist in the TurtleScreen’s shape dictionary.
# Initially there are the following polygon shapes: “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”.

# change the shape -

tim.shape('turtle')
# screen = Screen()
# screen.exitonclick()

# You can see on the window that the shaoe of the cursor has changed to a turtle

# You cannot read through the entire documentation before using a module
# What you can do is you can google, and then find answers from StackOverflow, and then look it up on the documentation
# So you will get it better

# Change the color
# From the documentation -
# turtle.color(*args)

tim.color("black", "red")
# screen = Screen()
# screen.exitonclick()
# You can see that now the fill color is red and the outline is black

# How do I know which colors I can use?
# From the documentation -
# color()
# Return the current pencolor and the current fillcolor as a pair of color specification strings or tuples
# as returned by pencolor() and fillcolor().
#
# Click pencolor()
# It says that it uses a Tk color specification string
# Which comes from the tkinter module

# So under the hood, turtle uses tkinter

# An easier way to see the colors is through a web page where you can see the colors and the corresponding info
# Should be out there in google


# Let's see how we can make it do certain things
# From the documentation -

tim.forward(100)
# screen = Screen()
# screen.exitonclick()

# You can see the turtle moves a hundred paces forward

# Change direction
# From the documentation -

# turtle.right(angle)
# turtle.left(angle)

tim.left(45)
tim.forward(100)
# screen = Screen()
# screen.exitonclick()

# You can see the turtle changes direction and moves forward a hundred paces


# 165 Turtle Challenge 1 - Draw a Square

for _ in range (4):
    tim.forward(100)
    tim.right(90)
# screen = Screen()
# screen.exitonclick()

# Change the name of your turtle from timmy to tim using the refactor feature in PyCharm
# Just click on timmy anywhere, right click, refactor, rename
# All the names have changed


# 166 Importing Modules, Installing Packages, and Working with Aliases

'''
Ways you can import - 

import turtle
tim = turtle.Turtle()

from turtle import Turtle
tim = Turtle()
tom = Turtle()
terry = Turtle()

from turtle import *
(imports everything from the module)
tim = Turtle()
tom = Screen()
(confusing, because....)
forward()
left()
(...these will be valid and leave the reader confused as to where they came from)

example
from random import *
print(choice([1, 2, 4]))
(the reader will be confused as to where choice came, which module it belongs to etc.)

'''

# Aliasing modules
# Suppose you have a module with a really long name
import turtle as t
tummy = t.Turtle()

# Installing Modules
# There are some modules that do not come preinstalled
# You have to install them separately

# import heroes
# You see an error
# (Pycharm) Hover over the error, click on the red bulb icon, it will give you an option to install


# 167 Turtle Challenge 2 - Draw a Dashed Line

# Essentially move for 10 paces
# tim.forward(10)
# # Then move without drawing for 10 paces
# tim.penup()
# tim.forward(10)
# # Repeat 50 times
# for i in range(50)

# Now put it together

for i in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()

screen = Screen()
screen.exitonclick()

# You can see that it draws a dotted linecache, nice


# 168 Turtle Challenge 3 - Drawing Different Shapes

# Draw a triangle, then square, then pentagon etc.

# Determine no. of sides
for i in range (3, 9):
    print(i)
# Determine angles
    angle = 360/i
# Make robot turn angle
    tim.right(angle)
# Make robot draw
    tim.forward(100)
# Make robot do this the required number of times to draw the shape
    for j in range(i):
        tim.right(angle)
        tim.forward(100)
# Change color at every iteration
def change_color():
    from random import randint
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    # this function should be called after angle = 360/i

# Now put it all together

from turtle import Turtle, Screen
tim = Turtle()
screen = Screen()
# you have to have a screen object
from random import randint


for i in range (3, 9):
    angle = 360/i
    screen.colormode(255)
    # colormode for the screen object must be changed to 1.0 or 255 (rgb range) before you attempt to change pencolor
    # and r, g, b values of color triples have to be in the range 0 - colormode
    R = randint(0, 255)
    G = randint(0, 255)
    B = randint(0, 255)
    tim.pencolor((R, G, B))
    # pencolor changed, will change everytime the number of sides changes, i.e. before a new shape is drawn
    for j in range(i):
        tim.forward(100)
        tim.right(angle)

screen.exitonclick()


# 169 Turtle Challenge 4 - Generate a Random Walk

# choose random direction
# the video shows angle change of 0, 90, 180, though we can make it like a range from 0 to 360
import random
random.randint(0, 360)
# or
possible_angles = [0, 90, 180, 360]
random.choice(possible_angles)

# move in the random direction
import turtle
tim = turtle.Turtle()
tim.forward(30)

# make the movement continue
n = 0
while n <= 100:
    # put code here
    n += 1

# make lines thicker
tim.pensize(5)

# choose different color for every pace
R = random.randint(0, 255)
G = random.randint(0, 255)
B = random.randint(0, 255)
screen.colormode(1.0)
# colormode for the screen object must be changed to 1.0 or 255 (rgb range) before you attempt to change pencolor
# and r, g, b values of color triples have to be in the range 0 - colormode
tim.pencolor((R, G, B))

# change turtle speed

# from the documentation
# turtle.speed(speed=None)
# Parameters
# speed – an integer in the range 0..10 or a speedstring (see below)
# Set the turtle’s speed to an integer value in the range 0..10. If no argument is given, return current speed
# “fastest”: 0, “fast”: 10, “normal”: 6, “slow”: 3, “slowest”: 1

tim.speed(0)

# Now put it all together

import turtle
import random
tim = turtle.Turtle()
screen = turtle.Screen()
tim.pensize(5)
tim.speed(0)
n = 0
while n <= 100:
    # put code here
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    screen.colormode(255)
    tim.pencolor((R, G, B))
    possible_angles = [0, 90, 180, 270, 360]
    tim.setheading(random.choice(possible_angles))
    tim.forward(30)
    n += 1


# 170 Python Tuples and How to Generate Random RGB Colours

# we can change colors using rgb tuples
# what is a tuple
# it is a data type that looks like this - (1, 2, 3)

my_tuple = (1, 5, 7)
print(my_tuple[1])
# 5

# what is different here from list?
# well a tuple is carved in stone, no change in values allowed
my_tuple[2] = 15
# TypeError: 'tuple' object does not support item assignment

# why would you use tuples? creating a color scheme for your website, a sensitive data which, if changed in any
# manner, will mess the look of site. in that case, create a tuple of color schemes, not list

# changing a tuple into a list

my_list = list(my_tuple)
print(my_list)
# [1, 5, 7]

# coming back to the color change problem
# apparenty we have to change the color on the module level
# so -
from turtle import Turtle
turtle.colormode(255)
def random_color:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# when you want to change color
tim.color(random_color())


# 171 Turtle Challenge 5 - Draw a Spirograph

# draw a circle

# turtle.circle(radius, extent=None, steps=None)
# Parameters - radius – a number, extent – a number (or None), steps – an integer (or None)
# turtle.circle(120, 180)  # draw a semicircle
from turtle import Turtle
tim = Turtle()
tim.circle(5)

# change angle of the second circle
for angle in range(0, 360):
    tim.setheading(angle)
    tim.circle(5)

# keep drawing circles till you reach the starting point
for angle in range(0, 360):
    tim.setheading(angle)
    tim.circle(5)

# change colors for each circle
from turtle import Turtle
tim = Turtle()
turtle.colormode(255)
def random_color:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# Now put it all together

import turtle
import random
from turtle import Turtle, Screen
screen = Screen()
tim = Turtle()
tim.speed(0)
turtle.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

for angle in range(0, 360, 5):
    tim.color(random_color())
    tim.setheading(angle)
    tim.circle(100)

screen.exitonclick()


# 172 The Hirst Painting Project Part 1 - How to Extract RGB Values from Images

# install colorgram
# Install the package into our project (Settings > Project > Python Interpreter > +(bottom) > search and install)

# extract colors from an image
# from the documentation -
# # Extract 6 colors from an image.
# colors = colorgram.extract('sweet_pic.jpg', 6)

import colorgram
colors = colorgram.extract('hirst_spot.jpg', 6)
print(colors)
# [<colorgram.py Color: Rgb(r=245, g=239, b=227), 32.3002926696463%>,
# <colorgram.py Color: Rgb(r=235, g=240, b=247), 24.715838192254463%>,
# <colorgram.py Color: Rgb(r=247, g=237, b=243), 20.096649045987704%>,
# <colorgram.py Color: Rgb(r=235, g=246, b=240), 17.653197812918304%>,
# <colorgram.py Color: Rgb(r=193, g=159, b=126), 3.278353789958482%>,
# <colorgram.py Color: Rgb(r=66, g=95, b=120), 1.9556684892347482%>]
# this is a list containing color objects

# colorgram.extract returns Color objects, which let you access RGB, HSL, and what proportion of the image was that color.
# first_color = colors[0]
# rgb = first_color.rgb # e.g. (255, 151, 210)
# hsl = first_color.hsl # e.g. (230, 255, 203)
# proportion  = first_color.proportion # e.g. 0.34

# therefore to access rgb tuples of the colors -

color_palette = []
for i in colors:
    color_palette.append(i.rgb)
print(color_palette)

# [Rgb(r=245, g=239, b=227),
#  Rgb(r=235, g=240, b=247),
#  Rgb(r=247, g=237, b=243),
#  Rgb(r=235, g=246, b=240),
#  Rgb(r=193, g=159, b=126),
#  Rgb(r=66, g=95, b=120)]

# from the documentation -
# RGB and HSL are named tuples, so values can be accessed as properties. These all work just as well:
# red = rgb[0]
# red = rgb.r
# saturation = hsl[1]
# saturation = hsl.s

color_palette = []
for i in colors:
    # get the rgb named tuple
    rgb = i.rgb
    # from the named tuple, get the red, green and blue separately
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    # append it into a tuple
    rgb_codes = (red, green, blue)
    # append the tuple into the list
    color_palette.append(rgb_codes)
print(color_palette)
# [(245, 239, 227), (235, 240, 247), (247, 237, 243), (235, 246, 240), (193, 159, 126), (66, 95, 120)]
# We quick check on the rgb viewer online shows that the closer the values are to 255, the more chance they are whites
# delete them
# [(193, 159, 126), (66, 95, 120)]
# Do not worry, we will get more colors extracted later, so we will have more actual colors to work with


# 173 The Hirst Painting Project Part 2 - Drawing the Dots

import colorgram
colors = colorgram.extract('random_image.jpg', 50)
color_palette = []
for i in colors:
    # get the rgb named tuple
    rgb = i.rgb
    # from the named tuple, get the red, green and blue separately
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    # append it into a tuple
    rgb_codes = (red, green, blue)
    # append the tuple into the list
    color_palette.append(rgb_codes)

# pick a random color
import random
color = random.choice(color_palette)

# paint a dot with turtle
import turtle
hirst = Turtle()
# from the documentation -
# turtle.dot(size=None, *color) [size – an integer >= 1 (if given), color – a colorstring or a numeric color tuple]
# Draw a circular dot with diameter size, using color. If size is not given, the maximum of pensize+4 and 2*pensize is used.
hirst.dot(20, color)

# lift the pen
hirst.penup()

# move 20 paces
hirst.forward(50)

# pen down
turtle.pendown()

# repeat
# the drawing is to be 10x10 square
# to draw 10 dots -
for i in range(1, 11):
    # enter code here
# at the beginning every line, the turtles x coordinates will remain same but y coordinates increment by 50
x += 50
hirst.setposition(x, 0)
# and this will happen 9 times for every iteration
for n in range(1, 10):
    # enter code here

# Now put it all together

import colorgram
import random
import turtle
screen = turtle.Screen()
hirst = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)

hirst.penup()
# I do not want to see the turtle relocating, so penup()
hirst.hideturtle()
# this will not show the turtle as it draws
hirst.speed(0)

colors = colorgram.extract('random_image.jpg', 50)
color_palette = []
for i in colors:
    # get the rgb named tuple
    rgb = i.rgb
    # from the named tuple, get the red, green and blue separately
    red = rgb.r
    green = rgb.g
    blue = rgb.b
    # append it into a tuple
    rgb_codes = (red, green, blue)
    # append the tuple into the list
    color_palette.append(rgb_codes)

x, y = -200, -200
for n in range(1, 11):
    hirst.setposition(x, y)
    for i in range(1, 11):
        color = random.choice(color_palette)
        hirst.dot(20, color)
        hirst.penup()
        hirst.forward(50)
        turtle.pendown()
        # we could just write hirst.penup() once at the top, that would do the same thing
        # hirst would have its pen up, paint the dot and move on, keeping the pen up
    y += 50
screen.exitonclick()


# 174 Space out your study sessions and stay consistent