import random
import time
from turtle import *
from spaceship import Spaceship
from aliens import Alien

screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor('black')
screen.listen()
ship = Spaceship()
alien = Alien()


screen.onkey(key='a', fun=ship.move_left)
screen.onkey(key='d', fun=ship.move_right)
screen.onkey(key='w',fun=ship.shoot)

points = 0
game_on = False
DIAMETER = 40

while alien.lives_left > 0:
    time.sleep(0.1)
    # aliens move
    alien.move()

    # bullet motion
    if ship.stop_bullet:
        ship.bullet.hideturtle()
    else:
        ship.bullet_move()

    # aliens drops bomb randomly
    if random.randint(0, 30) == 15:
        alien.drop_bomb()

    # bombs fall
    alien.drop_move()

    # checks when a bullet hits an alien
    for creature in alien.all_alien:
        if ship.bullet.distance(creature) < 20:
            ship.stop_bullet = True
            ship.bullet.goto(0, -280)
            ship.bullet.hideturtle()
            points += 10
            creature.hideturtle()
            alien.all_alien.remove(creature)

    # checks when a bomb hits the ship
    for bomb in alien.all_bombs:
        if ship.ship.distance(bomb) < 15:
            for _ in alien.all_bombs:
                _.hideturtle()
            alien.all_bombs = []
            alien.lives_left -= 1
            ship.ship.goto(0, -200)
            ship.stop_bullet = True
            ship.bullet.goto(0, -280)
            ship.bullet.hideturtle()

        # bullet killing bombs
        if ship.bullet.distance(bomb) < 15:
            ship.stop_bullet = True
            ship.bullet.goto(0, -280)
            ship.bullet.hideturtle()
            bomb.hideturtle()
            alien.all_bombs.remove(bomb)

    # shows scoreboard and lives
    alien.scoreboard(points)
    alien.show_lives()

    # updates screen
    screen.update()

screen.clear()
screen.bgcolor("black")
alien.game_end(points)
screen.exitonclick()



screen.exitonclick()
