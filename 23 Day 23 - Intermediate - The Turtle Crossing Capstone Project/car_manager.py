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

