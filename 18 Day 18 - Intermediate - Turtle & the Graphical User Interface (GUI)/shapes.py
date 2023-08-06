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