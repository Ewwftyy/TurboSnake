from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from brick_manager import BrickManager
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Brick Breaker")
screen.tracer(0)


paddle = Paddle()
ball = Ball()
game_text = Turtle()
game_text.hideturtle()
game_text.color("white")
game_text.penup()
level = 1
bricks = BrickManager(level)

screen.listen()
screen.onkey(paddle.move_left, "Left")
screen.onkey(paddle.move_right, "Right")

lives = 3
running = True
while running:
    time.sleep(ball.speed_factor)
    screen.update()
    ball.move()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.bounce_x()

    if ball.ycor() > 290:
        ball.bounce_y()

    if ball.distance(paddle) < 50 and ball.ycor() < -230:
        ball.bounce_y()

    for brick in bricks.all_bricks:
        if ball.distance(brick) < 40:
            bricks.destroy_brick(brick)
            ball.bounce_y()
            break

    if ball.ycor() < -290:
        lives -= 1
        ball.reset_position()
        if lives == 0:
            game_text.goto(0, 0)
            game_text.write("GAME OVER", align="center", font=("Courier", 32, "bold"))
            running = False

    if not bricks.all_bricks:
        level += 1
        if level > 3:
            game_text.goto(0, 0)
            game_text.write("GAME OVER", align="center", font=("Courier", 32, "bold"))
            running = False
        else:
            ball.increase_speed()
            bricks = BrickManager(level)
            ball.reset_position()

screen.exitonclick()