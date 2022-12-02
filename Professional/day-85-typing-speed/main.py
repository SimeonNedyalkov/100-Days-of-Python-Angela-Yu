import tkinter as tk
import time
from datetime import datetime, timedelta
import random

window = tk.Tk()
window.geometry('1000x900')

game_on = False
wordcount = 0
count = 00
minutes = 00

time_label = tk.Label(text=f'Timer: 00:0{count}', font=("Aerial, 24"))
time_label.pack()

words = ['programming', 'coding', 'algorithm', 'systems', 'python', 'software']
write_those_words_label = tk.Label(text=f"{words}")
write_those_words_label.pack()

def update():
    global count, game_on,minutes
    count += 1
    if count >= 60:
        time_label.after_cancel()
        return game_on == True
    if count >= 10:
        time_label.config(text=f'Timer: 00:{count}')
        time_label.after(1000, update)
    if count < 10:
        time_label.config(text=f'Timer: 00:0{count}')
        time_label.after(1000, update)


def submit():
    global wordcount
    for word in words:
        input_value = textbox.get()
        if word == input_value:
            wordcount += 1
            print(input_value)

def check_word():
    global wordcount
    for word in words:
        input_value = textbox.get()
        if word == input_value:
            wordcount += 1
            print(input_value)


textbox = tk.Entry(window)
textbox.pack()

word_count = tk.Label(text=wordcount)
word_count.pack()



start_label = tk.Button(text="Start", font='Aerial, 10', command=update)
start_label.pack(padx=10, pady=10)
submit = tk.Button(text='Submit', width=10, command=submit)
submit.pack()

while game_on == False:
    for word in words:
        input_value = textbox.get()
        if word == input_value:
            wordcount += 1
            print(input_value)
    if game_on == True:
        break








    window.mainloop()
