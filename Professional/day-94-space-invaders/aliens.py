from turtle import *
import random

class Alien:
    def __init__(self):
        self.all_alien = []
        self.create()
        self.score = Turtle()
        self.lives = Turtle()
        self.lives_left = 3
        self.scoreboard()
        self.show_lives()
        self.move_side = 10

        self.all_bombs = []

    def scoreboard(self, points=0):
        self.score.penup()
        self.score.goto(150, 270)
        self.score.color("white")
        self.score.hideturtle()
        self.score.clear()
        self.score.write(f"Points: {points}", font=("Arial", 16, "normal"))

    def show_lives(self):
        self.lives.penup()
        self.lives.goto(-280, 270)
        self.lives.color("white")
        self.lives.hideturtle()
        self.lives.clear()
        self.lives.write(f"Lives: {self.lives_left}", font=("Arial", 16, "normal"))

    def game_end(self, points):
        self.lives.penup()
        self.lives.goto(-200, -50)
        self.lives.color("white")
        self.lives.hideturtle()
        self.lives.clear()
        self.lives.write(f"GAMEOVER\n score: {points}", font=("Arial", 50, "normal"))

    def create(self):
        for pos_y in range(3, 7):
            for pos_x in range(-3, 4):
                self.add_alien(pos_x, pos_y)

    def add_alien(self, x, y):
        new_alien = Turtle(shape="turtle")
        new_alien.penup()
        new_alien.setheading(-90)
        new_alien.color("yellow")
        new_alien.goto(x*40, y*40)
        new_alien.shapesize(stretch_wid=1, stretch_len=1)
        self.all_alien.append(new_alien)

    def move(self):
        for alien in self.all_alien:
            if alien.xcor() > 260 or alien.xcor() < -260:
                self.move_side *= -1
                break
        for alien in self.all_alien:
            new_x = alien.xcor() + self.move_side
            alien.goto(new_x, alien.ycor())

    def drop_bomb(self):
        new_bomb = Turtle(shape="circle")
        new_bomb.setheading(-90)
        new_bomb.color("red")
        new_bomb.penup()
        new_bomb.shapesize(0.2, 0.5, 0.2)

        chosen = random.choice(self.all_alien)
        drop_x = chosen.xcor()
        drop_y = chosen.ycor()
        new_bomb.goto(drop_x, drop_y)

        self.all_bombs.append(new_bomb)

    def drop_move(self):
        for bomb in self.all_bombs:
            if bomb.ycor() > -250:
                bomb.forward(30)
            else:
                bomb.hideturtle()
                self.all_bombs.remove(bomb)