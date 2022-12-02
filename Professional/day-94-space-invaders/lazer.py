from turtle import Turtle
#from main import ship


class Lazer():
    def __init__(self):
        self.all_lazers = []

    def shoot(self):
       for _ in self.all_lazers:
           _.forward(1000)

    def create_lazer(self,x,y):
        new_lazer = Turtle()
        new_lazer.penup()
        new_lazer.speed(2)
        new_lazer.shape("square")
        new_lazer.shapesize(0.5,0.3)
        new_lazer.color('green')
        new_lazer.goto(x,y)
        new_lazer.setheading(90)
        self.all_lazers.append(new_lazer)