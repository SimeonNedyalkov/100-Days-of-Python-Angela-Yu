import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


########### Challenge 4 - Random Walk ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tupple = (r, g, b)
    return my_tupple


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.circle(100)
        tim.speed("fastest")
        tim.color(random_color())
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
