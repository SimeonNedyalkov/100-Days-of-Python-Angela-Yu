from turtle import Screen
from ship import Ship
from lazer import Lazer

window = Screen()
window.setup(width=900, height=600)
window.bgcolor('black')
window.listen()

ship = Ship()
lazer = Lazer()
lazer.create_lazer(ship.xcor(),ship.ycor())
window.onkey(key='a', fun=ship.move_left)
window.onkey(key='d', fun=ship.move_right)
window.onkey(key='w', fun=lazer.shoot)

if lazer.shoot():
    lazer.create_lazer(ship.xcor(),ship.ycor())



window.mainloop()
