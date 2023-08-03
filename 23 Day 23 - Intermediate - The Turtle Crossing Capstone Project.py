# 206 Day 23 Goals_ what you will make by the end of the day

# We will build a game just like crossy road


# 208 How to use the Starter Code

# We have four different files to work with_-

# player - this is a file containing the player class, you will create player object that you will control
# car manager - car classes, you will create multiple car object that will run randomly across the screen
# scoreboard - scoreboard class, delineating the level we are currently on and the game over sequence
# main/turtle_crossing - the main game

# As of now the turtle_crossing file has this -

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
# setting up the screen to the desired dimensions
screen.tracer(0)
# turning off continuous refresh

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # putting a 0.1-second lag before the screen updates
    screen.update()


# 209 Step 1 - Check out how the game play works

# 210 Step 2 - Break down the Problem

# These are web files, with written instructions
# Takeaways -
# player object will move north responding to key press
# car objects will move from east to west, with increasing speed at each level
# if the player object hits a car object it is game over

# Problem Breakdown
# 1. Create a player class
# 2. Create a car class
# 3. Once the player hits the car it is game over
# 4. When the player reaches y = 280, create a new level with faster cars and the player at the bottom
# 5. Scoreboard


# 211 Solution to Step 3 - Create the Player Behaviour

# in the player.py file, add -
from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.back(MOVE_DISTANCE)

# in the turtle_crossing.py file, add -
screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


# 212 Solution to Step 4 - Create the Car Behaviour

# in the car_manager.py file, add -

from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def move(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def create_cars(self):
        # to stop the cars from being generated too frequently -
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            # this will create cars only when the random_chance is 6, other times it will skip
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-250, 250))
            new_car.left(180)
            self.all_cars.append(new_car)

# in the turtle_crossing.py file, add -


cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()


# 213 Solution to Step 5 - Detect when the Turtle collides with a Car _squish_

# in the turtle_crossing.py file, add -

    for i in cars.all_cars:
        if i.distance(player) < 20:
            game_is_on = False


screen.exitonclick()

# You can see now that whenever the player turtle comesin contact with any of the car turtles, it stops the game


# 214 Solution to Step 6 - Detect when the Player has reached the other side

# in the player.py file, add -

class Player(Turtle):
    self.reset()


def reset(self):
    self.goto(STARTING_POSITION)

# in the car_manager.py file, add -


class CarManager:
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE


def move(self):
    for car in self.all_cars:
        car.forward(self.car_speed)


def move_faster(self):
    # global STARTING_MOVE_DISTANCE
    # STARTING_MOVE_DISTANCE += MOVE_INCREMENT
    self.car_speed += MOVE_INCREMENT

# finally, in the turtle_crossing.py file, add -


if player.ycor() > 280:
    player.reset()
    cars.move_faster()


# 215 Solution to Step 7 - Add the Scoreboard and Game Over sequence

# in the scoreboard.py file, add -

from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align='center', font=FONT)

# in the turtle_crossing.py file, add -


for i in cars.all_cars:
    if i.distance(player) < 20:
        level.game_over()
        game_is_on = False
if player.ycor() > 280:
    player.reset()
    level.level_up()
    cars.move_faster()


# That's it. That's the entire game

# car_manager.py -

from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def create_cars(self):
        # to stop the cars from being generated too frequently -
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            # this will create cars only when the random_chance is 6, other times it will skip
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(300, random.randint(-250, 250))
            new_car.left(180)
            self.all_cars.append(new_car)

    def move_faster(self):
        # global STARTING_MOVE_DISTANCE
        # STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.car_speed += MOVE_INCREMENT

# player.py

from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.setheading(90)
        self.reset()

    def move_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.setheading(90)
        self.back(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)

# scoreboard.py

from turtle import Turtle
FONT = ("Courier", 12, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align='center', font=FONT)

# and turtle_crossing.py -

import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
level = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')
screen.onkey(player.move_left, 'Left')
screen.onkey(player.move_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()
    for i in cars.all_cars:
        if i.distance(player) < 20:
            level.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.reset()
        level.level_up()
        cars.move_faster()

screen.exitonclick()


# 216 This course is not about typing out code

