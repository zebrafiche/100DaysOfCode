from turtle import Turtle
import random


class Food(Turtle):
    # not the lowercase turtle because turtle is the module and Turtle is a class inside that module we want to inherit
    def __init__(self):
        super().__init__()
        # now to add some attributes
        # we will use the shape attribute from the turtle class
        self.shape('circle')
        # before we would have done tim = Turtle(), tim.shape
        # now we are calling for the same method inside the food class, so self.shape()
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        # turtle.shapesize(stretch_wid=None, stretch_len=None, outline=None)
        self.color('blue')
        self.speed(0)
        # random_x = random.randint(-280, 280)
        # random_y = random.randint(-280, 280)
        # self.goto(random_x, random_y)
        # self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
