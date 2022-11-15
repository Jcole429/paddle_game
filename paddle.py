from turtle import Turtle
from constant import *


class Paddle(Turtle):

    def __init__(self, xcor=0, ycor=0):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_STRETCH_WIDTH, stretch_len=PADDLE_STRETCH_LENGTH)
        self.penup()
        self.goto(xcor, ycor)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
