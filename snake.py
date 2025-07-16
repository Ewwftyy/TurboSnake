from turtle import Turtle
STARTING_POS = [(0,0),(-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.seg_list =[]
        self.create_snake()
        self.head=self.seg_list[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_seg(pos)

    def add_seg(self,pos):
        seg = Turtle("square")
        seg.color("white")
        seg.penup()
        seg.goto(pos)
        self.seg_list.append(seg)

    def extend(self):
        self.add_seg(self.seg_list[-1].position())


    def move(self):
        for seg_num in range(len(self.seg_list) - 1, 0, -1):
            new_x = self.seg_list[seg_num - 1].xcor()
            new_y = self.seg_list[seg_num - 1].ycor()
            self.seg_list[seg_num].goto(new_x, new_y)

        self.seg_list[0].fd(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



