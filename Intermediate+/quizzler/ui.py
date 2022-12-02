from tkinter import *

import data
from quiz_brain import QuizBrain
from data import question_data
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.data = question_data
        self.window = Tk()
        self.window.config(padx=20,pady=20,background=THEME_COLOR)
        self.window.title("Quizzler")
        self.score_label = Label(text="Score:",background=THEME_COLOR,highlightthickness=0,foreground="white")
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(height=250, width=300,bg="white")
        self.canvas.grid(row=1,column=0,columnspan=2, pady=50)
        true = PhotoImage(file="images/true.png")
        false = PhotoImage(file="images/false.png")
        self.question_text = self.canvas.create_text(150,125,text="Question",fill=THEME_COLOR,font=("Arial",20,"bold"), width=280)
        self.truebutton = Button(image=true, command=self.true_button)
        self.truebutton.grid(row=2, column=0)
        self.falsebutton = Button(image=false,command=self.false_button)
        self.falsebutton.grid(row=2, column=1)
        self.get_next_question()




        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz :)")
            self.truebutton.config(state="disabled")
            self.falsebutton.config(state="disabled")


    def true_button(self) -> bool:
        self.give_feedback(self.quiz.check_answer("True"))


    def false_button(self) -> bool:
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
