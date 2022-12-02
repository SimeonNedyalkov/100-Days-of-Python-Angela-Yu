import tkinter
window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=100, height=200)
window.config(padx=20, pady=20)

def miles():
    miles = float(input.get())
    km = miles * 1.609
    results.config(text= f"{km}")

input = tkinter.Entry()
input.grid(row=0, column=2)

miles_label = tkinter.Label(text="miles", font=("Arial", 12, "bold"))
miles_label.grid(row=0, column=3)

equal_to = tkinter.Label(text=f"is equal to: ")
equal_to.grid(row=2, column=0)

results = tkinter.Label(text= f"0")
results.grid(row=2, column=2)

button = tkinter.Button(text= "Calculate", command=miles)
button.grid(row=3, column=2)

km_lebel = tkinter.Label(text= "km")
km_lebel.grid(row= 2, column=3)








window.mainloop()
