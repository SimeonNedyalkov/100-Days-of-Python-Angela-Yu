import csv

BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random

current_card = {}
try:
    data = pandas.read_csv("data/Words to learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

#------- switch card -------
def flip():
    canvas.itemconfig(card_background, image=canvas_image_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")






#------- generate word -------
def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=canvas_front_image)
    window.after(3000, func=flip)

def i_know():
    generate_word()
    print(len(to_learn))
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/Words to learn.csv", index= False)



#------ user settings -------
window = Tk()
window.title("Flash-card-project")
window.config(pady=50, padx=50, background=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, func=flip)

canvas = Canvas(width=800, height=526)
canvas_front_image = PhotoImage(file="../flash-card-project-start/images/card_front.png")
canvas_image_back = PhotoImage(file="../flash-card-project-start/images/card_back.png")
card_background = canvas.create_image(400, 263, image=canvas_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_title = canvas.create_text(400,150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400,263, text="Word", font= ("Arial", 60, "bold"))


x_button_image = PhotoImage(file="../flash-card-project-start/images/wrong.png")
wrong_button = Button(image=x_button_image, highlightthickness=0, command=generate_word)
wrong_button.grid(row=1, column=0)

j_button_image = PhotoImage(file="../flash-card-project-start/images/right.png")
right_button = Button(image=j_button_image, highlightthickness=0, command=i_know)
right_button.grid(row=1, column=1)








window.mainloop()
