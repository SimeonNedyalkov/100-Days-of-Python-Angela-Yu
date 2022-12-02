import tkinter as tk
import datetime

window = tk.Tk()
window.geometry('800x600')

timer = 0
timer_label = tk.Label(text=timer, font='Aerial 24')
timer_label.grid(row =0, column = 0, pady = 20, padx = 0)
insert_here = tk.Label(text='Write your text here ↓ ', font='Aerial, 24')
insert_here.grid(row =1, column = 0, pady = 10, padx = 75)
text =tk.Text(window, state='normal')
text.insert(tk.END, "Write your text here")
text.grid(row =2, column = 0, pady = 20, padx = 75)



def write(event):
    current = text.get("1.0", tk.END)
    if current == "Write your text here\n":
        text.delete("1.0", tk.END)
    elif current == "\n":
        text.insert("1.0", "Write your text here")

def update_time():
    global timer
    if timer <= 5:
        timer_label.config(text=f'{timer}')
        timer_label.after(1000, update_time)
    if timer == 5:
        text.delete("1.0", tk.END)
    timer += 1
    if text.get("1.0", tk.END) ==  "\n":
        timer = 0
update_time()




text.bind("<FocusIn>", write)
text.bind("<FocusOut>", write)





window.mainloop()
