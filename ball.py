from turtle import Turtle
from constant import *


class Ball(Turtle):
    def __init__(self, xcor=0, ycor=0):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=BALL_STRETCH_DIAMETER, stretch_len=BALL_STRETCH_DIAMETER)
        self.penup()
        self.goto(xcor, ycor)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        # Detect collision with wall
        if self.ycor() >= (SCREEN_HEIGHT / 2) - BALL_DIAMETER or self.ycor() <= (-SCREEN_HEIGHT / 2) + BALL_DIAMETER:
            self.bounce_y()

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
