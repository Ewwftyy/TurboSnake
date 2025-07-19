from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from score import Score

t= 0.1
screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong Game")
screen.tracer(0)

left_paddle = Paddle((-350,0))
right_paddle = Paddle((350,0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(right_paddle.go_up,"Up")
screen.onkey(right_paddle.go_down,"Down")
screen.onkey(left_paddle.go_up,"w")
screen.onkey(left_paddle.go_down,"s")

game_on = True
while game_on:
    time.sleep(ball.sped)
    screen.update()
    ball.move()



    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320  or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_pos()
        score.increase_score_of_left()


    if ball.xcor() < -380:
        ball.reset_pos()
        score.increase_score_of_right()

    if score.l_score == 10 or score.r_score == 10:
        game_on = False
        score.win()





screen.exitonclick()