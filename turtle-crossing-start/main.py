import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(fun=turtle.move,key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.movement_of_car()
    for car in cars.all_cars:
        if car.distance(turtle) < 23:
            game_is_on = False
            score.game_over()



    if turtle.is_at_finish():
        turtle.start_again()
        cars.level_up()
        score.update_score()
        score.increase_level()




screen.exitonclick()