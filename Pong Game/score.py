from turtle import Turtle
from ball import Ball
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updated_score()

    def updated_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 50, "normal"))

    def increase_score_of_right(self):
        self.r_score += 1
        self.updated_score()

    def increase_score_of_left(self):
        self.l_score += 1
        self.updated_score()

    def win(self):
        self.color("yellow")
        self.goto(0, 0)
        if self.l_score ==10:
            self.write(f"left won with {self.l_score} points",align="center", font=("courier", 15, "normal"))
        if self.r_score ==10:
            self.write(f"right won with {self.r_score} points",align="center", font=("courier", 15, "normal"))
