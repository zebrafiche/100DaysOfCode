import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from another_car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = []

screen.listen()
screen.onkey(player.move_up, 'Up')
screen.onkey(player.move_down, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1, 6)
    if random_chance == 6:
        # this will create cars only when the random_chance is 6, other times it will skip
        car = CarManager()
        cars.append(car)
    for i in cars:
        i.move()
