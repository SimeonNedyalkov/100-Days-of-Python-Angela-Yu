from turtle import Turtle,Screen
import random

POSSITIONS = [-300, -260, -220, -180, -140, -100, -60, -20, 20, 60, 100,140,180,220,260,300]
list_of_colors = ['yellow', 'gold', 'orange', 'red', 'maroon', 'violet', 'turquoise', 'lightgreen', 'green', 'darkgreen',]

class Block():
    def __init__(self):
        self.all_blocks = []
        self.screen = Screen()


    def random_place(self):
        random_y = random.randint(200,200)
        random_x = random.choice(POSSITIONS)
        self.block.penup()
        self.block.goto(random_x,random_y)
        self.block.pendown()

    def create_blocks(self):
        for pos_y in range(3,4):
            for pos_x in range(-4, 5):
                 self.add_block(pos_x,pos_y)

    def add_block(self,x, y):
        self.block = Turtle()
        self.block.shape('square')
        self.block.color(random.choice(list_of_colors))
        self.block.shapesize(stretch_wid=1, stretch_len=2)
        self.block.penup()
        self.block.goto(x*80, y*80)
        self.block.pendown()
        self.all_blocks.append(self.block)

