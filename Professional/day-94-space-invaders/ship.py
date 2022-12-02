from turtle import Turtle

ship_pos = ()

class Ship(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shapesize(2)
        self.shape('triangle')
        self.color('green')
        self.setheading(90)
        self.penup()
        self.goto(0,-250)
        self.showturtle()

    def move_left(self):
        self.setheading(180)
        self.penup()
        self.forward(30)
        self.setheading(90)

    def move_right(self):
        self.setheading(360)
        self.penup()
        self.forward(30)
        self.setheading(90)

    def ship_location(self):
        global ship_pos
        ship_pos = self.pos()
        return ship_pos

