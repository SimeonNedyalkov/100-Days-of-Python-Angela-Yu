import turtle
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
turtle.tracer(0)

paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard((300,300))

paddle_left.screen.onkey(key="w", fun=paddle_left.move_up)
paddle_left.screen.onkey(key="s", fun=paddle_left.move_down)
paddle_right.screen.onkey(key="Up", fun=paddle_right.move_up)
paddle_right.screen.onkey(key="Down", fun=paddle_right.move_down)


game_is_on = True
while game_is_on:
    turtle.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() > -320 :
        ball.bounce_from_paddle()
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.goal_l()
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.goal_r()









screen.exitonclick()
