import time
from turtle import Screen
from scoreboard import Scoreboard

from food import Food
from snake import Snake


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("my big snake")
screen.tracer(0)
snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.down,"Down")

game_on = True

delay = 0.08

while game_on:
    screen.update()
    time.sleep(delay)
    snake.move()

    if snake.head.distance(food) < 19:
        food.refresh()
        snake.extend()
        score.increase_score()

        if score.score % 10 == 0:
            delay = max(0.02, delay - 0.01)

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    for seg in snake.seg_list[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.game_over()












screen.exitonclick()