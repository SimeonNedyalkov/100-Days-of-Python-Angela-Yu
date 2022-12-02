import pyautogui as pg

from PIL import Image, ImageGrab

from numpy import asarray

import time
x= 151
y= -330
# coordinates = ['x=591, y=400']

time.sleep(2)
pg.move(-820,720,2)
pg.leftClick()
pg.move(x,y, 2)
def press():
    pg.press('num8')
    return

def isCollision(Data):

# Check colison for birds

    # for i in range(470,500):
    #
    #     for j in range(260,270):
    #
    #         if Data[i, j] < 171:
    #
    #             pg.press("num2")
    #
    #             return

# Check colison for cactus

    for i in range(470,520):

        for j in range(x,y):

            if Data[i, j] < 200:

                pg.press("num8")

                return

    return



if __name__ =="__main__":

    time.sleep(5)

    pg.press("num8")




    while True:

        image=ImageGrab.grab().convert("L")

        Data=image.load()

        isCollision(Data)
