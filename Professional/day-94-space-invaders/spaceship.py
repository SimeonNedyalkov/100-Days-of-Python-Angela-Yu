from turtle import Turtle

class Spaceship:
    def __init__(self):
        self.ship = Turtle(shape="arrow")
        self.ship.color("green")
        self.ship.setheading(90)
        self.ship.penup()
        self.ship.goto(0, -200)
        self.ship.shapesize(2, 1, 1)
        self.stop_bullet = True

        self.lives = 3

        self.bullet = Turtle(shape="circle")
        self.bullet.setheading(90)
        self.bullet.color("blue")
        self.bullet.penup()
        self.bullet.shapesize(0.2, 0.5, 0.2)
        self.bullet.goto(0, -250)
        self.bullet.speed(1)
        self.bullet.hideturtle()

    def move_right(self):
        if self.ship.xcor() < 250:
            new_x = self.ship.xcor() + 20
            self.ship.goto(new_x, self.ship.ycor())

    def move_left(self):
        if self.ship.xcor() > -250:
            new_x = self.ship.xcor() - 20
            self.ship.goto(new_x, self.ship.ycor())

    def died(self):
        self.lives -= 1

    def shoot(self):
        if self.stop_bullet:
            self.bullet.goto(self.ship.xcor(), -200)
            self.bullet.showturtle()
            self.stop_bullet = False

    def bullet_move(self):
        if self.bullet.ycor() < 250:
            self.bullet.forward(30)
            self.stop_bullet = False
        else:
            self.stop_bullet = True