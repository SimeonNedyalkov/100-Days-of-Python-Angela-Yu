from turtle import Turtle, Screen
import time
import padle
from padle import Paddle
from blocks import Block
from ball import Ball
from scoreboard import Scoreboard

# Screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.listen()

# Objects
paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard(150)


# Game
game_on = False
screen.onkey(key='a', fun=paddle.left)
screen.onkey(key='d', fun=paddle.right)

block=Block()
blocks = block.create_blocks()

def game():
    while game_on == False:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        if ball.distance(paddle) < 40:
            ball.bounce_from_paddle()
        for _ in block.all_blocks:
            if ball.distance(_) < 40:
                scoreboard.destroyed_blocks()
                scoreboard.update_scoreboard()
                ball.bounce_from_paddle()
                block.all_blocks.remove(_)
                _.hideturtle()

        if ball.ycor() > 260 or ball.ycor() < -260:
            ball.bounce_from_paddle()
        if ball.xcor() > 360 or ball.xcor() < -360:
            ball.bounce_from_wall()


game()





screen.exitonclick()
