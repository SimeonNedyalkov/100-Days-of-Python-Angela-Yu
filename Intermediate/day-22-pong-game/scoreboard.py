from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def goal_l(self):
        self.l_score += 1
        self.update_scoreboard()

    def goal_r(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"{self.l_score}", align='left', font=('Courier', 30, 'normal'))
        self.goto(100, 250)
        self.write(f"{self.r_score}", align='left', font=('Courier', 30, 'normal'))

