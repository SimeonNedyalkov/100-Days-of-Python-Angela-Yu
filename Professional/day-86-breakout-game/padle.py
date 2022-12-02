import turtle
from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(0, -260, )
        self.pendown()

    def left(self):
        self.penup()
        if self.xcor() > -320:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())

    def right(self):
        self.penup()
        if self.xcor() < 320:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

