# 188 Day 21 Goals_ what we will make by the end of the day

# We are going to learn about another important concept in OOP
# That is class inheritance
# Classes can inherit from other classes attributes methods etc.
#
# We will also learn about slicing with lists
#
# And finally finish up our snake game, we have four remaining objectives -
# Detect Food
# Scoreboard
# Detect Wall
# Detect Tail


# 189 Class Inheritance

# Let's say you have a class called chef, and in it you have attributes and methods
# Methods like bake(), stir(), measure()
# Now let's say you ought to have another class with some extended capabilities
# Maybe methods called mix(), fold(), season()
# But you will also need the base methods - bake(), stir(), measure()
# You can just add the old methods to the new class, and this process is called class inheritance
# You can inherit both attributes and methods

# How does this class inheritance work in terms of code -
# class name_of_class(class_you_want_to_inherit_from):
#     def __init__(self):
#         super.__init__()
#         this last line inherits all the attributes and methods from the superclass(class_you_want_to_inherit_from)
#         The call to super() in the initialiser is recommended, but not strictly required
# Example -

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

# Now let us create another class which inherit the properties of Animal class


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print('moving in water')


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# moving in water
# Inhale, exhale
# 2

# What if I wanted to inherit the function but add to it in my new class?


class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

# Now let us create another class which inherit the properties of Animal class


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print('moving in water')

    def breathe(self):
        super().breathe()
        # inherit the existing method from the superclass (Animal)
        print('doing this underwater')
        # Adding to it


nemo = Fish()
nemo.breathe()
# Inhale, exhale
# doing this underwater


# 190 Detect Collisions with Food

# create food

from turtle import Turtle
food = Turtle()

# challenge - create a class, food
from turtle import Turtle


class food:
    def __init__(self):
        self.food = Turtle()

# challenge 2 - now instead of creating an initialization, why don't we inherit all of turtle's properties
# that way our food class will be able to behave just like a turtle but it will also have some other capabilites


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

# make the turtle generate itself is a random location in the screen
# our screen is 600 by 600
import random
random_x = random.randint(-280, 280)
# not 300, 300 because that would generate the turtle right at the edge
random_y = random.randint(-280, 280)

# usually it would be
# tim.goto(random_x, random_y)
# but since now we are doing this inside a Food class, it would be -

self.goto(random_x, random_y)

# All of this code above is going to be used to create our food class
# So the food class looks like this

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
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


# now
# when the food and the snake collides, the food should regenerate itself in a random location
# turtle.distance(x, y=None)
# Return the distance from the turtle to (x,y), the given vector, or the given other turtle, in turtle step units.
# turtle.home()
# turtle.distance(30,40)
# 50.0

# So using that method
if snake.head.distance(food) < 15:
    # distance == 0 wont work because one moment the snake head might be 1 pixel away from the food,
    # and the other moment further
    # by default a circle shape is 20 pixels, we resized it by 0.5, so now it is 10 pixels
    # allowing for some kind of buffer, keeping the distance less than 15
    print('nom nom nom')

# replace nom nom nom with the food regeneration

# add another function in the food module inside the Food class

def refresh(self):
    random_x = random.randint(-280, 280)
    random_y = random.randint(-280, 280)
    self.goto(random_x, random_y)

# and then call on this function in the initialization block, good practice but not necessary


# 191 Create a Scoreboard and Keep Score

# turtle.write(arg, move=False, align='left', font=('Arial', 8, 'normal'))
# turtle.write("Home = ", True, align="center")

# create a counter
score = 0
# so the score counter will change every time the turtle eats food
if snake.head.distance(food) < 15:
    score += 1
# create a turtle object that displays the text involving the counter
scoreboard = Turtle()
scoreboard.write(f"Score: {score}", False, align= "center")
# do this all inside a class
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.write(f"Score: {score}", False, align="center")
# it should have a refresh method to update the score
def refresh(self):
    self.clear()
    self.goto(0, 280)
    self.write(f"Score: {score}", False, align="center")

# now put it all together in a separate scoreboard.py file

from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color('white')
        # this line comes before the self.write because otherwise the turtle would write in black before changing color
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center")

    def refresh(self):
        self.score += 1
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", False, align="center")

# timestamp - 04:51


# 192 Detect Collisions with the Wall

# form boundaries
left_border = (-280, y)
right_border = (280, y)
top_border = (x, 280)
bottom_border = (x, -280)
# create a new function that prints game over status
def game_over(self):
    self.home()
    self.pendown()
    self.write(f"self.write(f"You hit the wall./nScore: {self.score}", False, align=ALIGNMENT, font=FONT))

# everytime snake hits boundary print sth, with score printed on screen
if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_on = False
    points.game_over


# 193 Detect Collisions with your own Tail

# increase snake length everytime it eats food
# in the snake class
def increase_length(self):
    new_turtle = Turtle(shape='square')
    new_turtle.color('white')
    self.turtles.append(new_turtle)
# now trigger this function everytime the snake eats food
# in the snake_game
if snake.head.distance(food) < 15:
    snake.increase_length()
# now detect collision with tail
# in the snake_game
for i in range (1, len(snake.turtles)):
    if snake.head.position() == snake.turtles[i].position:
        # wrong statement, one moment they can be 2 pixels away, the next moment overlapper and now 3 pixels away
        # the if statement would never trigger
        points.game_over()
# OR

for i in snake.turtles[1:len(snake.turtles)]:
    if snake.head.distance(i) < 10:
        points.game_over()


# 194 How to Slice Lists & Tuples in Python

# new concept - slicing
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(lista[2:5])
# ['c', 'd', 'e']

print(lista[2:])
# ['c', 'd', 'e', 'f', 'g']

print(lista[:5])
# ['a', 'b', 'c', 'd', 'e']

print(lista[2:5:2])
# ['c', 'e']
# 2 is the step

# now lets say i do not want to start at two, but beginning
# i also want to capture all items till the end
# furthermore i also want to capture every other item, i.e step = 2

print(lista[::2])
# ['a', 'c', 'e', 'g']

# now start from the end
lista[::-1]
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Now put it all together

from turtle import Screen
import time
import snake
import food
import scoreboard
screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor('black')
screen.title("Rafi's snake game")
screen.tracer(0)

snake = snake.Snake()
food = food.Food()
food.refresh()
points = scoreboard.scoreboard()
screen.update()


# def move_right():
#     turtle1.setheading(0)
#
#
# def move_left():
#     turtle1.setheading(180)
#
#
# def move_up():
#     turtle1.setheading(90)
#
#
# def move_down():
#     turtle1.setheading(270)


screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        points.refresh()
        snake.increase_length()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        game_on = False
        points.game_over()

    for i in snake.turtles[1:]:
        if snake.head.distance(i) < 10:
            game_on = False
            points.game_over()


screen.exitonclick()


# 195 Stay motivated by remembering the reason you signed up