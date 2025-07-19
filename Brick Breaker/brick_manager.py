from turtle import Turtle

class BrickManager:
    def __init__(self, level):
        self.all_bricks = []
        self.create_bricks(level)

    def create_bricks(self, level):
        colors = ["red", "orange", "green", "yellow"]
        y = 250
        rows = level + 2
        for i in range(rows):
            color = colors[i % len(colors)]
            for x in range(-350, 360, 75):
                brick = Turtle("square")
                brick.color(color)
                brick.shapesize(stretch_wid=1, stretch_len=3)
                brick.penup()
                brick.goto(x, y)
                self.all_bricks.append(brick)
            y -= 30

    def destroy_brick(self, brick):
        brick.hideturtle()
        self.all_bricks.remove(brick)
