from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.blocks_score = 0
        self.update_scoreboard()

    def destroyed_blocks(self):
        self.blocks_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f"Blocks destroyed: {self.blocks_score}", align='left', font=('Courier', 30, 'normal'))