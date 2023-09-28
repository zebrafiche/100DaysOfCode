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