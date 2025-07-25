STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.start_again()
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(10)


    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

    def start_again(self):
        self.goto(STARTING_POSITION)