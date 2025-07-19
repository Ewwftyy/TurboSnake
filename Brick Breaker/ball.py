from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.goto(0, -230)
        self.x_move = 4
        self.y_move = 4
        self.speed_factor = 0.015

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(0, -230)
        self.bounce_y()

    def increase_speed(self):
        self.speed_factor *= 0.8
        self.x_move *= 1.1
        self.y_move *= 1.1

