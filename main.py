import time
from turtle import Screen
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
car = Car()
score = Score()

screen.listen()
screen.onkeypress(turtle.move, "w")
screen.onkeypress(turtle.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.scoring()
    car.create_car()
    car.race()

    for vehicle in car.all_cars:
        if vehicle.distance(turtle) < 20:
            game_is_on = False
            score.over()
    if turtle.ycor() > 280:
        turtle.reposition()
        car.level_up()
        score.inc_score()

screen.exitonclick()
