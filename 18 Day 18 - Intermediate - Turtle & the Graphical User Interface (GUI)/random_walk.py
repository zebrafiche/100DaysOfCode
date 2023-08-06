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