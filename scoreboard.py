from turtle import Turtle
from food import Food

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.write(f"Score : {self.score} ", align="center", font=("Courier", 10, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.color("yellow")
        self.write(f"your Score is : {self.score}, GAME OVER ", align="center", font=("Courier", 10, "normal"))
        self.game_on = False
        
