import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5


class Car:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            start_y = random.randint(-250, 250)
            new_car.goto(300, start_y)
            self.all_cars.append(new_car)

    def race(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

