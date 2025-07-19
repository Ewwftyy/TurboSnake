from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        x = self.xcor() - 30
        if x > -350:
            self.goto(x, -250)

    def move_right(self):
        x = self.xcor() + 30
        if x < 350:
            self.goto(x, -250)
