from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.fillcolor('white')
        self.setheading(270)
        self.x_move = -10
        self.y_move = -60
        self.move_speed = 0.2


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.penup()
        self.goto(new_x, new_y)

    def bounce_from_paddle(self):
        self.y_move *= -1

    def bounce_from_block(self):
        self.y_move *= +1

    def bounce_from_wall(self):
        self.x_move *= -1