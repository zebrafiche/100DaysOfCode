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