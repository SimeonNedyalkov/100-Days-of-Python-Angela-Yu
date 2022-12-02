from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    reps += 1
    if reps % 8 == 0:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break)
        timer_label.config(text="Break", fg= PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work")
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds <= 9:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text= f"{count_minute}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions= math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
            check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")

window.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white",font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1,column=1)
reset = Button(text="reset",highlightthickness=0, command=reset_timer)
reset.grid(row=2,column=2)

timer_label = Label(text="TIMER", font=(FONT_NAME, 20, "bold"), fg=GREEN)
timer_label.grid(row=0,column=1)

check_mark = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN)
check_mark.grid(row=2, column=1)

start = Button(text="start", command=start_timer)
start.grid(row=2,column=0)

window.mainloop()
